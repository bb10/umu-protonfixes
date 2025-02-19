"""Atelier Ryza 3: Alchemist of the End & the Secret Key
Missing voices/sounds in cutscenes
Requires disabling the gstreamer protonaudioconverterbin plugin to get full audio in cutscenes
"""

from protonfixes import util


def main() -> None:
    util.disable_protonmediaconverter()
    
    """Grants bonus content to players with save data for Atelier Ryza: Ever Darkness & the Secret Hideout"""
    util.import_saves_folder(1121560, 'Documents/KoeiTecmo/Atelier Ryza')

    """Grants bonus content to players with save data for Atelier Ryza 2: Lost Legends & the Secret Fairy"""
    util.import_saves_folder(1257290, 'Documents/KoeiTecmo/Atelier Ryza 2')

    """Grants bonus content to players with save data for Atelier Sophie 2: The Alchemist of the Mysterious Dream"""
    util.import_saves_folder(1621310, 'Documents/KoeiTecmo/Atelier Sophie 2')
