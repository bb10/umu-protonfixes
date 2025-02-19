"""Atelier Sophie 2: The Alchemist of the Mysterious Dream"""

def main() -> None:
    """Grants bonus content to players with save data for BLUE REFLECTION: Second Light (only if you own pre-order editions of both games)"""
    util.import_saves_folder(1423600, 'Documents/KoeiTecmo/BLUE REFLECTION Second Light')

    """Grants bonus content to players with save data for Atelier Ryza 2: Lost Legends & the Secret Fairy"""
    util.import_saves_folder(1257290, 'Documents/KoeiTecmo/Atelier Ryza 2')

    """Grants bonus content to players with save data for Atelier Sophie: The Alchemist of the Mysterious Book DX"""
    util.import_saves_folder(1502970, 'Documents/KoeiTecmo/Atelier Sophie DX/SAVEDATA')

    """Grants bonus content to players with save data for Atelier Firis: The Alchemist and the Mysterious Journey DX"""
    util.import_saves_folder(1502980, 'Documents/KoeiTecmo/Atelier Firis DX/SAVEDATA')

    """Grants bonus content to players with save data for Atelier Lydie & Suelle: The Alchemists and the Mysterious Paintings DX"""
    util.import_saves_folder(1502990, 'Documents/KoeiTecmo/Atelier Lydie and Suelle DX/SAVEDATA')
