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

# While they aren't dictionaries, nodes can be thought of this way.
# You can think of it as a list of nested dictionaries

# head = {
#     "value": 4,
#     "next": {
#         "value": 8,
#         "next": {
#             "value": 20,
#             "next": {
#                 "value": 9,
#                 "next": None
#             }
#         }
#     }
# }

# print(head['next']['next']['next']['value'])

# This is to be referenced by LinkedList in order to create nodes in each method
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Create new node
    def __init__(self, value):

        # variable to be used in this method
        # passes value to Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        # in case list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # in case list is not empty
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# calls LinkedList class and passes value of 4
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

# print(my_linked_list.head.value)

    # create new Node, then add node to end
    # def append(self, value):

    # create new Node, add Node to beginning
    # def prepend(self, value):

    # create new Node, insert Node
    # def insert(self, index, value):
        