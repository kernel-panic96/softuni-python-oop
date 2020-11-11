from project import *


heroes = [
    Hero('hero', 1),
    Elf('elf', 1),
    Wizard('wizard', 1),
    Knight('knight', 1),
    MuseElf('melf', 1),
    DarkWizard('dw', 1),
    DarkKnight('dk', 1),
    SoulMaster('sm', 1),
    BladeKnight('bk', 1),
]

for h in heroes:
    print(h.__class__.__name__, h, h.__dict__)