# Homework 1. ToDo List Application

# Task class
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "incomplete"  # default holat

    def mark_complete(self):
        self.status = "complete"

    def __str__(self):
        return f"{self.title} | {self.description} | {self.due_date} | {self.status}"


# ToDoList class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"'{title}' bajarildi deb belgilandi.")
                return
        print(f"'{title}' topilmadi.")

    def list_all_tasks(self):
        if not self.tasks:
            print("Hech qanday vazifa yo'q.")
        else:
            print("\nBarcha vazifalar:")
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "incomplete"]
        if not incomplete:
            print("🎉 Tugallanmagan vazifa yo'q!")
        else:
            print("\nTugallanmagan vazifalar:")
            for task in incomplete:
                print(task)


# Asosiy dastur (CLI)
def main():
    todo = ToDoList()

    while True:
        print("\n===== ToDo List Menyu =====")
        print("1. Vazifa qo'shish")
        print("2. Vazifani bajarilgan deb belgilash")
        print("3. Barcha vazifalarni ko'rish")
        print("4. Faqat tugallanmagan vazifalarni ko'rish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            title = input("Vazifa nomi: ")
            description = input("Tavsifi: ")
            due_date = input("Muddati (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Vazifa qo'shildi.")

        elif choice == "2":
            title = input("Bajarilgan vazifa nomini kiriting: ")
            todo.mark_task_complete(title)

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("Dastur tugadi.")
            break

        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()

# Homework 2. Simple Blog System

# Post class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} | {self.author}\n{self.content}"


# Blog class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("Hali hech qanday post yo'q.")
        else:
            print("\nBarcha postlar:")
            for post in self.posts:
                print(post, "\n---")

    def display_posts_by_author(self, author):
        found = [post for post in self.posts if post.author == author]
        if not found:
            print(f"'{author}' tomonidan yozilgan post topilmadi.")
        else:
            print(f"\n{author} tomonidan yozilgan postlar:")
            for post in found:
                print(post, "\n---")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"🗑'{title}' posti o'chirildi.")
                return
        print(f"'{title}' nomli post topilmadi.")

    def edit_post(self, title, new_title, new_content):
        for post in self.posts:
            if post.title == title:
                post.title = new_title
                post.content = new_content
                print(f"'{title}' posti yangilandi.")
                return
        print(f"'{title}' nomli post topilmadi.")

    def display_latest_posts(self, n):
        if not self.posts:
            print("Hech qanday post yo'q.")
        else:
            print(f"\nOxirgi {n} ta post:")
            for post in self.posts[-n:]:
                print(post, "\n---")


# Asosiy dastur (CLI)
def main():
    blog = Blog()

    while True:
        print("\n===== Blog Menyu =====")
        print("1. Post qo'shish")
        print("2. Barcha postlarni ko'rish")
        print("3. Muallif bo'yicha postlarni ko'rish")
        print("4. Postni o'chirish")
        print("5. Postni tahrirlash")
        print("6. Oxirgi postlarni ko'rish")
        print("7. Chiqish")

        choice = input("Tanlang (1-7): ")

        if choice == "1":
            title = input("Post nomi: ")
            content = input("Post matni: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post qo'shildi.")

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Muallif ismi: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            title = input("O'chiriladigan post nomi: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Tahrir qilinadigan post nomi: ")
            new_title = input("Yangi nom: ")
            new_content = input("Yangi matn: ")
            blog.edit_post(title, new_title, new_content)

        elif choice == "6":
            n = int(input("Nechta oxirgi postni ko'rasiz? "))
            blog.display_latest_posts(n)

        elif choice == "7":
            print("Dastur tugadi.")
            break

        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()

# Homework 3. Simple Banking System

# Account class
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False  # overdraft

    def __str__(self):
        return f"Account: {self.account_number} | 👤 Holder: {self.holder_name} | Balance: {self.balance}"


# Bank class
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"Balans: {acc.balance}")
        else:
            print("Account topilmadi.")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.deposit(amount)
            print(f"{amount} so'm qo'shildi. Yangi balans: {acc.balance}")
        else:
            print("Account topilmadi.")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            if acc.withdraw(amount):
                print(f"{amount} so'm yechildi. Yangi balans: {acc.balance}")
            else:
                print("Mablag' yetarli emas (Overdraft).")
        else:
            print("Account topilmadi.")

    def transfer(self, sender_acc, receiver_acc, amount):
        sender = self.find_account(sender_acc)
        receiver = self.find_account(receiver_acc)
        if sender and receiver:
            if sender.withdraw(amount):
                receiver.deposit(amount)
                print(f"{amount} so'm {sender_acc} dan {receiver_acc} ga o'tkazildi.")
            else:
                print("⚠Pul o'tkazish uchun mablag' yetarli emas.")
        else:
            print("Account(lar) topilmadi.")

    def display_account_details(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(acc)
        else:
            print("Account topilmadi.")


# Asosiy dastur (CLI)
def main():
    bank = Bank()

    while True:
        print("\n===== Bank Menyu =====")
        print("1. Account qo'shish")
        print("2. Balansni ko'rish")
        print("3. Pul qo'yish (deposit)")
        print("4. Pul yechish (withdraw)")
        print("5. Pul o'tkazish (transfer)")
        print("6. Account ma'lumotlarini ko'rish")
        print("7. Chiqish")

        choice = input("Tanlang (1-7): ")

        if choice == "1":
            acc_num = input("Account raqami: ")
            name = input("Hisob egasi ismi: ")
            balance = float(input("Boshlang'ich balans: "))
            account = Account(acc_num, name, balance)
            bank.add_account(account)
            print("Account yaratildi.")

        elif choice == "2":
            acc_num = input("Account raqami: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Account raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.deposit(acc_num, amount)

        elif choice == "4":
            acc_num = input("Account raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.withdraw(acc_num, amount)

        elif choice == "5":
            sender = input("Yuboruvchi account raqami: ")
            receiver = input("Qabul qiluvchi account raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.transfer(sender, receiver, amount)

        elif choice == "6":
            acc_num = input("Account raqami: ")
            bank.display_account_details(acc_num)

        elif choice == "7":
            print("Dastur tugadi.")
            break

        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()
