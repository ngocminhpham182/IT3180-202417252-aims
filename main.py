from aims.dvd import DigitalVideoDisc
from aims.cart import Cart
from aims.search import search_by_title


def main():
    print("AIMS-mini v1.1.0")

    cart = Cart()
    dvd1 = DigitalVideoDisc(
        "The Lion King", "Animation", "Roger Allers", 87, 19.95
    )
    dvd2 = DigitalVideoDisc(
        "Star Wars", "Science Fiction", "George Lucas", 87, 24.95
    )
    dvd3 = DigitalVideoDisc("Aladdin", "Animation", cost=18.99)

    cart.add_dvd(dvd1)
    cart.add_dvd(dvd2)
    cart.add_dvd(dvd3)

    print("\n--- TEST SEARCH BY TITLE ---")
    # Thử tìm kiếm đĩa có chứa từ khóa "lion"
    found_items = search_by_title(cart.items, "lion")
    print(f"Kết quả tìm kiếm cho từ khóa 'lion':")
    for item in found_items:
        print(f"- {item.title} ({item.cost} $)")


if __name__ == "__main__":
    main()