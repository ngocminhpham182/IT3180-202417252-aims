import unittest
from aims.discount import calculate_discount

class TestDiscount(unittest.TestCase):
    
    def test_calculate_discount_normal(self):
        # Kiểm tra: 100 giảm 20% số tiền phải trả còn lại là 80
        # (Code cũ đang trả về 20 vì chỉ tính tiền giảm, nên đoạn này sẽ FAIL)
        self.assertEqual(calculate_discount(100, 20), 80)

    def test_calculate_discount_invalid_percent(self):
        # Kiểm tra: Truyền percent = 150 phải báo lỗi ValueError do không hợp lệ
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

if __name__ == "__main__":
    unittest.main()