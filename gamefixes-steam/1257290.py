"""Atelier Ryza 2: Lost Legends & the Secret Fairy
Missing voices/sounds in cutscenes
Requires disabling the gstreamer protonaudioconverterbin plugin to get full audio in cutscenes
"""

from protonfixes import util


def main() -> None:
    util.disable_protonmediaconverter()
    
    """Grants bonus content to players with save data for Atelier Ryza: Ever Darkness & the Secret Hideout"""
    util.import_saves_folder(1121560, 'Documents/KoeiTecmo/Atelier Ryza')
