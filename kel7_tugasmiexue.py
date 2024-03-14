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

#ListMenu
daftar_menu = {
    "(1) Mixeue Ice Cream"  : 5000,
    "(2) Boba Shake"        : 16000,
    "(3) Mi Sundae"         : 14000,
    "(4) Mi Ganas"          : 11000,
    "(5) Creamy Mango Boba" : 22000
}
MENU = list(daftar_menu.items())
menu_list = Orders ()

def tampilan_menu():
    print("daftar menu")
    for nama_menu, harga in daftar_menu.items():
        print(f"{nama_menu} - {harga} Rupiah")

def tampilan_pesanan():
    print("pesanan anda : ")
    menu_list.tampilkan_pesanan()
    
def menghitung_harga_akhir():
    total = menu_list.total_harga()
    print(f"Total biaya yang harus dibayarkan adalah {total} rupiah\nTerima kasih sudah berbelanja di Miexue")

tampilan_menu()
# Penggunaan program
while True :
    pilihan = input("silahkan piih menu yang anda inginkan... (ketikan 'done' jika sudah selesai memesan) : ")
    if pilihan.lower() == 'done' :
        break
    
    pilihan =int(pilihan) - 1
    menu_list.tambah_pesanan(MENU[pilihan][0], MENU[pilihan][1])

tampilan_pesanan()
menghitung_harga_akhir()



