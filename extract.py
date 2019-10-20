# Extracts necessary assets/data from a given Mother ROM

from bitarray import bitarray

rom_path = 'Mother (Japan).nes'
rom_bits = bitarray()

with open(rom_path, 'rb') as f:
    rom_bits.fromfile(f)

rom_map = {
    'map_data': {
        'starts': 0x2010,
        'ends':   0x2000F
    }
}

def getByteAt(loc, bits):
    loc_decimal = int(loc)
    index = loc_decimal * 8

    return bits[index:index + 8]

print(getByteAt(rom_map['map_data']['starts'], rom_bits))
