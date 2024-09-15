class Node:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node


class LinkedList:

  def __init__(self, head = None):
    self.head = head

  def append(self, node):
    # Add element to the beginning of the list if the list is empty
    if self.head == None:
        self.head = node
        return
    # Otherwise, traverse the list to find the last node
    last_node = self.head
    while last_node.next_node:
      last_node = last_node.next_node
    # and add the node to the end
    last_node.next_node = node

  def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_node
        return " -> ".join(nodes)

list = LinkedList()

list.append(Node("Bulldog"))
print(list)
# Bulldog
list.append(Node("Chihuahua"))
print(list)
# Bulldog -> Chihuahua
list.append(Node("German Shepard"))
print(list)
# Bulldog -> Chihuahua -> German Shepard    