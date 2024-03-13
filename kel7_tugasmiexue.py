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

     def tampilkan_pesanan(self):
        current = self.head
        count = 1
        while current:
            print (f"{count}. {current.menu}(pcs)- {current.price} rupiah")
            current = current.next
            count += 1

      def total_harga(self):
        harga_akhir = 0
        current = self.head
        while current:
            harga_akhir += current.price
            current = current.next
        return harga_akhir

