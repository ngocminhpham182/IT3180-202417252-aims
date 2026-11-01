MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("Đã thêm đĩa thành công vào trong giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        """In ra danh sách các đĩa trong giỏ hàng hoặc thông báo giỏ trống."""
        if len(self.items) == 0:
            print("The cart is empty")
        else:
            print("********************CART********************")
            print("Ordered Items:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. DVD - {item.title} - {item.category} - {item.cost} $")
            print(f"Total cost: {self.total_cost()} $")
            print("********************************************")

    def sort_by_title(self):
        """Sắp xếp các item trong giỏ hàng theo tiêu đề (Alphabet)"""
        self.items.sort(key=lambda x: x.title)
        print("Cart has been sorted by title.")

    def sort_by_cost(self):
        """Sắp xếp các item trong giỏ hàng theo giá tiền giảm dần"""
        self.items.sort(key=lambda x: x.cost, reverse=True)
        print("Cart has been sorted by cost.")