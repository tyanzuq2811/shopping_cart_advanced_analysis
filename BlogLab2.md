# 📦 Case Study: Phân tích giỏ hàng nâng cao với Apriori và FP-Growth

## 👥 Thông tin Nhóm
- **Nhóm:** Nhóm nghiên cứu AI Agent
- **Thành viên:**
  - Lê Tuấn Dũng
  - Lê Thị Ngọc Bích
  - Đỗ Ngọc Trung
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
  - 
  - Số khách hàng: 4,372</content>
<parameter name="filePath">/hdd3/nckh-AIAgent/tyanzuq/DataMining/shopping_cart_advanced_analysis/case_study.md
## 4. Áp dụng Apriori
**Tham số sử dụng:**
- `min_support = 0.01` (1% giao dịch chứa tập mục)
- `min_threshold = 1.0` (cho lift)
- `max_len = 3` (độ dài tối đa của tập mục)

### Thử nghiệm Tham số
Để hiểu rõ tác động của từng tham số, chúng tôi thử nghiệm thay đổi giá trị và quan sát sự thay đổi kết quả.

#### 4.1. Thay đổi min_support
**Giá trị mặc định:** `MIN_SUPPORT = 0.01`
<img width="801" height="471" alt="image" src="https://github.com/user-attachments/assets/f72d6f31-d83b-4815-9ec6-550c5450a581" />
<img width="798" height="464" alt="image" src="https://github.com/user-attachments/assets/98ab3119-a45f-4cfe-a8f5-aa4bde9e6930" />


**Giảm `min_support` xuống 0.008**

- Thời gian chạy: **37.28 giây**
- Số tập mục phổ biến: **4,002**

→ Số tập mục phổ biến tăng gần gấp đôi so với giá trị mặc định, cho phép phát hiện thêm nhiều mối quan hệ tiềm năng. Tuy nhiên, chi phí tính toán tăng và nguy cơ xuất hiện nhiễu cũng cao hơn.

---

**Giảm sâu `min_support` xuống 0.006**

- Thời gian chạy: **201.44 giây**
- Số tập mục phổ biến: **9,968**

→ Số tập mục và thời gian chạy tăng đột biến, cho thấy Apriori trở nên kém hiệu quả khi ngưỡng support quá thấp. Mặc dù phát hiện được nhiều pattern hiếm, kết quả dễ bị nhiễu và khó áp dụng trong thực tế.

---

**Tăng `min_support` lên 0.02**

- Thời gian chạy: **2.77 giây**
- Số tập mục phổ biến: **400**

→ Số tập mục giảm mạnh, tập trung vào các sản phẩm phổ biến nhất. Kết quả sạch hơn và thời gian xử lý nhanh, phù hợp cho các bài toán quy mô lớn.

---

**Tăng `min_support` lên 0.03**

- Thời gian chạy: **0.44 giây**
- Số tập mục phổ biến: **145**

→ Chỉ giữ lại các tập mục xuất hiện rất thường xuyên. Kết quả đơn giản, dễ diễn giải nhưng có thể bỏ sót nhiều mối quan hệ tiềm năng.

---

**Nhận xét chung:**  
`min_support` là tham số ảnh hưởng mạnh nhất đến số lượng tập mục phổ biến và thời gian chạy của thuật toán. Giá trị quá thấp gây bùng nổ tập mục và chi phí tính toán cao, trong khi giá trị quá cao làm mất nhiều thông tin có giá trị.

---

