# Extracts necessary assets/data from a given Mother ROM

from bitarray import bitarray

rom_path = 'Mother (Japan).nes'
rom_bits = bitarray()

with open(rom_path, 'rb') as f:
    rom_bits.fromfile(f)

print(len(rom_bits))
