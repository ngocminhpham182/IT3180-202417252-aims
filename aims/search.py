def search_by_title(item_list, keyword):
    """Tìm kiếm các đĩa DVD trong danh sách theo tiêu đề (hỗ trợ tìm kiếm gần đúng/không phân biệt hoa thường)."""
    keyword_lower = keyword.lower()
    result = [item for item in item_list if keyword_lower in item.title.lower()]
    return result

def search_by_category(items, keyword):
    """
    Tìm kiếm đĩa trong danh sách dựa theo danh mục (category).
    Có xử lý không phân biệt hoa/thường (case-insensitive).
    """
    result = []
    for dvd in items:
        # Kiểm tra xem từ khóa có nằm trong category của đĩa không
        # (dùng .lower() để không bị phân biệt hoa/thường giống như lỗi ở search_by_title)
        # fix: updated search_by_title to handle case-insensitive properly (Issue #20)
        if keyword.lower() in dvd.category.lower():
            result.append(dvd)
    return result