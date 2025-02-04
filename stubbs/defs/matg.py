from ...hek.defs.matg import *
from supyr_struct.defs.tag_def import TagDef
from ..common_descs import *

def get():
    return matg_def

matg_body = Struct('tagdata',
    Pad(248),
    reflexive("sounds", sound, 2,
        "enter water", "exit water"),
    reflexive("cameras", camera, 1),
    reflexive("player_controls", player_control, 1),
    reflexive("difficulties", difficulty, 1),
    reflexive("grenades", grenade, len(grenade_types), *grenade_types),
    reflexive("rasterizer_datas", rasterizer_data, 1),
    reflexive("interface_bitmaps", interface_bitmaps, 1),
    reflexive("cheat_weapons", cheat_weapon, 20,
        DYN_NAME_PATH='.weapon.filepath'),
    reflexive("cheat_powerups", cheat_powerup, 20,
        DYN_NAME_PATH='.powerup.filepath'),
    reflexive("multiplayer_informations", multiplayer_information, 1),
    reflexive("player_informations", player_information, 1),
    reflexive("first_person_interfaces", first_person_interface, 1),
    reflexive("falling_damages", falling_damage, 1),
    reflexive("materials", material, len(materials_list), *materials_list),
    reflexive("playlist_members", playlist_member, 20,
        DYN_NAME_PATH='.map_name'),

    SIZE=428
    )

matg_def = TagDef("matg",
    blam_header_stubbs('matg', 3),
    matg_body,

    ext=".globals", endian=">"
    )
