class Node:
  def __init__(self, data, next_node = None, prev_node = None):
    self.data = data
    self.next_node = next_node
    self.prev_node = prev_node

class DoublyLinkedList:

  def __init__(self, head = None, tail = None):
    self.head = head


  def delete_tail(self):
      if self.head == self.tail:
        self.head = None
        self.tail = None
      # traverse the entire list to find the second-to-last node (prev)
      else:
        # access the second-to-last node (self.tail.prev_node)
        prev = self.tail.prev_node
        # update the tail and next_node pointers
        # 1 <-> 2 <-> 3

        prev.next_node = None
        self.tail = prev
        # 1 <-> 2

    
  def append(self, node):
    if self.head == None:
        self.head = node
        self.tail = node
        return
    node.prev_node = self.tail
    self.tail.next_node = node
    self.tail = node    

  def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next_node
        return " <-> ".join(nodes)

# Example usage:
dll = DoublyLinkedList()
dll.append(Node("1"))
dll.append(Node("2"))
dll.append(Node("3"))
dll.append(Node("4"))

print("Initial list:", dll)  # Output: Initial list: 1 <-> 2 <-> 3

dll.delete_tail()
print("After deleting tail:", dll)  # Output: After deleting tail: 1 <-> 2

dll.delete_tail()
print("After deleting tail:", dll)  # Output: After deleting tail: 1

dll.delete_tail()
print("After deleting tail:", dll)  # Output: After deleting tail: List is empty  