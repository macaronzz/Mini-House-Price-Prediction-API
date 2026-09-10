# Week 06 Assignment - Mini House-Price Prediction API

## How to run the project
1. Mở terminal và di chuyển vào thư mục `backend/`: `cd backend`
2. Kích hoạt virtual environment của bạn (nếu có).
3. Chạy server bằng uvicorn: `uvicorn main:app --reload`
4. Mở trình duyệt và truy cập trang form tại: `http://127.0.0.1:8000/static/house_form.html`

## Answers to "Explain Why" Questions

**Task 3.4: Try calling `/predict` without `location` — confirm it still works and explain why.**
* Lệnh gọi vẫn hoạt động vì trong định nghĩa hàm `get_predict`, tham số `location` được gán giá trị mặc định là `"other"` (`location: str = "other"`). Do đó, FastAPI hiểu đây là một tham số tùy chọn (optional query parameter). Nếu người dùng không cung cấp, server sẽ tự động dùng giá trị "other" để tính toán thay vì báo lỗi thiếu dữ liệu.

**Task 3.5: Try calling `/predict` without `area` — confirm you get a 422 error and explain why.**
* Sẽ xuất hiện lỗi HTTP 422 Unprocessable Entity vì `area` được định nghĩa là một tham số bắt buộc (required query parameter) có kiểu dữ liệu `float` mà không có giá trị mặc định. Khi không truyền tham số này, cơ chế auto-validation của FastAPI (nhờ Pydantic) sẽ phát hiện request thiếu dữ liệu đầu vào cần thiết và lập tức từ chối request, trả về mã lỗi 422.

**Task 5.2: Explain why a relative URL (like `/predict?...`) works now.**
* Relative URL hoạt động vì ở Task 4, chúng ta đã dùng `StaticFiles` để host trực tiếp trang `house_form.html` trên cùng một server FastAPI (cùng địa chỉ `127.0.0.1` và cùng port `8000`). Trình duyệt hiểu rằng `/predict` thuộc về cùng một gốc (origin) với trang web hiện tại đang được tải, giúp tránh hoàn toàn lỗi vi phạm chính sách CORS (Cross-Origin Resource Sharing).

**Task 6 (Bonus): Explain one difference between sending data via query parameters and sending it via a JSON body.**
* **Query Parameters (GET):** Dữ liệu được nối trực tiếp vào thanh địa chỉ URL (ví dụ: `?area=80&bedrooms=3`), dễ dàng chia sẻ link và lưu lại lịch sử, nhưng giới hạn độ dài và kém bảo mật.
* **JSON Body (POST):** Dữ liệu được gửi ngầm bên trong payload của HTTP Request, không hiển thị trên URL. Cách này phù hợp để gửi các cấu trúc dữ liệu lớn, phức tạp hoặc chứa thông tin nhạy cảm.