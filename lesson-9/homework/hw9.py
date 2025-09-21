## 1. Circle Class

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
# r = float(input("Doiraning radiusini kiriting: "))
#
# c = Circle(r)
# print("Maydon (area):", c.area())
# print("Perimetr (circumference):", c.perimeter())

## 2. Person Class

# from datetime import datetime
#
# class Person:
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = datetime.strptime(dob, "%Y-%m-%d")
#
#     def get_age(self):
#         today = datetime.today()
#         age = today.year - self.dob.year
#         if (today.month, today.day) < (self.dob.month, self.dob.day):
#             age -= 1
#         return age
#
# p = Person("Ali", "Uzbekistan", "2000-05-15")
# print("Ism:", p.name)
# print("Davlat:", p.country)
# print("Tug‘ilgan sana:", p.dob.date())
# print("Yosh:", p.get_age())

## 3. Calculator Class

# class Calculator:
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         if b == 0:
#             return "Xatolik: 0 ga bo‘lish mumkin emas!"
#         return a / b
#
# calc = Calculator()
#
# print(f"Qo‘shish: {calc.add(10, 5)}")
# print("Ayirish:", calc.subtract(10, 5))
# print("Ko‘paytirish:", calc.multiply(10, 5))
# print("Bo‘lish:", calc.divide(10, 5))
# print("0 ga bo‘lish:", calc.divide(10, 0))

## 4. Shape and Subclasses

# import math
#
# class Shape:
#     def area(self):
#         raise NotImplementedError("Area metodi hali yozilmagan")
#
#     def perimeter(self):
#         raise NotImplementedError("Perimeter metodi hali yozilmagan")
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimeter(self):
#         return 4 * self.side
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = self.perimeter() / 2
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
# circle = Circle(5)
# square = Square(4)
# triangle = Triangle(3, 4, 5)
#
# print("Doira: Yuza =", circle.area(), ", Perimetr =", circle.perimeter())
# print("Kvadrat: Yuza =", square.area(), ", Perimetr =", square.perimeter())
# print("Uchburchak: Yuza =", triangle.area(), ", Perimetr =", triangle.perimeter())

## 5. Binary Search Tree Class

# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)
#
#     def _insert(self, current_node, key):
#         if key < current_node.key:
#             if current_node.left is None:
#                 current_node.left = Node(key)
#             else:
#                 self._insert(current_node.left, key)
#         elif key > current_node.key:
#             if current_node.right is None:
#                 current_node.right = Node(key)
#             else:
#                 self._insert(current_node.right, key)
#         else:
#             pass
#
#     # Search metodi
#     def search(self, key):
#         return self._search(self.root, key)
#
#     def _search(self, current_node, key):
#         if current_node is None:
#             return False
#         if key == current_node.key:
#             return True
#         elif key < current_node.key:
#             return self._search(current_node.left, key)
#         else:
#             return self._search(current_node.right, key)
#
#     def inorder(self):
#         elements = []
#         self._inorder(self.root, elements)
#         return elements
#
#     def _inorder(self, node, elements):
#         if node:
#             self._inorder(node.left, elements)
#             elements.append(node.key)
#             self._inorder(node.right, elements)
#
#
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(80)
#
# print("Inorder Traversal:", bst.inorder())
# print("Search 40:", bst.search(40))
# print("Search 25:", bst.search(25))

## 6. Stack Data Structure

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return "Stack bo‘sh!"
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return "Stack bo‘sh!"
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def size(self):
#         return len(self.items)
#
#
# stack = Stack()
#
# stack.push(10)
# stack.push(20)
# stack.push(30)
#
# print("Stack hajmi:", stack.size())
# print("Oxirgi element:", stack.peek())
#
# print("Pop qilingan:", stack.pop())
# print("Pop qilingan:", stack.pop())
# print("Stack bo‘shmi?:", stack.is_empty())
#
# print("Pop qilingan:", stack.pop())
# print("Stack bo‘shmi?:", stack.is_empty())

## 7. Linked List Data Structure

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#
#     def delete(self, data):
#         current = self.head
#
#         if current and current.data == data:
#             self.head = current.next
#             current = None
#             return
#
#         prev = None
#         while current and current.data != data:
#             prev = current
#             current = current.next
#
#         if current is None:
#             print("Element topilmadi!")
#             return
#
#         prev.next = current.next
#         current = None
#
#     def display(self):
#         elements = []
#         current = self.head
#         while current:
#             elements.append(current.data)
#             current = current.next
#         print("Linked List:", elements)
#
#
# ll = LinkedList()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.insert(40)
#
# ll.display()
#
# ll.delete(20)
# ll.display()
#
# ll.delete(10)
# ll.display()
#
# ll.delete(50)

## 8. Shopping Cart Class

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#
#     # Mahsulot qo‘shish
#     def add_item(self, name, price, quantity=1):
#         if name in self.items:
#             old_price, old_quantity = self.items[name]
#             self.items[name] = (price, old_quantity + quantity)
#         else:
#             self.items[name] = (price, quantity)
#
#     # Mahsulot o‘chirish
#     def remove_item(self, name):
#         if name in self.items:
#             del self.items[name]
#         else:
#             print(f"{name} savatda yo‘q!")
#
#     # Umumiy narxni hisoblash
#     def total_price(self):
#         total = 0
#         for price, quantity in self.items.values():
#             total += price * quantity
#         return total
#
#     # Savatni ko‘rsatish
#     def display_cart(self):
#         if not self.items:
#             print("Savat bo‘sh!")
#         else:
#             print("Savat tarkibi:")
#             for name, (price, quantity) in self.items.items():
#                 print(f"- {name}: {quantity} dona, narx: {price} so‘m (jami: {price * quantity} so‘m)")
#             print("Umumiy narx:", self.total_price(), "so‘m")
#
#
# cart = ShoppingCart()
# cart.add_item("Olma", 5000, 3)
# cart.add_item("Banan", 10000, 2)
# cart.add_item("Olma", 5000, 1)
#
# cart.display_cart()
#
# cart.remove_item("Banan")
# cart.display_cart()
#
# cart.remove_item("Gilos")

## 9. Stack with Display

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     # Element qo‘shish
#     def push(self, item):
#         self.items.append(item)
#         print(f"{item} stackka qo‘shildi")
#
#     # Elementni chiqarish
#     def pop(self):
#         if not self.is_empty():
#             removed = self.items.pop()
#             print(f"{removed} stackdan o‘chirildi")
#             return removed
#         else:
#             print("Stack bo‘sh! Pop qilish mumkin emas.")
#
#     # Stack elementlarini ko‘rsatish
#     def display(self):
#         if not self.is_empty():
#             print("Stack tarkibi (tepadan pastga):")
#             for item in reversed(self.items):
#                 print(item)
#         else:
#             print("Stack bo‘sh!")
#
#     # Stack bo‘shligini tekshirish
#     def is_empty(self):
#         return len(self.items) == 0
#
#
# # Test qilish
# stack = Stack()
#
# stack.push(10)
# stack.push(20)
# stack.push(30)
#
# stack.display()   # 30, 20, 10
#
# stack.pop()       # 30 ni o‘chiradi
# stack.display()   # 20, 10

## 10. Queue Data Structure

# class Queue:
#     def __init__(self):
#         self.items = []
#
#     # element qo‘shish (oxiriga)
#     def enqueue(self, item):
#         self.items.append(item)
#         print(f"{item} navbatga qo‘shildi")
#
#     # elementni olish (boshlanishidan)
#     def dequeue(self):
#         if not self.is_empty():
#             removed = self.items.pop(0)
#             print(f"{removed} navbatdan olindi")
#             return removed
#         else:
#             print("Navbat bo‘sh! Dequeue qilish mumkin emas.")
#
#     # navbatni ko‘rsatish
#     def display(self):
#         if not self.is_empty():
#             print("Navbat tarkibi (boshi → oxiri):", self.items)
#         else:
#             print("Navbat bo‘sh!")
#
#     # navbat bo‘shligini tekshirish
#     def is_empty(self):
#         return len(self.items) == 0
#
#
# # Test qilish
# queue = Queue()
#
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
#
# queue.display()   # [10, 20, 30]
#
# queue.dequeue()   # 10 ni olib tashlaydi
# queue.display()   # [20, 30]

## 11. Bank Class

class Bank:
    def __init__(self):
        self.accounts = {}  # {account_number: {"name": ..., "balance": ...}}
        self.next_account_number = 1001  # avtomatik hisob raqam berish

    # Yangi hisob yaratish
    def create_account(self, customer_name, initial_balance=0):
        account_number = self.next_account_number
        self.accounts[account_number] = {"name": customer_name, "balance": initial_balance}
        self.next_account_number += 1
        print(f"Hisob yaratildi! Mijoz: {customer_name}, Hisob raqami: {account_number}, Balans: {initial_balance}")
        return account_number

    # Pul qo‘yish
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"{amount} so‘m hisobga qo‘yildi. Yangi balans: {self.accounts[account_number]['balance']}")
        else:
            print("Hisob topilmadi!")

    # Pul yechish
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"{amount} so‘m yechildi. Yangi balans: {self.accounts[account_number]['balance']}")
            else:
                print("Balans yetarli emas!")
        else:
            print("Hisob topilmadi!")

    # Pul o‘tkazish
    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc]["balance"] >= amount:
                self.accounts[from_acc]["balance"] -= amount
                self.accounts[to_acc]["balance"] += amount
                print(f"{amount} so‘m {from_acc} dan {to_acc} ga o‘tkazildi.")
            else:
                print("Balans yetarli emas!")
        else:
            print("Hisob(lar) topilmadi!")

    # Hisoblarni ko‘rsatish
    def display_accounts(self):
        if not self.accounts:
            print("Bankda hali hisob yo‘q.")
        else:
            print("Barcha hisoblar:")
            for acc, info in self.accounts.items():
                print(f"Hisob: {acc}, Mijoz: {info['name']}, Balans: {info['balance']}")

bank = Bank()

# Hisob yaratish
acc1 = bank.create_account("Ali", 50000)
acc2 = bank.create_account("Vali", 30000)

# Pul qo‘yish va olish
bank.deposit(acc1, 20000)
bank.withdraw(acc2, 10000)

# Pul o‘tkazish
bank.transfer(acc1, acc2, 15000)

# Hisoblarni ko‘rsatish
bank.display_accounts()
