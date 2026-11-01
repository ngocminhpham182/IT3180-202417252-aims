def search_by_title(item_list, keyword):
    """Tìm kiếm các đĩa DVD trong danh sách theo tiêu đề (hỗ trợ tìm kiếm gần đúng/không phân biệt hoa thường)."""
    # fix: updated search_by_title to handle case-insensitive properly (Issue #20)
    keyword_lower = keyword.lower()
    result = [item for item in item_list if keyword_lower in item.title.lower()]
    return result