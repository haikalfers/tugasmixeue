#Implementasi Program Python untuk aplikasi pemesanan Menu Miexue dengan Linked List
class Node:
  def __init__(self, menu, price):
    self.menu = menu
    self.price = price
    self.next = None

class Orders:
    def __init__(self, data=None):
        self.head = Node(data) if data else None

    def tambah_pesanan(self, menu, harga):
        new_node = Node(menu, harga)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
