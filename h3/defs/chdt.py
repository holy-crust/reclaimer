############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/12/03  04:56
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: -DeToX-
# 	Fixed up the layout, mapped out some values..
# revision: 3		author: DarkShallFall
# 	More unknowns and types.
# revision: 4		author: DarkShallFall
# 	Plugin getting close to complete. A little more effort and we will be there.
# revision: 5		author: Lord Zedd
# 	Overhauled.
# revision: 6		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################

from ..common_descs import *
from .objs.tag import *
from supyr_struct.defs.tag_def import TagDef

chdt_hud_widget_animation_data_animation_1_function = (
    "default",
    "use_input",
    "use_range_input",
    "zero",
    )

chdt_hud_widget_placement_data_anchor = (
    "top_left",
    "top_right",
    "bottom_right",
    "bottom_left",
    "center",
    "top_edge",
    "grenade_a",
    "grenade_b",
    "grenade_c",
    "grenade_d",
    "scoreboard_friendly",
    "scoreboard_enemy",
    "health_and_shield",
    "bottom_edge",
    "unknown_0",
    "equipment",
    "unknown_1",
    "depreciated_0",
    "depreciated_1",
    "depreciated_2",
    "depreciated_3",
    "depreciated_4",
    "unknown_2",
    "gametype",
    "unknown_3",
    "state_right",
    "state_left",
    "state_center",
    "unknown_4",
    "gametype_friendly",
    "gametype_enemy",
    "metagame_top",
    "metagame_player_1",
    "metagame_player_2",
    "metagame_player_3",
    "metagame_player_4",
    "theater",
    )

chdt_hud_widget_render_data_input = (
    "zero",
    "one",
    "time",
    "fade",
    "unit_shield_current",
    "unit_shield",
    "clip_ammo_fraction",
    "total_ammo_fraction",
    "heat_fraction",
    "battery_fraction",
    "pickup",
    "unit_autoaimed",
    "grenade",
    "grenade_fraction",
    "charge_fraction",
    "friendly_score",
    "enemy_score",
    "score_to_win",
    "arming_fraction",
    "unknown_0",
    "unit_1x_overshield_current",
    "unit_1x_overshield",
    "unit_2x_overshield_current",
    "unit_2x_overshield",
    "unit_3x_overshield_current",
    "unit_3x_overshield",
    "aim_yaw",
    "aim_pitch",
    "target_distance",
    "target_elevation",
    "editor_budget",
    "editor_budget_cost",
    "film_total_time",
    "film_current_time",
    "unknown_1",
    "film_timeline_fraction_1",
    "film_timeline_fraction_2",
    "unknown_2",
    "unknown_3",
    "metagame_time",
    "metagame_score_transient",
    "metagame_score_player_1",
    "metagame_score_player_2",
    "metagame_score_player_3",
    "metagame_score_player_4",
    "metagame_modifier",
    "unknown_4",
    "sensor_range",
    "netdebug_latency",
    "netdebug_latency_quality",
    "netdebug_host_quality",
    "netdebug_local_quality",
    "metagame_score_negative",
    )

chdt_hud_widget_render_data_output_color_a = (
    "local_a",
    "local_b",
    "local_c",
    "local_d",
    "unknown_4",
    "unknown_5",
    "scoreboard_friendly",
    "scoreboard_enemy",
    "arming_team",
    "metagame_player_1",
    "metagame_player_2",
    "metagame_player_3",
    "metagame_player_4",
    "unknown_13",
    "global_dynamic_0",
    "global_dynamic_1",
    "global_dynamic_2",
    "global_dynamic_3",
    "global_dynamic_4",
    "global_dynamic_5",
    "global_dynamic_6",
    "global_dynamic_7",
    "global_dynamic_8",
    "global_dynamic_9",
    "global_dynamic_10",
    "global_dynamic_11",
    "global_dynamic_12",
    "global_dynamic_13",
    "global_dynamic_14",
    "global_dynamic_15",
    "global_dynamic_16",
    "global_dynamic_17",
    "global_dynamic_18",
    "global_dynamic_19",
    "global_dynamic_20",
    "global_dynamic_21",
    "global_dynamic_22",
    "global_dynamic_23",
    "global_dynamic_24",
    "global_dynamic_25",
    "global_dynamic_26",
    "global_dynamic_27",
    )

chdt_hud_widget_render_data_output_scalar_a = (
    "input",
    "range_input",
    "local_a",
    "local_b",
    "local_c",
    "local_d",
    "unknown_6",
    "unknown_7",
    )

chdt_hud_widget_render_data_shader_index = (
    "simple",
    "meter",
    "text_simple",
    "meter_shield",
    "meter_gradient",
    "crosshair",
    "directional_damage",
    "solid",
    "sensor",
    "meter_single_color",
    "navpoint",
    "medal",
    "texture_cam",
    "cortana_screen",
    "cortana_camera",
    "cortana_offscreen",
    "cortana_screen_final",
    "meter_chapter",
    "meter_double_gradient",
    "meter_radial_gradient",
    "turbulence",
    "emblem",
    "cortana_composite",
    "directional_damage_apply",
    "really_simple",
    )

chdt_hud_widget_special_hud_type = (
    "unspecial",
    "ammo",
    "crosshair_and_scope",
    "unit_shield_meter",
    "grenades",
    "gametype",
    "motion_sensor",
    "spike_grenade",
    "firebomb_grenade",
    )

chdt_hud_widget_text_widget_font = (
    "conduit_18_0",
    "fixedsys_9_0",
    "fixedsys_9_1",
    "conduit_16_0",
    "conduit_32_0",
    "conduit_32_1",
    "conduit_23",
    "larabie_10",
    "conduit_18_1",
    "conduit_16_1",
    "pragmata_14",
    )


chdt_hud_widget_state_data = Struct("state_data", 
    Bool16("_1_engine", 
        ("capture_the_flag", 1 << 4),
        "slayer",
        "oddball",
        "king_of_the_hill",
        "juggernaut",
        "territories",
        "assault",
        "vip",
        "infection",
        ("editor", 1 << 14),
        "theater",
        ),
    Bool16("_2", 
        "biped_1",
        "biped_2",
        "biped_3",
        ),
    Bool16("_3", 
        "offense",
        "defense",
        "free_for_all",
        ("talking_disabled", 1 << 6),
        "tap_to_talk",
        "talking_enabled",
        "not_talking",
        "talking",
        ),
    Bool16("_4_resolution", *unknown_flags_16),
    Bool16("_5_scoreboard", 
        "has_friends",
        "has_enemies",
        "has_variant_name",
        "someone_is_talking",
        "is_arming",
        "time_enabled",
        "friends_have_x",
        "enemies_have_x",
        "friends_are_x",
        "enemies_are_x",
        "x_is_down",
        "summary_enabled",
        "netdebug",
        ),
    Bool16("_6", 
        "texture_cam_enabled",
        "autoaim",
        ("training_prompt", 1 << 4),
        "objective_prompt",
        ),
    Bool16("_7_editor", 
        "editor_inactive",
        "editor_active",
        "editor_holding",
        "editor_not_allowed",
        "is_editor_biped",
        ),
    Bool16("_8", 
        "motion_tracker_10m",
        "motion_tracker_25m",
        "motion_tracker_75m",
        "motion_tracker_150m",
        ("metagame_player_2_exists", 1 << 6),
        ("metagame_player_3_exists", 1 << 8),
        ("metagame_player_4_exists", 1 << 10),
        ("metagame_score_added", 1 << 12),
        ("metagame_score_removed", 1 << 14),
        ),
    Bool16("_9", 
        "pickup_grenades",
        ),
    Bool16("_10", 
        "binoculars_enabled",
        "unit_is_zoomed_level_1",
        "unit_is_zoomed_level_2",
        ),
    Bool16("_11", 
        "primary_weapon",
        "secondary_weapon",
        ),
    Bool16("_12", 
        "motion_tracker_enabled",
        ("selected_frag_grenades", 1 << 2),
        "selected_plasma_grenades",
        "selected_spike_grenades",
        "selected_fire_grenades",
        ("has_1x_overshield", 1 << 12),
        "has_2x_overshield",
        "has_3x_overshield",
        "has_shields",
        ),
    Bool16("_13", 
        ("pickup_ammo", 1 << 1),
        ),
    Bool16("_14", 
        "primary_weapon",
        "secondary_weapon",
        "backpack",
        ),
    Bool16("_15", 
        "not_autoaim",
        "autoaim_friendly",
        "autoaim_enemy",
        "autoaim_headshot",
        ("plasma_locked_on", 1 << 7),
        ),
    Bool16("_16", 
        ("missile_locked", 1 << 1),
        "missile_locking",
        ),
    Bool16("_17", 
        ("has_frag_grenades", 1 << 2),
        "has_plasma_grenades",
        "has_spike_grenades",
        "has_fire_grenades",
        ),
    Bool16("_18_ammo", 
        "clip_warning",
        "ammo_warning",
        ("low_battery_1", 1 << 4),
        "low_battery_2",
        "overheated",
        ),
    Bool16("_19", 
        "binoculars_enabled",
        "unit_is_zoomed_level_1",
        "unit_is_zoomed_level_2",
        ),
    SInt16("unknown", VISIBLE=False),
    ENDIAN=">", SIZE=40
    )


chdt_hud_widget_placement_data = Struct("placement_data", 
    SEnum16("anchor", *chdt_hud_widget_placement_data_anchor),
    SInt16("unknown", VISIBLE=False),
    QStruct("mirror_offset", INCLUDE=xy_float),
    QStruct("offset", INCLUDE=xy_float),
    QStruct("scale", INCLUDE=xy_float),
    ENDIAN=">", SIZE=28
    )


chdt_hud_widget_animation_data = Struct("animation_data", 
    Bool16("animation_1_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_1_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_1"),
    Bool16("animation_2_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_2_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_2"),
    Bool16("animation_3_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_3_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_3"),
    Bool16("animation_4_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_4_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_4"),
    Bool16("animation_5_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_5_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_5"),
    Bool16("animation_6_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_6_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_6"),
    ENDIAN=">", SIZE=120
    )


chdt_hud_widget_render_data = Struct("render_data", 
    SEnum16("shader_index", *chdt_hud_widget_render_data_shader_index),
    SInt16("unknown", VISIBLE=False),
    SEnum16("input", *chdt_hud_widget_render_data_input),
    SEnum16("range_input", *chdt_hud_widget_render_data_input),
    color_argb_uint32("local_color_a"),
    color_argb_uint32("local_color_b"),
    color_argb_uint32("local_color_c"),
    color_argb_uint32("local_color_d"),
    Float("local_scalar_a"),
    Float("local_scalar_b"),
    Float("local_scalar_c"),
    Float("local_scalar_d"),
    SEnum16("output_color_a", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_b", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_c", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_d", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_e", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_f", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_scalar_a", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_b", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_c", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_d", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_e", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_f", *chdt_hud_widget_render_data_output_scalar_a),
    ENDIAN=">", SIZE=64
    )


chdt_hud_widget_bitmap_widget_state_data = Struct("state_data", 
    Bool16("_1_engine", 
        ("capture_the_flag", 1 << 4),
        "slayer",
        "oddball",
        "king_of_the_hill",
        "juggernaut",
        "territories",
        "assault",
        "vip",
        "infection",
        ("editor", 1 << 14),
        "theater",
        ),
    Bool16("_2", 
        "biped_1",
        "biped_2",
        "biped_3",
        ),
    Bool16("_3", 
        "offense",
        "defense",
        "free_for_all",
        ("talking_disabled", 1 << 6),
        "tap_to_talk",
        "talking_enabled",
        "not_talking",
        "talking",
        ),
    Bool16("_4_resolution", *unknown_flags_16),
    Bool16("_5_scoreboard", 
        "has_friends",
        "has_enemies",
        "has_variant_name",
        "someone_is_talking",
        "is_arming",
        "time_enabled",
        "friends_have_x",
        "enemies_have_x",
        "friends_are_x",
        "enemies_are_x",
        "x_is_down",
        "summary_enabled",
        "netdebug",
        ),
    Bool16("_6", 
        "texture_cam_enabled",
        "autoaim",
        ("training_prompt", 1 << 4),
        "objective_prompt",
        ),
    Bool16("_7_editor", 
        "editor_inactive",
        "editor_active",
        "editor_holding",
        "editor_not_allowed",
        "is_editor_biped",
        ),
    Bool16("_8", 
        "motion_tracker_10m",
        "motion_tracker_25m",
        "motion_tracker_75m",
        "motion_tracker_150m",
        ("metagame_player_2_exists", 1 << 6),
        ("metagame_player_3_exists", 1 << 8),
        ("metagame_player_4_exists", 1 << 10),
        ("metagame_score_added", 1 << 12),
        ("metagame_score_removed", 1 << 14),
        ),
    Bool16("_9", 
        "pickup_grenades",
        ),
    Bool16("_10", 
        "binoculars_enabled",
        "unit_is_zoomed_level_1",
        "unit_is_zoomed_level_2",
        ),
    Bool16("_11", 
        "primary_weapon",
        "secondary_weapon",
        ),
    Bool16("_12", 
        "motion_tracker_enabled",
        ("selected_frag_grenades", 1 << 2),
        "selected_plasma_grenades",
        "selected_spike_grenades",
        "selected_fire_grenades",
        ("has_1x_overshield", 1 << 12),
        "has_2x_overshield",
        "has_3x_overshield",
        "has_shields",
        ),
    Bool16("_13", 
        ("pickup_ammo", 1 << 1),
        ),
    Bool16("_14", 
        "primary_weapon",
        "secondary_weapon",
        "backpack",
        ),
    Bool16("_15", 
        "not_autoaim",
        "autoaim_friendly",
        "autoaim_enemy",
        "autoaim_headshot",
        ("plasma_locked_on", 1 << 7),
        ),
    Bool16("_16", 
        ("missile_locked", 1 << 1),
        "missile_locking",
        ),
    Bool16("_17", 
        ("has_frag_grenades", 1 << 2),
        "has_plasma_grenades",
        "has_spike_grenades",
        "has_fire_grenades",
        ),
    Bool16("_18_ammo", 
        "clip_warning",
        "ammo_warning",
        ("low_battery_1", 1 << 4),
        "low_battery_2",
        "overheated",
        ),
    Bool16("_19", 
        "binoculars_enabled",
        "unit_is_zoomed_level_1",
        "unit_is_zoomed_level_2",
        ),
    SInt16("unknown", VISIBLE=False),
    ENDIAN=">", SIZE=40
    )


chdt_hud_widget_bitmap_widget_placement_data = Struct("placement_data", 
    SEnum16("anchor", *chdt_hud_widget_placement_data_anchor),
    SInt16("unknown", VISIBLE=False),
    QStruct("mirror_offset", INCLUDE=xy_float),
    QStruct("offset", INCLUDE=xy_float),
    QStruct("scale", INCLUDE=xy_float),
    ENDIAN=">", SIZE=28
    )


chdt_hud_widget_bitmap_widget_animation_data = Struct("animation_data", 
    Bool16("animation_1_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_1_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_1"),
    Bool16("animation_2_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_2_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_2"),
    Bool16("animation_3_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_3_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_3"),
    Bool16("animation_4_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_4_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_4"),
    Bool16("animation_5_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_5_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_5"),
    Bool16("animation_6_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_6_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_6"),
    ENDIAN=">", SIZE=120
    )


chdt_hud_widget_bitmap_widget_render_data = Struct("render_data", 
    SEnum16("shader_index", *chdt_hud_widget_render_data_shader_index),
    SInt16("unknown", VISIBLE=False),
    SEnum16("input", *chdt_hud_widget_render_data_input),
    SEnum16("range_input", *chdt_hud_widget_render_data_input),
    color_argb_uint32("local_color_a"),
    color_argb_uint32("local_color_b"),
    color_argb_uint32("local_color_c"),
    color_argb_uint32("local_color_d"),
    Float("local_scalar_a"),
    Float("local_scalar_b"),
    Float("local_scalar_c"),
    Float("local_scalar_d"),
    SEnum16("output_color_a", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_b", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_c", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_d", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_e", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_f", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_scalar_a", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_b", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_c", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_d", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_e", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_f", *chdt_hud_widget_render_data_output_scalar_a),
    ENDIAN=">", SIZE=64
    )


chdt_hud_widget_bitmap_widget = Struct("bitmap_widget", 
    h3_string_id("name"),
    SEnum16("special_hud_type", *chdt_hud_widget_special_hud_type),
    UInt8("unknown_0", VISIBLE=False),
    UInt8("unknown_1", VISIBLE=False),
    h3_reflexive("state_data", chdt_hud_widget_bitmap_widget_state_data),
    h3_reflexive("placement_data", chdt_hud_widget_bitmap_widget_placement_data),
    h3_reflexive("animation_data", chdt_hud_widget_bitmap_widget_animation_data),
    h3_reflexive("render_data", chdt_hud_widget_bitmap_widget_render_data),
    SInt32("widget_index"),
    Bool16("flags", 
        "mirror_horizontally",
        "mirror_vertically",
        "stretch_edges",
        "enable_texture_cam",
        "looping",
        ("player_1_emblem", 1 << 6),
        "player_2_emblem",
        "player_3_emblem",
        "player_4_emblem",
        ),
    SInt16("unknown_2", VISIBLE=False),
    h3_dependency("bitmap"),
    UInt8("bitmap_sprite_index"),
    UInt8("unknown_3", VISIBLE=False),
    UInt8("unknown_4", VISIBLE=False),
    UInt8("unknown_5", VISIBLE=False),
    ENDIAN=">", SIZE=84
    )


chdt_hud_widget_text_widget_state_data = Struct("state_data", 
    Bool16("_1_engine", 
        ("capture_the_flag", 1 << 4),
        "slayer",
        "oddball",
        "king_of_the_hill",
        "juggernaut",
        "territories",
        "assault",
        "vip",
        "infection",
        ("editor", 1 << 14),
        "theater",
        ),
    Bool16("_2", 
        "biped_1",
        "biped_2",
        "biped_3",
        ),
    Bool16("_3", 
        "offense",
        "defense",
        "free_for_all",
        ("talking_disabled", 1 << 6),
        "tap_to_talk",
        "talking_enabled",
        "not_talking",
        "talking",
        ),
    Bool16("_4_resolution", *unknown_flags_16),
    Bool16("_5_scoreboard", 
        "has_friends",
        "has_enemies",
        "has_variant_name",
        "someone_is_talking",
        "is_arming",
        "time_enabled",
        "friends_have_x",
        "enemies_have_x",
        "friends_are_x",
        "enemies_are_x",
        "x_is_down",
        "summary_enabled",
        "netdebug",
        ),
    Bool16("_6", 
        "texture_cam_enabled",
        "autoaim",
        ("training_prompt", 1 << 4),
        "objective_prompt",
        ),
    Bool16("_7_editor", 
        "editor_inactive",
        "editor_active",
        "editor_holding",
        "editor_not_allowed",
        "is_editor_biped",
        ),
    Bool16("_8", 
        "motion_tracker_10m",
        "motion_tracker_25m",
        "motion_tracker_75m",
        "motion_tracker_150m",
        ("metagame_player_2_exists", 1 << 6),
        ("metagame_player_3_exists", 1 << 8),
        ("metagame_player_4_exists", 1 << 10),
        ("metagame_score_added", 1 << 12),
        ("metagame_score_removed", 1 << 14),
        ),
    Bool16("_9", 
        "pickup_grenades",
        ),
    Bool16("_10", 
        "binoculars_enabled",
        "unit_is_zoomed_level_1",
        "unit_is_zoomed_level_2",
        ),
    Bool16("_11", 
        "primary_weapon",
        "secondary_weapon",
        ),
    Bool16("_12", 
        "motion_tracker_enabled",
        ("selected_frag_grenades", 1 << 2),
        "selected_plasma_grenades",
        "selected_spike_grenades",
        "selected_fire_grenades",
        ("has_1x_overshield", 1 << 12),
        "has_2x_overshield",
        "has_3x_overshield",
        "has_shields",
        ),
    Bool16("_13", 
        ("pickup_ammo", 1 << 1),
        ),
    Bool16("_14", 
        "primary_weapon",
        "secondary_weapon",
        "backpack",
        ),
    Bool16("_15", 
        "not_autoaim",
        "autoaim_friendly",
        "autoaim_enemy",
        "autoaim_headshot",
        ("plasma_locked_on", 1 << 7),
        ),
    Bool16("_16", 
        ("missile_locked", 1 << 1),
        "missile_locking",
        ),
    Bool16("_17", 
        ("has_frag_grenades", 1 << 2),
        "has_plasma_grenades",
        "has_spike_grenades",
        "has_fire_grenades",
        ),
    Bool16("_18_ammo", 
        "clip_warning",
        "ammo_warning",
        ("low_battery_1", 1 << 4),
        "low_battery_2",
        "overheated",
        ),
    Bool16("_19", 
        "binoculars_enabled",
        "unit_is_zoomed_level_1",
        "unit_is_zoomed_level_2",
        ),
    SInt16("unknown", VISIBLE=False),
    ENDIAN=">", SIZE=40
    )


chdt_hud_widget_text_widget_placement_data = Struct("placement_data", 
    SEnum16("anchor", *chdt_hud_widget_placement_data_anchor),
    SInt16("unknown", VISIBLE=False),
    QStruct("mirror_offset", INCLUDE=xy_float),
    QStruct("offset", INCLUDE=xy_float),
    QStruct("scale", INCLUDE=xy_float),
    ENDIAN=">", SIZE=28
    )


chdt_hud_widget_text_widget_animation_data = Struct("animation_data", 
    Bool16("animation_1_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_1_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_1"),
    Bool16("animation_2_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_2_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_2"),
    Bool16("animation_3_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_3_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_3"),
    Bool16("animation_4_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_4_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_4"),
    Bool16("animation_5_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_5_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_5"),
    Bool16("animation_6_flags", 
        "reverse_frames",
        ),
    SEnum16("animation_6_function", *chdt_hud_widget_animation_data_animation_1_function),
    h3_dependency("animation_6"),
    ENDIAN=">", SIZE=120
    )


chdt_hud_widget_text_widget_render_data = Struct("render_data", 
    SEnum16("shader_index", *chdt_hud_widget_render_data_shader_index),
    SInt16("unknown", VISIBLE=False),
    SEnum16("input", *chdt_hud_widget_render_data_input),
    SEnum16("range_input", *chdt_hud_widget_render_data_input),
    color_argb_uint32("local_color_a"),
    color_argb_uint32("local_color_b"),
    color_argb_uint32("local_color_c"),
    color_argb_uint32("local_color_d"),
    Float("local_scalar_a"),
    Float("local_scalar_b"),
    Float("local_scalar_c"),
    Float("local_scalar_d"),
    SEnum16("output_color_a", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_b", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_c", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_d", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_e", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_color_f", *chdt_hud_widget_render_data_output_color_a),
    SEnum16("output_scalar_a", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_b", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_c", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_d", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_e", *chdt_hud_widget_render_data_output_scalar_a),
    SEnum16("output_scalar_f", *chdt_hud_widget_render_data_output_scalar_a),
    ENDIAN=">", SIZE=64
    )


chdt_hud_widget_text_widget = Struct("text_widget", 
    h3_string_id("name"),
    SEnum16("special_hud_type", *chdt_hud_widget_special_hud_type),
    UInt8("unknown_0", VISIBLE=False),
    UInt8("unknown_1", VISIBLE=False),
    h3_reflexive("state_data", chdt_hud_widget_text_widget_state_data),
    h3_reflexive("placement_data", chdt_hud_widget_text_widget_placement_data),
    h3_reflexive("animation_data", chdt_hud_widget_text_widget_animation_data),
    h3_reflexive("render_data", chdt_hud_widget_text_widget_render_data),
    SInt32("widget_index"),
    Bool16("flags", 
        "string_is_a_number",
        "force_2_digit",
        "force_3_digit",
        "prefix_0",
        "m_suffix",
        "hundredths_decimal",
        "thousandths_decimal",
        "hundred_thousandths_decimal",
        "only_a_number",
        "x_suffix",
        "in_brackets",
        "time_format_s_ms",
        "time_format_h_m_s",
        "money_format",
        "prefix_1",
        ),
    SEnum16("font", *chdt_hud_widget_text_widget_font),
    h3_string_id("string"),
    ENDIAN=">", SIZE=68
    )


chdt_hud_widget = Struct("hud_widget", 
    h3_string_id("name"),
    SEnum16("special_hud_type", *chdt_hud_widget_special_hud_type),
    UInt8("unknown_0", VISIBLE=False),
    UInt8("unknown_1", VISIBLE=False),
    h3_reflexive("state_data", chdt_hud_widget_state_data),
    h3_reflexive("placement_data", chdt_hud_widget_placement_data),
    h3_reflexive("animation_data", chdt_hud_widget_animation_data),
    h3_reflexive("render_data", chdt_hud_widget_render_data),
    h3_reflexive("bitmap_widgets", chdt_hud_widget_bitmap_widget),
    h3_reflexive("text_widgets", chdt_hud_widget_text_widget),
    ENDIAN=">", SIZE=80
    )


chdt_body = Struct("tagdata", 
    h3_reflexive("hud_widgets", chdt_hud_widget),
    SInt32("low_clip_cutoff"),
    SInt32("low_ammo_cutoff"),
    SInt32("age_cutoff"),
    ENDIAN=">", SIZE=24
    )


def get():
    return chdt_def

chdt_def = TagDef("chdt",
    h3_blam_header('chdt'),
    chdt_body,

    ext=".%s" % h3_tag_class_fcc_to_ext["chdt"], endian=">", tag_cls=H3Tag
    )