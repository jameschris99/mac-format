# MAC address formatting tool for searches in switches, etc.

import sys
import re

mac_input =  sys.argv[1]

mac_chars_list = []
chars_remove = [':', '.', '-' ]

for char in mac_input:
    if char in chars_remove:
        continue
    else:
        mac_chars_list.append(char)

mac_string = (''.join(mac_chars_list))

if len(mac_string) != 12:
    print ('Error: {} is not a valid MAC address'.format(mac_input))
    sys.exit()

mac_cisco = []
a = 0
b = 4
for n in range(1,4):
    hextet = (mac_string[a:b])
    a = a + 4
    b = b + 4
    mac_cisco.append(hextet)

print ('.'.join(mac_cisco))

if '-u' in sys.argv:
    print (('.'.join(mac_cisco)).upper())

mac_colon_2 = []
a = 0
b = 2
for n in range(1,7):
    hextet = (mac_string[a:b])
    a = a + 2
    b = b + 2
    mac_colon_2.append(hextet)

print (':'.join(mac_colon_2))

if '-u' in sys.argv:
    print ((':'.join(mac_colon_2)).upper())

mac_hyphen_2 = []
a = 0
b = 2
for n in range(1,7):
    hextet = (mac_string[a:b])
    a = a + 2
    b = b + 2
    mac_hyphen_2.append(hextet)

print ('-'.join(mac_hyphen_2))

if '-u' in sys.argv:
    print (('-'.join(mac_hyphen_2)).upper())