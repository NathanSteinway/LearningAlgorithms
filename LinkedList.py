# Python List        

#  _________
# |11|7|23|3|
# | 0|1| 2|3|
# -----------

# Linked List
'__________________'
'|7 |    |    | 3  |'
'|  |    | 23 |    |'
'|  | 11 |    |    |'
'|__|____|____|____|'

# Key differences

# Python Lists:                    |    Linked Lists:
# 1) Contiguously stored in mem    |    1) Not stored contiguously in mem
#     Lists require a BLOCK of mem |        Linked Lists can make use of fragments of memory
# 2) May access indexes O(1)       |    2) May access indexes O(n)
#     Block of mem isn't ambiguous |        Must traverse the Linked List because its data is not all in one place
# 3) Each index mapped to address


# Key Features of Linked Lists
# 1) Head points to first node in list
# 2) Tail points to last node in list
# 3) each node points to the next
# 4) last node points to None


#  HEAD      TAIL       
#   |         |
#   0 -> 1 -> 2 -> None
