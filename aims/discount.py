def calculate_discount(total, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")
    # Số tiền thực trả = Tổng tiền - (Tổng tiền * phần trăm giảm / 100)
    return total - (total * percent / 100)