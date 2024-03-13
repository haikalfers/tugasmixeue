#Implementasi Program Python untuk aplikasi pemesanan Menu Miexue dengan Linked List
class Node:
  def __init__(self, menu, price):
    self.menu = menu
    self.price = price
    self.next = None

class Orders:
    def __init__(self, data=None):
        self.head = Node(data) if data else None
