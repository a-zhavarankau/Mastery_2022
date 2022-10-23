class Store:
    def __init__(self, name: str):
        self.name = name
        self._accounts = []
        self._series = []
        self._books = []

    def add_user(self, user):
        self._accounts.append(user)

    def show_accounts(self):
        print(f'Store "{self.name}" has the next accounts:')
        Store.print_if_exists(self._accounts, "mr.", "name")

    def add_series(self, book):
        self._series.append(book)

    def show_series(self):
        print(f'Store "{self.name}" has the next series:')
        Store.print_if_exists(self._series, "*")

    def add_book(self, book):
        self._books.append(book)
        book.store = self
        print(f'[INFO] Book "{book.title}" added the store "{self.name}"')

    def delete_book(self, book):
        self._books.remove(book)

    def show_books(self):
        print(f'List of books in the store "{self.name}":')
        Store.print_if_exists(self._books, "-", "title")

    def check_book_in_store(self, book):
        if book in self._books:
            return True
        return False

    # Method is used only for internal needs
    @staticmethod
    def print_if_exists(place, sign: str, attr=None):
        if place:
            for item in place:
                str_ = (f"  {sign} {getattr(item,attr)}"
                        if not isinstance(item, str) else f" {sign} {item}")
                print(str_)
        else:
            print(" -Empty-")


class User:
    def __init__(self, name: str, surname: str, birth: str, email: str, phone: int):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.email = email
        self.phone = phone
        self.order_list: list = []
        self.prev_order_list: list = []
        self._cart: list = []
        self._orders_count = 0

    def add_to_cart(self, store, book):
        if store.check_book_in_store(book):
            self._cart.append(book)
            print(f"[INFO] \"{book.title}\" from the store \"{store.name}\" "
                  f"added to the {self.name}'s cart")
        else:
            print(f"[INFO] No book \"{book.title}\" in the store \"{store.name}\"")

    def make_order(self, address: str):
        if self.order_list:
            print("You can't make another order. Please make the payment.")
            return
        if self._cart:
            self._orders_count += 1
            order = Order(self._orders_count, self._cart, address)
            self.order_list.append(order)
        else:
            print(f"{self.name}'s cart is empty")

    def find_order(self, num: int):
        for order in (self.order_list or self.prev_order_list):
            if order.order_num == num:
                return order
        return False

    def show_order(self, num: int):
        required_order = self.find_order(num)
        if required_order is not False:
            print(f"Order number: {required_order.order_num},\n\t"
                  f"order_list: {[item.title for item in required_order.books]},\n\t"
                  f"total_amount: {required_order.total_amount},\n\t"
                  f"delivery address: {required_order.delivery_addr}")
            return
        print(f"Order {num} not found")

    def pay_order(self, num: int):
        required_order = self.find_order(num)
        if required_order is not False:
            for book in required_order.books:
                book.store.delete_book(book)
            required_order.books = self._cart[:]
            self.prev_order_list.append(required_order)
            self._cart.clear()
            self.order_list.remove(required_order)
            print(f"Your payment accepted. Wait for your books at: "
                  f"{required_order.delivery_addr}")
            return
        print(f"Order {num} not found")

    def show_curr_order_list(self):
        print(f"{self.name} has current orders:")
        Store.print_if_exists(self.order_list, "*", "order_num")

    def show_prev_order_list(self):
        print(f"{self.name}'s previous orders are:")
        Store.print_if_exists(self.prev_order_list, "*", "order_num")


class Book:
    def __init__(self, title: str, num_pages: int, publish_year: int, author: str):
        self.title = title
        self.num_pages = num_pages
        self.publish_year = publish_year
        self.author = author


class Order:
    def __init__(self, order_num: int, cart: list, delivery_addr: str):
        self.order_num = order_num
        self.books = cart
        self.total_amount = len(self.books)
        self.delivery_addr = delivery_addr


if __name__ == "__main__":
    store1 = Store("Knigarnya")

    maugli = Book("Maugli", 200, 1995, "R.Kipling")
    generation_p = Book("Generation P", 343, 2010, "V.Pelevin")
    hobbit = Book("Hobbit", 405, 2008, "J.R.R.Tolkien")

    store1.add_book(maugli)
    store1.add_book(hobbit)
    store1.add_book(generation_p)

    alex = User("Alex", "Alexandrov", "01.02.2000", "alex@gmail.com", 48123456789)
    store1.add_user(alex)

    alex.add_to_cart(store1, maugli)
    alex.add_to_cart(store1, generation_p)

    alex.make_order("Beverly Hills, 21")
    alex.show_curr_order_list()
    alex.show_order(1)
    alex.pay_order(1)

    store1.show_books()

    alex.show_curr_order_list()
    alex.show_prev_order_list()
