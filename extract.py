# Extracts necessary assets/data from a given Mother ROM

from bitarray import bitarray

rom_path = 'Mother (Japan).nes'
rom_bits = bitarray()

with open(rom_path, 'rb') as f:
    rom_bits.fromfile(f)

rom_map = {
    'map_data': {
        'starts': 0x2010,  # Inclusive
        'ends':   0x20010, # Exclusive
        'bank0': { # Bank 0 contains no map data, only tileset data
            'starts': 0x2010,
            'ends':   0x4010
        },
        'bank1': {
            'starts': 0x4010,
            'ends':   0x8010
        }
    }
}

map_bank_layout = {
    'map': {
        'starts': 0x0,
        'length': 0x2000
    }
}

def getByteAt(loc, bits):
    loc_decimal = int(loc)
    index = loc_decimal * 8

    return bits[index:index + 8]

# Convert the read binary data into a map of our own format
map_data = []
map_width = 256

for i in range(rom_map['map_data']['bank1']['starts'] + map_bank_layout['map']['starts'], rom_map['map_data']['bank1']['starts'] + map_bank_layout['map']['length']):
    byte = getByteAt(i, rom_bits)

    map_data.append({
        'tile64': byte[0:6],
        'tileset2': byte[6],
        'event_flag': byte[7]
    })

def printMapAsASCII(map_data):
    for i in range(0, len(map_data)):
        if i >= map_width and i % map_width == 0:
            print('')

        as_ord = ord(map_data[i]['tile64'].tobytes().decode())
        print(chr((as_ord % 26) + 65), end='')

    print('')

printMapAsASCII(map_data)
