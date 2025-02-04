import os

from binilla.handler import Handler
from reclaimer.misc.defs import __all__ as all_def_names
from supyr_struct.defs.constants import PATHDIV


class MiscHaloLoader(Handler):
    frozen_imp_paths = all_def_names
    default_defs_path = "reclaimer.misc.defs"

    tagsdir = "%s%stags%s" % (os.path.abspath(os.curdir), PATHDIV, PATHDIV)

    def get_def_id(self, filepath):
        '''docstring'''
        def_id = Handler.get_def_id(self, filepath)

        if def_id == 'xbox_gametype' and 'pc_gametype' in self.id_ext_map:
            return 'pc_gametype'
        return def_id
