def calculate_discount(total, percent):
    # Lỗi: Không kiểm tra percent > 100 và công thức tính nhầm (chỉ tính số tiền giảm chứ không trừ vào tổng)
    return total * percent / 100