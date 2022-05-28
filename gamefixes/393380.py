""" Game fix for Squad
"""
#pylint: disable=C0103
import os
import stat

from protonfixes import util


def main():
    """ Do the Squad tutorial fix at https://squadfm.org/#installation-linux-only
    """
    URL = "https://github.com/ValveSoftware/Proton/files/4839724/easyanticheat_wine_x64.tar.gz"
    extract_path = os.path.join(
        util.protonprefix(),
        '..'
    )
    eac_path = os.path.join(
        util.protonprefix(),
        'drive_c',
        'users',
        'steamuser',
        'AppData',
        'Roaming',
        'EasyAntiCheat',
        '55'
    )
    temp_path = os.path.join(
        util.protonprefix(),
        'drive_c',
        'users',
        'steamuser',
        'Temp'
    )

    util.install_all_from_tgz(URL, extract_path)
    
    # Set Paths to readonly
    os.chmod(os.path.join(eac_path, "easyanticheat_wine_x64.eac"), stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(os.path.join(eac_path, "easyanticheat_wine_x64.eac.metadata"), stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    os.chmod(eac_path, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    os.chmod(temp_path, stat.S_IRUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
