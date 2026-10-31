import unittest
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart, MAX_NUMBERS_ORDERED


class TestCart(unittest.TestCase):
    """Lớp kiểm thử các chức năng của giỏ hàng (Cart)."""

    def test_add_dvd_until_full(self):
        """Kiểm thử việc thêm đĩa cho đến khi đạt giới hạn MAX_NUMBERS_ORDERED và chặn đĩa tiếp theo."""
        cart = Cart()

        # Thêm đủ số lượng tối đa cho phép (20 đĩa)
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {i+1}", "Category", cost=10.0)
            result = cart.add_dvd(dvd)
            self.assertTrue(result, f"Thêm đĩa thứ {i+1} phải thành công (True)")

        # Thêm đĩa thứ 21 (vượt quá giới hạn) -> Phải trả về False và không cho thêm vào giỏ
        extra_dvd = DigitalVideoDisc("Extra DVD", "Category", cost=15.0)
        result_extra = cart.add_dvd(extra_dvd)
        
        self.assertFalse(result_extra, "Thêm đĩa thứ 21 phải bị từ chối và trả về False")
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED, "Số lượng đĩa trong giỏ hàng không được vượt quá 20")


if __name__ == "__main__":
    unittest.main()