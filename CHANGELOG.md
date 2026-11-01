## [Unreleased]

## [1.0.1] - 2026-11-01
### Fixed
- Sửa lỗi tìm kiếm title không phân biệt hoa/thường (Issue #20).

## [1.0.0] - 2026-11-01
### Added
- Hàm `calculate_discount` để tính tiền giảm giá.
- Hàm `search_by_title` trong `search.py` (#4).
- Hàm `print_cart` cho lớp `Cart`.
- Cập nhật thông báo khi thêm đĩa vào giỏ hàng thành công (từ dev 1).
- Template Pull Request (`docs: add pull request template`).
- Các bộ kiểm thử (test) tái hiện lỗi cho tính năng giảm giá và giới hạn giỏ hàng.

### Fixed
- Lỗi tính sai số tiền sau giảm giá và bổ sung validate phần trăm hợp lệ.
- Lỗi giới hạn giỏ hàng (Cart limit bug #5).