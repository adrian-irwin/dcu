#
#   Return an empty list to get your list of binary numbers.
#
#   Then return a list of strings representing the binary numbers in the correct positions
#

# Your list is:
# 	'0011',
# 	'1100',
# 	'0001',
# 	'1010',
# 	'1111',
# 	'0000',

def sol():
    return ["1100", "1010", "0000", "0011", "0001", "1111"]

# pass1: 1100, 1010, 0000, 0011, 0001, 1111
# pass2: 1100, 0000, 0001, 1010, 0011, 1111
# pass3: 0000, 0001, 1010, 0011, 1100, 1111
# pass4: 0000, 0001, 0011, 1010, 1100, 1111