from ...common_descs import *
from .objs.tag import HekTag
from supyr_struct.defs.tag_def import TagDef

wind_body = Struct("tagdata",
    from_to_wu("velocity"),
    yp_float_rad("variation_area"),
    Float("local_variation_weight"),
    Float("local_variation_rate"),
    Float("damping"),
    SIZE=64,
    )


def get():
    return wind_def

wind_def = TagDef("wind",
    blam_header('wind'),
    wind_body,

    ext=".wind", endian=">", tag_cls=HekTag
    )
