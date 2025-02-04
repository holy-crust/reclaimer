from reclaimer.h2.common_descs import *
from supyr_struct.defs.tag_def import TagDef

sound_classes = (
    ("projectile impact", 0),
    ("projectile detonation", 1),
    ("projectile flyby", 2),

    ("weapon fire", 4),
    ("weapon ready", 5),
    ("weapon reload", 6),
    ("weapon empty", 7),
    ("weapon charge", 8),
    ("weapon overheat", 9),
    ("weapon idle", 10),
    ("weapon melee", 11),
    ("weapon animation", 12),
    ("object impacts", 13),
    ("particle impacts", 14),

    ("unit footsteps", 18),
    ("unit dialog", 19),
    ("unit animation", 20),

    ("vehicle collision", 22),
    ("vehicle engine", 23),
    ("vehicle animation", 20),

    ("device door", 26),
    ("device machinery", 28),
    ("device stationary", 29),

    ("music", 32),
    ("ambient nature", 33),
    ("ambient machinery", 34),

    ("huge ass", 36),
    ("object looping", 37),
    ("cinematic music", 38),

    ("cortana mission", 45),
    ("cortana cinematic", 46),
    ("mission dialog", 47),
    ("cinematic dialog", 48),
    ("scripted cinematic foley", 49),
    ("game event", 50),
    ("ui", 51),
    ("test", 52),
    ("multilingual test", 53),
    )

snd__body = Struct("tagdata",
    Bool16("flags",
        "fit to adpcm blocksize",
        "split long sounds into permutations",
        "always spatialize",
        "never obstruct",
        {NAME: "INTERNAL DONT TOUCH", EDITABLE:False},
        "use huge sound transmission"
        "link count to owner unit",
        "pitch range is language",
        "dont use sound class speaker flags",
        "dont use lipsync data",
        ),
    UEnum8("sound_class", *sound_classes),
    UEnum8("sample rate",
        {NAME: "khz_22", GUI_NAME: "22kHz"},
        {NAME: "khz_44", GUI_NAME: "44kHz"},
        {NAME: "khz_32", GUI_NAME: "32kHz"},
        ),
    UEnum8("encoding",
        "mono",
        "stereo",
        "codec",
        ),
    UEnum8("compression",
        "none (big endian)",
        "xbox adpcm",
        "ima adpcm",
        "none (little endian)",
        "wma",
        ),
    SInt16("playback_parameter_index"),
    SInt16("pitch_range_index"),
    SInt8("pitch_range_count"),
    SInt8("scale_index"),
    SInt8("promotion_index"),
    SInt8("custom_playback_index"),
    SInt16("extra_info_index"),
    SInt32("maximum_play_time"),
    ENDIAN="<", SIZE=20
    )


def get():
    return snd__def

snd__def = TagDef("snd!",
    h2_blam_header('snd!'),
    snd__body,

    ext=".%s" % h2_tag_class_fcc_to_ext["snd!"], endian="<"
    )
