import math
import os
import re
import traceback

from copy import deepcopy
from reclaimer.util import float_to_str, float_to_str_truncate,\
     parse_jm_float, parse_jm_int


class JmsNode:
    __slots__ = (
        "name",
        "first_child", "sibling_index", "parent_index",
        "rot_i", "rot_j", "rot_k", "rot_w",
        "pos_x", "pos_y", "pos_z",
        )
    def __init__(self, name="", first_child=-1, sibling_index=-1,
                 rot_i=0.0, rot_j=0.0, rot_k=0.0, rot_w=1.0,
                 pos_x=0.0, pos_y=0.0, pos_z=0.0, parent_index=-1):
        self.name = name
        self.sibling_index = sibling_index
        self.first_child = first_child
        self.rot_i = rot_i
        self.rot_j = rot_j
        self.rot_k = rot_k
        self.rot_w = rot_w
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.parent_index = parent_index

    def __repr__(self):
        return """JmsNode(name=%s,
    first_child=%s, sibling_index=%s,
    i=%s, j=%s, k=%s, w=%s,
    x=%s, y=%s, z=%s
)""" % (self.name, self.first_child, self.sibling_index,
        self.rot_i, self.rot_j, self.rot_k, self.rot_w,
        self.pos_x, self.pos_y, self.pos_z)

    def __eq__(self, other):
        if not isinstance(other, JmsNode):
            return False
        elif self.name != other.name:
            return False
        elif self.first_child != other.first_child:
            return False
        elif self.sibling_index != other.sibling_index:
            return False
        elif (abs(self.rot_i - other.rot_i) > 0.00001 or
              abs(self.rot_j - other.rot_j) > 0.00001 or
              abs(self.rot_k - other.rot_k) > 0.00001 or
              abs(self.rot_w - other.rot_w) > 0.00001):
            return False
        elif (abs(self.pos_x - other.pos_x) > 0.00001 or
              abs(self.pos_y - other.pos_y) > 0.00001 or
              abs(self.pos_z - other.pos_z) > 0.00001):
            return False
        return True

    def is_node_hierarchy_equal(self, other):
        if not isinstance(other, JmsNode):
            return False
        elif self.name != other.name:
            return False
        elif self.first_child != other.first_child:
            return False
        elif self.sibling_index != other.sibling_index:
            return False
        return True

    @classmethod
    def setup_node_hierarchy(cls, nodes, jms_version="8200"):
        if jms_version == "8200":
            # Halo 1
            parented_nodes = set()
            # setup the parent node hierarchy
            for parent_idx in range(len(nodes)):
                node = nodes[parent_idx]
                if node.first_child > 0:
                    sib_idx = node.first_child
                    seen_nodes = set()
                    while sib_idx >= 0:
                        if (sib_idx in seen_nodes or sib_idx == parent_idx or
                            sib_idx >= len(nodes)):
                            break
                        seen_nodes.add(sib_idx)
                        parented_nodes.add(sib_idx)
                        sib_node = nodes[sib_idx]
                        sib_node.parent_index = parent_idx
                        sib_idx = sib_node.sibling_index
        elif jms_version == "8210":
            # Halo 2
            pass


class JmsMaterial:
    __slots__ = (
        "name", "tiff_path",
        "shader_path", "shader_type",
        "properties"
        )
    def __init__(self, name="__unnamed", tiff_path="<none>",
                 shader_path="", shader_type="", properties=""):
        for c in "!@#$%^&*-.":
            if c in name and c not in properties:
                properties += c
            name = name.replace(c, '')

        self.name = name
        self.tiff_path = tiff_path
        self.shader_path = shader_path if shader_path else name
        self.shader_type = shader_type
        self.properties = properties

    @property
    def ai_defeaning(self): return "&" in self.properties
    @ai_defeaning.setter
    def ai_defeaning(self, new_val):
        self.properties = self.properties.replace("&", "") + ("&" if new_val else "")

    @property
    def allow_transparency(self): return "#" in self.properties
    @allow_transparency.setter
    def allow_transparency(self, new_val):
        self.properties = self.properties.replace("#", "") + ("#" if new_val else "")

    @property
    def breakable(self): return "-" in self.properties
    @breakable.setter
    def breakable(self, new_val):
        self.properties = self.properties.replace("-", "") + ("-" if new_val else "")

    # collision_only means the player collides, but not projectiles
    @property
    def collision_only(self): return "@" in self.properties
    @collision_only.setter
    def collision_only(self, new_val):
        self.properties = self.properties.replace("@", "") + ("@" if new_val else "")

    @property
    def double_sided(self): return "%" in self.properties
    @double_sided.setter
    def double_sided(self, new_val):
        self.properties = self.properties.replace("%", "") + ("%" if new_val else "")

    @property
    def exact_portal(self): return "." in self.properties
    @exact_portal.setter
    def exact_portal(self, new_val):
        self.properties = self.properties.replace(".", "") + ("." if new_val else "")

    @property
    def fog_plane(self): return "$" in self.properties
    @fog_plane.setter
    def fog_plane(self, new_val):
        self.properties = self.properties.replace("$", "") + ("$" if new_val else "")

    @property
    def ladder(self): return "^" in self.properties
    @ladder.setter
    def ladder(self, new_val):
        self.properties = self.properties.replace("^", "") + ("^" if new_val else "")

    # this is what sky and invisible collision get set to
    @property
    def large_collideable(self): return "*" in self.properties
    @large_collideable.setter
    def large_collideable(self, new_val):
        self.properties = self.properties.replace("*", "") + ("*" if new_val else "")

    @property
    def render_only(self): return "!" in self.properties
    @render_only.setter
    def render_only(self, new_val):
        self.properties = self.properties.replace("!", "") + ("!" if new_val else "")

    def __repr__(self):
        return """JmsMaterial(name=%s,
    tiff_path=%s
)""" % (self.name, self.tiff_path)


class JmsMarker:
    __slots__ = (
        "name", "permutation",
        "region", "parent",
        "rot_i", "rot_j", "rot_k", "rot_w",
        "pos_x", "pos_y", "pos_z",
        "radius",
        )
    def __init__(self, name="", permutation="", region=0, parent=0,
                 rot_i=0.0, rot_j=0.0, rot_k=0.0, rot_w=1.0,
                 pos_x=0.0, pos_y=0.0, pos_z=0.0, radius=0.0):
        self.name = name
        self.permutation = permutation
        self.parent = parent
        self.region = max(0, region)
        self.rot_i = rot_i
        self.rot_j = rot_j
        self.rot_k = rot_k
        self.rot_w = rot_w
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.radius = radius

    def __repr__(self):
        return """JmsMarker(name=%s,
    permutation=%s,
    region=%s,  parent=%s,
    i=%s, j=%s, k=%s, w=%s,
    x=%s, y=%s, z=%s,
    radius=%s
)""" % (self.name, self.permutation, self.region, self.parent,
        self.rot_i, self.rot_j, self.rot_k, self.rot_w,
        self.pos_x, self.pos_y, self.pos_z, self.radius)

    def __eq__(self, other):
        if not isinstance(other, JmsMarker):
            return False
        elif self.name != other.name:
            return False
        elif self.permutation != other.permutation:
            return False
        elif self.region != other.region:
            return False
        elif abs(self.radius - other.radius) > 0.00001:
            return False
        elif (abs(self.rot_i - other.rot_i) > 0.00001 or
              abs(self.rot_j - other.rot_j) > 0.00001 or
              abs(self.rot_k - other.rot_k) > 0.00001 or
              abs(self.rot_w - other.rot_w) > 0.00001):
            return False
        elif (abs(self.pos_x - other.pos_x) > 0.000001 or
              abs(self.pos_y - other.pos_y) > 0.000001 or
              abs(self.pos_z - other.pos_z) > 0.000001):
            return False
        return True


class JmsVertex:
    __slots__ = (
        "node_0",
        "pos_x", "pos_y", "pos_z",
        "norm_i", "norm_j", "norm_k",
        "binorm_i", "binorm_j", "binorm_k",
        "tangent_i", "tangent_j", "tangent_k",
        "node_1", "node_1_weight",
        "tex_u", "tex_v", "tex_w",
        "other_nodes", "other_weights", "other_uvws"
        )
    def __init__(self, node_0=0,
                 pos_x=0.0, pos_y=0.0, pos_z=0.0,
                 norm_i=0.0, norm_j=0.0, norm_k=1.0,
                 node_1=-1, node_1_weight=0.0,
                 tex_u=0, tex_v=0, tex_w=0,
                 binorm_i=0.0,  binorm_j=1.0,  binorm_k=0.0,
                 tangent_i=1.0, tangent_j=0.0, tangent_k=0.0,
                 other_nodes=(), other_weights=(), other_uvws=()):
        if node_1_weight <= 0:
            node_1 = -1
            node_1_weight = 0

        self.node_0 = node_0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.norm_i = norm_i
        self.norm_j = norm_j
        self.norm_k = norm_k
        self.binorm_i = binorm_i
        self.binorm_j = binorm_j
        self.binorm_k = binorm_k
        self.tangent_i = tangent_i
        self.tangent_j = tangent_j
        self.tangent_k = tangent_k
        self.node_1 = node_1
        self.node_1_weight = node_1_weight
        self.tex_u = tex_u
        self.tex_v = tex_v
        self.tex_w = tex_w
        self.other_nodes = other_nodes
        self.other_weights = other_weights
        self.other_uvws = other_uvws

        norm_len = self.norm_i**2 + self.norm_j**2 + self.norm_k**2
        if norm_len > 0.0:
            norm_len = math.sqrt(norm_len)
            self.norm_i /= norm_len
            self.norm_j /= norm_len
            self.norm_k /= norm_len

    def __repr__(self):
        return """JmsVertex(node_0=%s,
    x=%s, y=%s, z=%s,
    i=%s, j=%s, k=%s,
    node_1=%s, node_1_weight=%s,
    u=%s, v=%s, w=%s
)""" % (self.node_0,
        self.pos_x, self.pos_y, self.pos_z,
        self.norm_i, self.norm_j, self.norm_k,
        self.node_1, self.node_1_weight,
        self.tex_u, self.tex_v, self.tex_w)

    def __eq__(self, other):
        if not isinstance(other, JmsVertex):
            return False
        elif (abs(self.pos_z  - other.pos_z)  > 0.00001 or
              abs(self.norm_k - other.norm_k) > 0.0001):
            return False
        elif (abs(self.pos_x - other.pos_x) > 0.00001 or
              abs(self.pos_y - other.pos_y) > 0.00001):
            return False
        elif (abs(self.norm_i - other.norm_i) > 0.0001 or
              abs(self.norm_j - other.norm_j) > 0.0001):
            return False
        elif abs(self.node_1_weight - other.node_1_weight) > 0.0001:
            return False
        elif self.node_0 != other.node_0 or self.node_1 != other.node_1:
            return False

        return (abs(self.tex_u - other.tex_u) <= 0.0001 and
                abs(self.tex_v - other.tex_v) <= 0.0001)


class JmsTriangle:
    __slots__ = (
        "region", "shader",
        "v0", "v1", "v2"
        )
    def __init__(self, region=0, shader=0,
                 v0=0, v1=0, v2=0):
        self.region = region
        self.shader = shader
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2

    def __getitem__(self, index):
        if   index == 0: return self.v0
        elif index == 1: return self.v1
        elif index == 2: return self.v2
        raise IndexError("Triangle indices must be in range(0, 3)")

    def __repr__(self):
        return """JmsTriangle(
    region=%s, shader=%s,
    v0=%s, v1=%s, v2=%s
)""" % (self.region, self.shader,
        self.v0, self.v1, self.v2)


class JmsModel:
    name = ""

    version = ""

    perm_name = "__base"
    lod_level = "superhigh"
    is_random_perm = True

    node_list_checksum = 0
    nodes = ()
    materials = ()
    regions = ()
    markers = ()
    verts   = ()
    tris    = ()

    def __init__(self, name="", node_list_checksum=0, nodes=None,
                 materials=None, markers=None, regions=None,
                 verts=None, tris=None, version="8200"):

        name = name.strip(" ")
        perm_name = name
        if name.startswith("~"):
            self.is_random_perm = False
            perm_name = perm_name.lstrip("~")

        self.lod_level = "superhigh"
        for lod_level in ("superhigh", "high", "medium", "superlow", "low"):
            if perm_name.lower().endswith(lod_level):
                perm_name = perm_name[: -len(lod_level)].strip(" ")
                self.lod_level = lod_level
                break

        node_list_checksum = node_list_checksum

        self.name = name
        self.version = version
        self.perm_name = perm_name
        self.node_list_checksum = node_list_checksum
        self.nodes = nodes if nodes else []
        self.materials = materials if materials else []
        self.regions = regions if regions else ["__unnamed"]
        self.markers = markers if markers else []
        self.verts   = verts   if verts   else []
        self.tris    = tris    if tris    else []

    def calculate_vertex_normals(self):
        verts = self.verts
        vert_ct = len(verts)
        sqrt = math.sqrt

        v_indices = (0, 1, 2)
        binormals = [[0, 0, 0, 0] for i in range(vert_ct)]
        tangents  = [[0, 0, 0, 0] for i in range(vert_ct)]
        for tri in self.tris:
            for tri_i in v_indices:
                v_i = tri[tri_i]
                if v_i >= vert_ct:
                    continue

                v0 = verts[v_i]
                v1 = verts[tri[(tri_i + 1) % 3]]
                v2 = verts[tri[(tri_i + 2) % 3]]
                b = binormals[v_i]
                t = tangents[v_i]

                x0 = v1.pos_x - v0.pos_x;
                x1 = v2.pos_x - v0.pos_x;
                y0 = v1.pos_y - v0.pos_y;
                y1 = v2.pos_y - v0.pos_y;
                z0 = v1.pos_z - v0.pos_z;
                z1 = v2.pos_z - v0.pos_z;


                s0 = v1.tex_u - v0.tex_u;
                s1 = v2.tex_u - v0.tex_u;
                t0 = v1.tex_v - v0.tex_v;
                t1 = v2.tex_v - v0.tex_v;

                r = s0 * t1 - s1 * t0
                if r == 0:
                    continue

                r = 1 / r

                bi = -(s0 * x1 - s1 * x0) * r
                bj = -(s0 * y1 - s1 * y0) * r
                bk = -(s0 * z1 - s1 * z0) * r
                b_len = sqrt(bi**2 + bj**2 + bk**2)

                ti = (t1 * x0 - t0 * x1) * r
                tj = (t1 * y0 - t0 * y1) * r
                tk = (t1 * z0 - t0 * z1) * r
                t_len = sqrt(ti**2 + tj**2 + tk**2)

                if b_len:
                    b[0] += bi / b_len
                    b[1] += bj / b_len
                    b[2] += bk / b_len
                    b[3] += 1

                if t_len:
                    t[0] += ti / t_len
                    t[1] += tj / t_len
                    t[2] += tk / t_len
                    t[3] += 1

        for i in range(vert_ct):
            vert = verts[i]
            b = binormals[i]
            t = tangents[i]

            if b[3]:
                vert.binorm_i = b[0] / b[3]
                vert.binorm_j = b[1] / b[3]
                vert.binorm_k = b[2] / b[3]

            if t[3]:
                vert.tangent_i = t[0] / t[3]
                vert.tangent_j = t[1] / t[3]
                vert.tangent_k = t[2] / t[3]

    def optimize_geometry(self, exact_compare=True):
        verts = self.verts
        vert_ct = len(verts)

        # this will map the verts to prune to the vert they are identical to
        dup_vert_map = {}
        similar_vert_map = {}

        if exact_compare:
            for i in range(len(verts)):
                v = verts[i]
                similar_vert_map.setdefault(
                    (v.pos_x, v.pos_y, v.pos_z), []).append(i)

            # loop over all verts and figure out which ones to replace with others
            for similar_vert_indices in similar_vert_map.values():
                for i in range(len(similar_vert_indices) - 1):
                    orig_idx = similar_vert_indices[i]
                    if orig_idx in dup_vert_map:
                        continue

                    vert_a = verts[orig_idx]
                    vert_a_i = vert_a.norm_i; vert_a_j = vert_a.norm_j; vert_a_k = vert_a.norm_k
                    vert_a_u = vert_a.tex_u;  vert_a_v = vert_a.tex_v
                    vert_a_n0 = vert_a.node_0; vert_a_n1 = vert_a.node_1
                    vert_a_n1w = vert_a.node_1_weight
                    for j in similar_vert_indices[i + 1: ]:
                        if j in dup_vert_map:
                            continue

                        vert_b = verts[j]
                        if (vert_a_i != vert_b.norm_i or
                            vert_a_j != vert_b.norm_j or
                            vert_a_k != vert_b.norm_k):
                            continue
                        elif vert_a_n1w != vert_b.node_1_weight:
                            continue
                        elif vert_a_n0 != vert_b.node_0 or vert_a_n1 != vert_b.node_1:
                            continue
                        elif vert_a_u != vert_b.tex_u or vert_a_v != vert_b.tex_v:
                            continue

                        dup_vert_map[j] = orig_idx
        else:
            for i in range(len(verts)):
                v = verts[i]
                similar_vert_map.setdefault(
                    (round(v.pos_x + 0.001, 3),
                     round(v.pos_y + 0.001, 3),
                     round(v.pos_z + 0.001, 3)), []).append(i)

            # loop over all verts and figure out which ones to replace with others
            for similar_vert_indices in similar_vert_map.values():
                for i in range(len(similar_vert_indices) - 1):
                    orig_idx = similar_vert_indices[i]
                    if orig_idx in dup_vert_map:
                        continue

                    vert_a = verts[orig_idx]
                    for j in similar_vert_indices[i + 1: ]:
                        if j not in dup_vert_map and verts[j] == vert_a:
                            dup_vert_map[j] = orig_idx

        if not dup_vert_map:
            # nothing to optimize away
            return

        # remap any duplicate triangle vert indices to the original
        get_mapped_vert = dup_vert_map.get
        for tri in self.tris:
            tri.v0 = get_mapped_vert(tri.v0, tri.v0)
            tri.v1 = get_mapped_vert(tri.v1, tri.v1)
            tri.v2 = get_mapped_vert(tri.v2, tri.v2)

        # copy the verts list so we can modify it without side-effects
        new_vert_ct = vert_ct - len(dup_vert_map)
        self.verts = new_verts = self.verts[: new_vert_ct]

        shift_map = {}
        copy_idx = vert_ct - 1
        # loop over all duplicate vert indices and move any vertices
        # on the high end of the vert list down to fill in the empty
        # spaces left by the duplicate verts we're removing.
        for dup_i in sorted(dup_vert_map):
            while copy_idx in dup_vert_map:
                # keep looping until we get to a vert we can move
                # from its high index to overwrite the low index dup
                copy_idx -= 1

            if copy_idx <= dup_i or dup_i >= new_vert_ct:
                # cant copy any lower. all upper index verts are duplicates
                break

            # move the vert from its high index to the low index dup
            new_verts[dup_i] = verts[copy_idx]
            shift_map[copy_idx] = dup_i
            copy_idx -= 1

        # remap any triangle vert indices
        get_mapped_vert = shift_map.get
        for tri in self.tris:
            tri.v0 = get_mapped_vert(tri.v0, tri.v0)
            tri.v1 = get_mapped_vert(tri.v1, tri.v1)
            tri.v2 = get_mapped_vert(tri.v2, tri.v2)

    def get_node_depths(self):
        node_depths = [-1] * len(self.nodes)
        if not self.nodes:
            return node_depths

        node_depths[0] = 0

        seen_hierarchy = set((-1, ))
        # figure out the hierarchy depth of each node
        for i in range(len(self.nodes)):
            child_depth = node_depths[i] + 1
            child_idx = self.nodes[i].first_child
            while (child_idx not in seen_hierarchy and
                   child_idx in range(len(self.nodes))):
                seen_hierarchy.add(child_idx)
                node_depths[child_idx] = child_depth
                child_idx = self.nodes[child_idx].sibling_index

        return node_depths

    def verify_nodes_valid(self):
        errors = []
        if len(self.nodes) == 0:
            errors.append("No nodes. Must contain at least one node.")
            return errors

        if len(self.nodes) >= 64:
            errors.append("Too many nodes. Max count is 64.")

        seen_names = set()
        for i in range(len(self.nodes)):
            n = self.nodes[i]
            if n.first_child >= len(self.nodes):
                errors.append("First child of node '%s' is invalid." % n.name)
            elif n.sibling_index >= len(self.nodes):
                errors.append("Sibling node of node '%s' is invalid." % n.name)
            elif len(n.name) >= 32:
                errors.append("Node name node '%s' is too long." % n.name)
            elif n.name.lower() in seen_names:
                errors.append("Multiple nodes named '%s'." % n.name)

            seen_names.add(n.name.lower())

        if self.nodes and self.nodes[0].sibling_index != -1:
            errors.append("Root node must not have siblings.")

        node_depths = self.get_node_depths()

        # make sure the nodes are sorted in increasing hierarchy depth
        curr_depth = node_depths[0]
        prev_name = ""
        for i in range(len(node_depths)):
            if curr_depth > node_depths[i]:
                errors.append("Nodes are not sorted by hierarchy depth.")
                break

            curr_name = self.nodes[i].name
            if curr_depth != node_depths[i]:
                curr_depth = node_depths[i]
            elif curr_name < prev_name:
                errors.append(("Nodes within depth %s are not sorted "
                               "alphabetically.") % curr_depth)
                break

            prev_name = curr_name

        sib_errors = set()
        child_errors = set()
        seen_hierarchy = set()
        for node in self.nodes:
            sib_idx = node.sibling_index
            child_idx = node.first_child

            if child_idx in child_errors:
                pass
            elif child_idx in seen_hierarchy:
                errors.append(
                    "Node %s is specified as the child of multiple nodes." %
                    self.nodes[child_idx].name)
            elif child_idx >= 0:
                seen_hierarchy.add(child_idx)
                seen_children = set()
                while child_idx >= 0:
                    child_node = self.nodes[child_idx]
                    if child_idx in seen_children:
                        errors.append("Circular reference in children " +
                                      "of node '%s'." % node.name)
                        break

                    seen_children.add(child_idx)
                    child_idx = child_node.first_child

            if sib_idx in sib_errors:
                pass
            elif sib_idx in seen_hierarchy:
                errors.append(
                    "Node %s is specified as the sibling of multiple nodes." %
                    self.nodes[sib_idx].name)
            elif sib_idx >= 0:
                seen_hierarchy.add(sib_idx)
                seen_siblings = set()
                while sib_idx >= 0:
                    sib_node = self.nodes[sib_idx]
                    if sib_idx in seen_siblings:
                        errors.append("Circular reference in siblings " +
                                      "of node '%s'." % node.name)
                        break

                    seen_siblings.add(sib_idx)
                    sib_idx = sib_node.sibling_index


        return errors

    def verify_models_match(self, other_jms):
        errors = list(other_jms.verify_jms())
        if len(other_jms.nodes) != len(self.nodes):
            errors.append("Node counts do not match.")
            return errors

        for i in range(len(self.nodes)):
            if self.nodes[i] != other_jms.nodes[i]:
                errors.append("Nodes '%s' do not match." % i)

        return errors

    def verify_jms(self):
        crc = self.node_list_checksum
        mats  = self.materials
        markers = self.markers
        regions = self.regions

        if isinstance(self, MergedJmsModel):
            perm_meshes = self.perm_meshes
        else:
            perm_meshes = {self.name: self}

        node_error = False

        node_ct = len(self.nodes)
        region_ct = len(regions)
        mat_ct = len(mats)

        errors = self.verify_nodes_valid()
        if errors:
            return errors

        err_str = "Invalid %s index in %s(s)."
        for region_name in regions:
            if len(region_name) >= 32:
                errors.append("Region name '%s' is too long." % region_name)

        for marker in markers:
            if marker.parent >= node_ct:
                errors.append(err_str % ("parent", "marker"))
            elif marker.region >= region_ct:
                errors.append(err_str % ("region", "marker"))
            elif len(marker.name) >= 32:
                errors.append("Marker name '%s' is too long." % marker.name)
            else:
                continue
            break

        for perm_name in sorted(perm_meshes):
            verts = perm_meshes[perm_name].verts
            tris  = perm_meshes[perm_name].tris
            vert_ct = len(verts)
            for tri in tris:
                if (tri.v0 < 0 or tri.v1 < 0 or tri.v2 < 0 or
                    tri.v0 >= vert_ct or tri.v1 >= vert_ct or tri.v2 >= vert_ct):
                    errors.append(err_str % ("vertex", "triangle"))
                elif tri.region >= region_ct:
                    errors.append(err_str % ("region", "triangle"))
                elif tri.shader >= mat_ct:
                    errors.append(err_str % ("shader", "triangle"))
                else:
                    continue
                break

            for vert in verts:
                if vert.node_0 >= node_ct:
                    errors.append(err_str % ("node_0", "vertex"))
                elif vert.node_1 >= node_ct:
                    errors.append(err_str % ("node_1", "vertex"))
                else:
                    continue
                break

        return errors


class GeometryMesh:
    verts = ()
    tris  = ()
    local_nodes = []
    def __init__(self, verts=(), tris=()):
        self.verts = verts if verts else []
        self.tris  = tris  if tris  else []


class PermutationMesh:
    markers = ()
    lod_meshes = ()
    is_random_perm = True

    def __init__(self):
        self.markers = []
        self.lod_meshes = {}


class MergedJmsRegion:
    name = ""
    perm_meshes = ()
    _split_by_shader = True

    def __init__(self, name, *jms_models, split_by_shader=True):
        self.name = name
        self._split_by_shader = split_by_shader
        self.perm_meshes = {}

        for jms_model in jms_models:
            self.merge_jms_model(jms_model)

    def merge_jms_model(self, jms_model, merged_jms_materials):
        assert isinstance(jms_model, JmsModel)
        try:
            src_region_index = jms_model.regions.index(self.name)
        except ValueError:
            # this region is not in the jms model provided
            return

        lod_level = jms_model.lod_level
        perm_name = jms_model.perm_name

        if perm_name not in self.perm_meshes:
            self.perm_meshes[perm_name] = PermutationMesh()
            self.perm_meshes[perm_name].is_random_perm = jms_model.is_random_perm

        perm_mesh = self.perm_meshes[perm_name]
        # copy the markers from the JmsModel we're given for this region,
        # BUT only do so if the lod_level is superhigh(this is what tool
        # does, and it makes sense to do it this way to prevent duplicates).
        if jms_model.lod_level == "superhigh":
            for marker in jms_model.markers:
                if marker.region == src_region_index:
                    perm_mesh.markers.append(marker)

        mesh_data = perm_mesh.lod_meshes.setdefault(lod_level, {})

        src_verts = jms_model.verts
        src_tris  = jms_model.tris
        region_verts = []
        region_tris = [None] * len(src_tris)

        mat_indices_by_name, i = {}, 0
        for mat in merged_jms_materials:
            mat_indices_by_name.setdefault(mat.name, []).append(i)
            i += 1

        mat_map, i = [0] * len(jms_model.materials), 0
        for mat in jms_model.materials:
            mat_map[i] = mat_indices_by_name[mat.name].pop(0)
            i += 1

        vert_map = dict()
        get_add_vert = vert_map.setdefault
        v_base = len(region_verts)
        tri_ct = 0
        mat_nums = set()
        for tri in src_tris:
            if tri.region == src_region_index:
                mat_num = mat_map[tri.shader]
                # region number doesnt matter at this point for triangles
                # since it isnt stored in compiled models, so set it to -1
                tri = JmsTriangle(-1, mat_num, tri.v0, tri.v1, tri.v2)
                tri.v0 = get_add_vert(tri.v0, v_base + len(vert_map))
                tri.v1 = get_add_vert(tri.v1, v_base + len(vert_map))
                tri.v2 = get_add_vert(tri.v2, v_base + len(vert_map))
                mat_nums.add(mat_num)
                region_tris[tri_ct] = tri
                tri_ct += 1

        if tri_ct == 0:
            return

        # collect all the verts and triangles used by this region
        region_verts.extend([None] * len(vert_map))
        for i, j in vert_map.items():
            v = src_verts[i]
            region_verts[j] = JmsVertex(
                v.node_0, v.pos_x, v.pos_y, v.pos_z,
                v.norm_i, v.norm_j, v.norm_k, v.node_1, v.node_1_weight,
                v.tex_u, v.tex_v, v.tex_w,
                v.binorm_i,  v.binorm_j,  v. binorm_k,
                v.tangent_i, v.tangent_j, v.tangent_k)

        del region_tris[tri_ct: ]

        if len(mat_nums) == 1 or not self._split_by_shader:
            for mat_num in mat_nums: break
            if not self._split_by_shader:
                mat_num = -1

            mesh_data[mat_num] = GeometryMesh()
            mesh_data[mat_num].verts = region_verts
            mesh_data[mat_num].tris  = region_tris
            return

        # make a mesh for each material
        for mat_num in mat_nums:
            if mat_num not in mesh_data:
                mesh_data[mat_num] = GeometryMesh()

            mat_verts = mesh_data[mat_num].verts
            mat_tris  = mesh_data[mat_num].tris

            vert_map = dict()
            get_add_vert = vert_map.setdefault
            v_base = len(mat_verts)
            tri_ct = 0
            for tri in region_tris:
                if tri.shader == mat_num:
                    tri.v0 = get_add_vert(tri.v0, v_base + len(vert_map))
                    tri.v1 = get_add_vert(tri.v1, v_base + len(vert_map))
                    tri.v2 = get_add_vert(tri.v2, v_base + len(vert_map))
                    tri_ct += 1

            mat_verts.extend([None] * len(vert_map))
            for i, j in vert_map.items():
                mat_verts[j] = region_verts[i]

            i = len(mat_tris)
            mat_tris.extend([None] * tri_ct)
            for tri in region_tris:
                if tri.shader == mat_num:
                    mat_tris[i] = tri
                    i += 1


class MergedJmsModel:
    node_list_checksum = 0
    nodes = ()
    materials = ()
    regions = ()

    u_scale = 1.0
    v_scale = 1.0

    def __init__(self, *jms_models):
        self.nodes = []
        self.materials = []
        self.regions = {}

        for jms_model in jms_models:
            self.merge_jms_model(jms_model)

    def calc_uv_scales(self):
        u_scale = self.u_scale
        v_scale = self.v_scale
        calc_u_scale = 0.0
        calc_v_scale = 0.0
        for region in self.regions.values():
            for perm_mesh in region.perm_meshes.values():
                for meshes in perm_mesh.lod_meshes.values():
                    for lod_mesh_list in perm_mesh.lod_meshes.values():
                        for mesh in lod_mesh_list.values():
                            for vert in mesh.verts:
                                calc_u_scale = max(abs(vert.tex_u * u_scale),
                                                   calc_u_scale)
                                calc_v_scale = max(abs(vert.tex_v * v_scale),
                                                   calc_v_scale)

        return calc_u_scale, calc_v_scale

    verify_models_match = JmsModel.verify_models_match

    def merge_jms_model(self, other_model):
        all_errors = {}
        first_nodes = None

        if not other_model:
            return

        if not self.nodes:
            self.node_list_checksum = other_model.node_list_checksum
            self.nodes = []
            self.materials = []
            for node in other_model.nodes:
                self.nodes.append(
                    JmsNode(
                        node.name, node.first_child, node.sibling_index,
                        node.rot_i, node.rot_j, node.rot_k, node.rot_w,
                        node.pos_x, node.pos_y, node.pos_z, node.parent_index)
                    )

            for mat in other_model.materials:
                self.materials.append(
                    JmsMaterial(
                        mat.name, mat.tiff_path, mat.shader_path,
                        mat.shader_type, mat.properties)
                    )

            self.regions = {}

        errors = self.verify_models_match(other_model)
        if errors:
            return errors

        new_mat_counts = {}
        for mat in self.materials:
            new_mat_counts[mat.name] = new_mat_counts.get(mat.name, 0) - 1

        default_mats = {}
        for mat in other_model.materials:
            default_mats.setdefault(mat.name, mat)
            new_mat_counts[mat.name] = new_mat_counts.get(mat.name, 0) + 1

        for mat_name, mat_ct in new_mat_counts.items():
            if mat_ct > 0:
                self.materials.extend((default_mats[mat_name], ) * mat_ct)

        # merge each region from the other model into this ones regions
        for region in other_model.regions:
            if region not in self.regions:
                self.regions[region] = MergedJmsRegion(region)

            self.regions[region].merge_jms_model(other_model, self.materials)

        # correct the region index numbers for each marker in the regions
        i = 0
        for region_name in sorted(self.regions):
            perm_meshes = self.regions[region_name].perm_meshes
            for perm_mesh in perm_meshes.values():
                for marker in perm_mesh.markers:
                    marker.region = i
            i += 1

        return all_errors


def read_jms(jms_string, stop_at="", perm_name=None):
    if perm_name is None:
        perm_name = "__unnamed"

    jms_model = JmsModel(perm_name)

    jms_data = tuple(d for d in jms_string.\
                     replace("\n", "\t").split("\t") if d)

    jms_model.version = str(parse_jm_int(jms_data[0]))

    if jms_model.version == "8200":
        # Halo 1
        return _read_jms_8200(jms_model, jms_data, stop_at)
    elif jms_model.version == "8210":
        # Halo 2
        return _read_jms_8210(jms_model, jms_data, stop_at)
    else:
        print("Unknown JMS version '%s'" % jms_model.version)
        return None


def _read_jms_8200(jms_model, jms_data, stop_at=""):
    # Halo 1
    try:
        jms_model.node_list_checksum = parse_jm_int(jms_data[1])
    except Exception:
        print(traceback.format_exc())
        print("Could not read node list checksum.")
        return jms_model

    if stop_at == "nodes": return jms_model

    dat_i = 2

    # read the nodes
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.nodes[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.nodes)):
            jms_model.nodes[i] = JmsNode(
                jms_data[dat_i], parse_jm_int(jms_data[dat_i+1]), parse_jm_int(jms_data[dat_i+2]),
                parse_jm_float(jms_data[dat_i+3]), parse_jm_float(jms_data[dat_i+4]),
                parse_jm_float(jms_data[dat_i+5]), parse_jm_float(jms_data[dat_i+6]),
                parse_jm_float(jms_data[dat_i+7]), parse_jm_float(jms_data[dat_i+8]), parse_jm_float(jms_data[dat_i+9]),
                )
            dat_i += 10
        JmsNode.setup_node_hierarchy(jms_model.nodes)
    except Exception:
        print(traceback.format_exc())
        print("Failed to read nodes.")
        del jms_model.nodes[i: ]
        return jms_model

    if stop_at == "materials": return jms_model

    # read the materials
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.materials[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.materials)):
            jms_model.materials[i] = JmsMaterial(jms_data[dat_i], jms_data[dat_i+1])
            dat_i += 2
    except Exception:
        print(traceback.format_exc())
        print("Failed to read materials.")
        del jms_model.materials[i: ]
        return jms_model

    if stop_at == "markers": return jms_model

    # read the markers
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.markers[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.markers)):
            jms_model.markers[i] = JmsMarker(
                jms_data[dat_i], jms_model.name,
                parse_jm_int(jms_data[dat_i+1]), parse_jm_int(jms_data[dat_i+2]),
                parse_jm_float(jms_data[dat_i+3]), parse_jm_float(jms_data[dat_i+4]),
                parse_jm_float(jms_data[dat_i+5]), parse_jm_float(jms_data[dat_i+6]),
                parse_jm_float(jms_data[dat_i+7]), parse_jm_float(jms_data[dat_i+8]), parse_jm_float(jms_data[dat_i+9]),
                parse_jm_float(jms_data[dat_i+10])
                )
            dat_i += 11
    except Exception:
        print(traceback.format_exc())
        print("Failed to read markers.")
        del jms_model.markers[i: ]
        return jms_model

    if stop_at == "regions": return jms_model

    # read the regions
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.regions[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.regions)):
            jms_model.regions[i] = jms_data[dat_i]
            dat_i += 1
    except Exception:
        print(traceback.format_exc())
        print("Failed to read regions.")
        del jms_model.regions[i: ]
        return jms_model

    if stop_at == "vertices": return jms_model

    # read the vertices
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.verts[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.verts)):
            jms_model.verts[i] = JmsVertex(
                parse_jm_int(jms_data[dat_i]),
                parse_jm_float(jms_data[dat_i+1]), parse_jm_float(jms_data[dat_i+2]), parse_jm_float(jms_data[dat_i+3]),
                parse_jm_float(jms_data[dat_i+4]), parse_jm_float(jms_data[dat_i+5]), parse_jm_float(jms_data[dat_i+6]),
                parse_jm_int(jms_data[dat_i+7]), parse_jm_float(jms_data[dat_i+8]),
                parse_jm_float(jms_data[dat_i+9]), parse_jm_float(jms_data[dat_i+10]), parse_jm_float(jms_data[dat_i+11])
                )
            dat_i += 12
    except Exception:
        print(traceback.format_exc())
        print("Failed to read vertices.")
        del jms_model.verts[i: ]
        return jms_model

    if stop_at == "triangles": return jms_model

    # read the triangles
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.tris[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.tris)):
            jms_model.tris[i] = JmsTriangle(
                parse_jm_int(jms_data[dat_i]), parse_jm_int(jms_data[dat_i+1]),
                parse_jm_int(jms_data[dat_i+2]), parse_jm_int(jms_data[dat_i+3]), parse_jm_int(jms_data[dat_i+4]),
                )
            dat_i += 5
    except Exception:
        print(traceback.format_exc())
        print("Failed to read triangles.")
        del jms_model.tris[i: ]
        return jms_model

    return jms_model


def _read_jms_8210(jms_model, jms_data, stop_at=""):
    # NOTE: This function is incomplete. Do not expect it to work

    # Halo 2
    if stop_at == "nodes": return jms_model

    dat_i = 1

    # read the nodes
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.nodes[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.nodes)):
            jms_model.nodes[i] = JmsNode(
                jms_data[dat_i], -1, -1,  # these will need to be calculated
                parse_jm_float(jms_data[dat_i+1]), parse_jm_float(jms_data[dat_i+2]),
                parse_jm_float(jms_data[dat_i+3]), parse_jm_float(jms_data[dat_i+4]),
                parse_jm_float(jms_data[dat_i+5]), parse_jm_float(jms_data[dat_i+6]),
                parse_jm_float(jms_data[dat_i+7]), parse_jm_int(jms_data[dat_i+8]),
                )
            dat_i += 9
        JmsNode.setup_node_hierarchy(jms_model.nodes, jms_model.version)
    except Exception:
        print(traceback.format_exc())
        print("Failed to read nodes.")
        del jms_model.nodes[i: ]
        return jms_model

    if stop_at == "materials": return jms_model

    # read the materials
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.materials[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.materials)):
            jms_model.materials[i] = JmsMaterial(jms_data[dat_i])
            # TODO: Figure out what the other 4 material values are
            dat_i += 5
    except Exception:
        print(traceback.format_exc())
        print("Failed to read materials.")
        del jms_model.materials[i: ]
        return jms_model

    if stop_at == "markers": return jms_model

    # read the markers
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.markers[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.markers)):
            jms_model.markers[i] = JmsMarker(
                jms_data[dat_i], jms_model.name, -1, parse_jm_int(jms_data[dat_i+1]),
                parse_jm_float(jms_data[dat_i+2]), parse_jm_float(jms_data[dat_i+3]),
                parse_jm_float(jms_data[dat_i+4]), parse_jm_float(jms_data[dat_i+5]),
                parse_jm_float(jms_data[dat_i+6]), parse_jm_float(jms_data[dat_i+7]), parse_jm_float(jms_data[dat_i+8]),
                parse_jm_float(jms_data[dat_i+9])
                )
            dat_i += 10
    except Exception:
        print(traceback.format_exc())
        print("Failed to read markers.")
        del jms_model.markers[i: ]
        return jms_model

    if stop_at == "instance_xrefs": return jms_model

    # read the instance xrefs
    try:
        i = 0 # make sure i is defined in case of exception
        instance_xrefs = [(None, ) * parse_jm_int(jms_data[dat_i])]
        dat_i += 1
        for i in range(len(instance_xrefs)):
            instance_xrefs[i] = (jms_data[dat_i], jms_data[dat_i+1])
            dat_i += 2
    except Exception:
        print(traceback.format_exc())
        print("Failed to read instance xrefs.")


    if stop_at == "instance_markers": return jms_model

    # read the instance markers
    try:
        i = 0 # make sure i is defined in case of exception
        instance_markers = [(None, ) * parse_jm_int(jms_data[dat_i])]
        dat_i += 1
        for i in range(len(instance_markers)):
            instance_markers[i] = JmsMarker(
                jms_data[dat_i], jms_model.name, -1,
                parse_jm_float(jms_data[dat_i+3]), parse_jm_float(jms_data[dat_i+4]),
                parse_jm_float(jms_data[dat_i+5]), parse_jm_float(jms_data[dat_i+6]),
                parse_jm_float(jms_data[dat_i+7]), parse_jm_float(jms_data[dat_i+8]), parse_jm_float(jms_data[dat_i+9]),
                )
            dat_i += 10
    except Exception:
        print(traceback.format_exc())
        print("Failed to read instance markers.")
        del instance_markers[i: ]
        return jms_model


    if stop_at == "vertices": return jms_model

    # read the vertices
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.verts[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.verts)):
            x, y, z = parse_jm_float(jms_data[dat_i]),   parse_jm_float(jms_data[dat_i+1]),  parse_jm_float(jms_data[dat_i+2])
            a, b, c = parse_jm_float(jms_data[dat_i+3]), parse_jm_float(jms_data[dat_i+4]),  parse_jm_float(jms_data[dat_i+5])
            u, v, w = parse_jm_float(jms_data[dat_i+9]), parse_jm_float(jms_data[dat_i+10]), parse_jm_float(jms_data[dat_i+11])
            dat_i += 6
            node_influences = [(-1, 0)] * 4
            node_influences_count = parse_jm_int(jms_data[dat_i])
            dat_i += 1
            for j in range(node_influences_count):
                node_influences[j] = (parse_jm_int(jms_data[dat_i]), parse_jm_int(jms_data[dat_i+1]))
                dat_i += 2

            tex_coords = [(0, 0)] * parse_jm_int(jms_data[dat_i])
            dat_i += 1
            for j in range(len(tex_coords)):
                tex_coords[j] = (parse_jm_int(jms_data[dat_i]), parse_jm_int(jms_data[dat_i+1]))
                dat_i += 2

            jms_model.verts[i] = JmsVertex(
                node_influences[0][0], x, y, z, a, b, c,
                node_influences[1][0], node_influences[1][1],
                tex_coords[0][0], tex_coords[0][1], 0,
                0, 1, 0, 1, 0, 0
                )
            dat_i += 12
    except Exception:
        print(traceback.format_exc())
        print("Failed to read vertices.")
        del jms_model.verts[i: ]
        return jms_model

    if stop_at == "triangles": return jms_model

    # read the triangles
    try:
        i = 0 # make sure i is defined in case of exception
        jms_model.tris[:] = ((None, ) * parse_jm_int(jms_data[dat_i]))
        dat_i += 1
        for i in range(len(jms_model.tris)):
            jms_model.tris[i] = JmsTriangle(
                -1, parse_jm_int(jms_data[dat_i]),
                parse_jm_int(jms_data[dat_i+1]), parse_jm_int(jms_data[dat_i+2]), parse_jm_int(jms_data[dat_i+3]),
                )
            dat_i += 4
    except Exception:
        print(traceback.format_exc())
        print("Failed to read triangles.")
        del jms_model.tris[i: ]
        return jms_model

    return jms_model


def write_jms(filepath, jms_model, use_blitzkrieg_rounding=False):
    if use_blitzkrieg_rounding:
        to_str = lambda f: float_to_str_truncate(f, 6)
    else:
        to_str = float_to_str

    materials = jms_model.materials
    regions = jms_model.regions

    # If the path doesnt exist, create it
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    if not regions:
        regions = ("__unnamed", )

    if not materials:
        materials = (JmsMaterial("__unnamed", "<none>"), )

    with open(filepath, "w", encoding='latin1') as f:
        f.write("%s\n" % jms_model.version)
        f.write("%s\n" % int(jms_model.node_list_checksum))

        f.write("%s\n" % len(jms_model.nodes))
        for node in jms_model.nodes:
            f.write("%s\n%s\n%s\n%s\t%s\t%s\t%s\n%s\t%s\t%s\n" % (
                node.name[: 31], node.first_child, node.sibling_index,
                to_str(node.rot_i), to_str(node.rot_j),
                to_str(node.rot_k), to_str(node.rot_w),
                to_str(node.pos_x), to_str(node.pos_y), to_str(node.pos_z),
                )
            )

        f.write("%s\n" % len(materials))
        for mat in materials:
            f.write("%s\n%s\n" % (mat.name + mat.properties, mat.tiff_path))

        f.write("%s\n" % len(jms_model.markers))
        for marker in jms_model.markers:
            f.write("%s\n%s\n%s\n%s\t%s\t%s\t%s\n%s\t%s\t%s\n%s\n" % (
                marker.name[: 31], marker.region, marker.parent,
                to_str(marker.rot_i), to_str(marker.rot_j),
                to_str(marker.rot_k), to_str(marker.rot_w),
                to_str(marker.pos_x), to_str(marker.pos_y), to_str(marker.pos_z),
                to_str(marker.radius)
                )
            )

        f.write("%s\n" % len(regions))
        for region in regions:
            f.write("%s\n" % region[: 31])

        f.write("%s\n" % len(jms_model.verts))
        for vert in jms_model.verts:
            f.write("%s\n%s\t%s\t%s\n%s\t%s\t%s\n%s\n%s\n%s\n%s\n%s\n" % (
                vert.node_0,
                to_str(vert.pos_x),  to_str(vert.pos_y),  to_str(vert.pos_z),
                to_str(vert.norm_i), to_str(vert.norm_j), to_str(vert.norm_k),
                vert.node_1,
                to_str(vert.node_1_weight),
                to_str(vert.tex_u), to_str(vert.tex_v), to_str(vert.tex_w),
                )
            )

        f.write("%s\n" % len(jms_model.tris))
        for tri in jms_model.tris:
            f.write("%s\n%s\n%s\t%s\t%s\n" % (
                tri.region, tri.shader,
                tri.v0, tri.v1, tri.v2
                )
            )


def generate_fake_nodes(node_count):
    nodes = []
    if node_count <= 0:
        return nodes

    nodes.append(JmsNode("fake_node0", 1, -1))
    for i in range(1, node_count):
        nodes.append(JmsNode("fake_node%s" % i, -1, i + 1))

    nodes[-1].first_child = -1
    nodes[-1].sibling_index = -1
    JmsNode.setup_node_hierarchy(nodes)
    return nodes


def edge_loop_to_strippable_tris(edge_loop, region=0, mat_id=0):
    tris = [None] * (len(edge_loop) - 2)
    vert_ct = len(edge_loop)

    even_face_ct = (vert_ct - 1) // 2
    odd_face_ct = (vert_ct - 2) // 2

    # make the even faces
    v0 = edge_loop[0]
    for i in range(even_face_ct):
        v1 = edge_loop[i + 1]
        v2 = edge_loop[vert_ct - 1 - i]
        tris[i << 1] = JmsTriangle(region, mat_id, v0, v1, v2)

        v0 = v2

    # make the odd faces
    v0 = edge_loop[1]
    for i in range(odd_face_ct):
        v1 = edge_loop[i + 2]
        v2 = edge_loop[vert_ct - 1 - i]
        tris[(i << 1) + 1] = JmsTriangle(region, mat_id, v0, v1, v2)

        v0 = v1

    return tris


def edge_loop_to_fannable_tris(edge_loop, region=0, mat_id=0):
    vert_index_count = len(edge_loop)
    v0 = edge_loop[0]
    return [JmsTriangle(region, mat_id, v0,
                        edge_loop[((i + 1) % vert_index_count)],
                        edge_loop[((i + 2) % vert_index_count)])
            for i in range(len(edge_loop) - 2)]


def edge_loop_to_tris(edge_loop_or_vert_index_count, region=0, mat_id=0,
                      base=0, make_fan=False):
    if isinstance(edge_loop_or_vert_index_count, int):
        edge_loop = list(range(base, base + edge_loop_or_vert_index_count))
    else:
        edge_loop = edge_loop_or_vert_index_count

    if make_fan:
        return edge_loop_to_fannable_tris(edge_loop, region, mat_id)

    return edge_loop_to_strippable_tris(edge_loop, region, mat_id)
