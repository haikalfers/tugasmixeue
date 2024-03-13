#Implementasi Program Python untuk aplikasi pemesanan Menu Miexue dengan Linked List
class Node:
  def __init__(self, menu, price):
    self.menu = menu
    self.price = price
    self.next = None
