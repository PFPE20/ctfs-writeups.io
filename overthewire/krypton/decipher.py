#!/usr/bin/env python3

import string

encrypted_string = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
given = "A" * len(encrypted_string)

to_decipher = "PNUKLYLWRQKGKBE"

positions = list()

# Primero encontremos el offset

for i in range(0, len(encrypted_string)):
    positions.append(ord(encrypted_string[i]) - ord(given[i]))

key = ""

for i in range(0, len(to_decipher)):
    char = ord(to_decipher[i])
    res = char - positions[i]
    if (chr(res) not in string.ascii_letters):
        res = char - positions[i] + 26

    key += chr(res)

print(key)
