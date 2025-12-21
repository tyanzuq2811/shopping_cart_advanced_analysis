# 📦 Case Study: Phân tích giỏ hàng nâng cao với Apriori và FP-Growth

## 👥 Thông tin Nhóm
- **Nhóm:** Nhóm nghiên cứu AI Agent
- **Thành viên:** 
  - Nguyễn Công Khanh (Trưởng nhóm)
  - Các thành viên khác (nếu có)
- **Chủ đề:** Phân tích giỏ hàng và khai thác luật kết hợp
- **Dataset:** Online Retail (UCI) - Dữ liệu bán lẻ UK (2010-2011)

## Mục tiêu 
Mục tiêu của nhóm là:  
> Khám phá mối quan hệ giữa các sản phẩm thường được mua cùng nhau trong dữ liệu bán lẻ, so sánh hiệu suất của hai thuật toán Apriori và FP-Growth trong việc khai thác luật kết hợp, và cung cấp insights để tối ưu hóa chiến lược bán hàng.

## 1. Ý tưởng & Feynman Style
Giải thích lại bài toán theo cách **dễ hiểu nhất** (không technical):
- Apriori và FP-Growth dùng để tìm ra "quy tắc mua hàng" từ dữ liệu giỏ hàng, ví dụ: nếu khách mua sữa thì có khả năng mua bánh mì.
- Phù hợp cho bài toán giỏ hàng vì giúp doanh nghiệp hiểu hành vi mua sắm, đề xuất sản phẩm liên quan, tăng doanh số.
- Ý tưởng thuật toán: Apriori kiểm tra từng tập sản phẩm có xuất hiện cùng nhau không (từ nhỏ đến lớn), FP-Growth xây cây để tìm nhanh hơn mà không cần kiểm tra nhiều lần.

## 2. Quy trình Thực hiện

1) Load & làm sạch dữ liệu (loại bỏ giao dịch lỗi, tập trung UK)
2) Tạo ma trận basket (transaction × product, dạng boolean)
3) Áp dụng Apriori và FP-Growth để tìm frequent itemsets
4) Trích xuất luật kết hợp từ itemsets
5) So sánh hai thuật toán về thời gian, số lượng itemsets/rules, độ dài itemset
6) Trực quan hóa kết quả và phân tích insights

## 3. Tiền xử lý Dữ liệu
- Những bước làm sạch:
  - Loại bỏ sản phẩm có tên rỗng hoặc thiếu thông tin
  - Loại bỏ transaction bị cancel (InvoiceNo bắt đầu bằng "C")
  - Loại bỏ số lượng âm hoặc đơn giá âm
  - Tập trung vào dữ liệu từ United Kingdom để đảm bảo tính nhất quán

- Thống kê nhanh:
  - Số giao dịch sau lọc: 397,924
  - Số sản phẩm duy nhất: Khoảng 3,891 (sau lọc)
  - Số khách hàng: 4,372</content>
<parameter name="filePath">/hdd3/nckh-AIAgent/tyanzuq/DataMining/shopping_cart_advanced_analysis/case_study.md


