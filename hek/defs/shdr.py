from ...common_descs import *
from .objs.shdr import ShdrTag
from supyr_struct.defs.tag_def import TagDef

radiosity_comment = """RADIOSITY/LIGHTMAPPING
The simple parameterisation flag is used for shaders that are on surfaces with more curved
shapes like grass hills. It avoids lightmap uv problems by using the uvs from the bsp geometry.
The ignore normals flag helps with shading bugs on double sided polygons by making the 
light independent of normals.(Suggested use: tree leaves).

The detail level controls the relative quality of the lightmaps/lightmap uvs for this shader."""

lighting_comment = """LIGHT
Light power controls the brightness and reach of the light emitted by this shader 
during lightmap rendering.
"""

material_type_comment = """MATERIAL TYPE
The material type is used to determine what material effects should be used for impacts on 
BSP geometry that uses this shader."""

shdr_attrs = Struct("shdr_attrs",
    Bool16("radiosity_flags",
        { NAME: "simple_parameterization", GUI_NAME: "simple parameterization(lightmap fix)" },
        "ignore_normals",
        "transparent_lit",
        COMMENT=radiosity_comment
        ),
    SEnum16("radiosity_detail_level" ,
        "high",
        "medium",
        "low",
        "turd",
        ),
    Float("radiosity_light_power", COMMENT=lighting_comment),
    QStruct("radiosity_light_color", INCLUDE=rgb_float),
    QStruct("radiosity_tint_color",  INCLUDE=rgb_float),

    Pad(2),
    SEnum16("material_type", *materials_list, COMMENT=material_type_comment),
    # THIS FIELD IS OFTEN INCORRECT ON STOCK TAGS.
    FlSEnum16("shader_type",
        *((shader_types[i], i - 1) for i in
          range(len(shader_types))),
        VISIBLE=False, DEFAULT=-1
        ),
    Pad(2),
    SIZE=40
    )

shader_body = Struct("tagdata",
    shdr_attrs,
    SIZE=40
    )

def get():
    return shdr_def

shdr_def = TagDef("shdr",
    blam_header('shdr'),
    shader_body,

    ext=".shader", endian=">", tag_cls=ShdrTag
    )
