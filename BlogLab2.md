# Case Study: Phân tích giỏ hàng nâng cao với Apriori và FP-Growth

## Thông tin Nhóm
- **Nhóm:** 13
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
  - Số khách hàng: 4,372

## 4. Kết quả Thử nghiệm và So sánh Apriori vs FP-Growth

### Tham số Chung
- `min_threshold = 1.0` (cho lift)
- `max_len = 3` (độ dài tối đa của tập mục)
- `metric = "lift"`

### Bảng So sánh Theo min_support

| min_support | Algorithm  | Runtime (s) | N_Itemsets | N_Rules | Avg_Itemset_Length | Peak Memory (MB) |
|-------------|------------|-------------|------------|---------|---------------------|------------------|
| 0.006      | Apriori   | 712.10     | 9968      | 30608  | 2.20               | 91133.56        |
| 0.006      | FP-Growth | 397.20     | 9968      | 30608  | 2.20               | 1239.94         |
| 0.008      | Apriori   | 182.37     | 4002      | 9504   | 1.96               | 28854.57        |
| 0.008      | FP-Growth | 142.59     | 4002      | 9504   | 1.96               | 1239.94         |
| 0.01       | Apriori   | 19.61      | 2120      | 3856   | 1.76               | 17149.53        |
| 0.01       | FP-Growth | 60.87      | 2120      | 3856   | 1.76               | 1239.94         |
| 0.02       | Apriori   | 4.45       | 400       | 218    | 1.26               | 2297.88         |
| 0.02       | FP-Growth | 10.79      | 400       | 218    | 1.26               | 1239.94         |
| 0.03       | Apriori   | 0.55       | 145       | 22     | 1.08               | 459.79          |
| 0.03       | FP-Growth | 4.96       | 145       | 22     | 1.08               | 1239.94         |

### Nhận xét Khi min_support Giảm
- **Thời gian chạy**: Khi min_support giảm (từ 0.03 xuống 0.006), thời gian chạy của cả hai thuật toán tăng đáng kể. Apriori thường nhanh hơn ở min_support cao (0.02-0.03), nhưng chậm hơn ở min_support thấp (0.006-0.008). FP-Growth ổn định hơn về thời gian tương đối.
- **Số lượng itemsets và rules**: Giảm min_support làm tăng số itemsets và rules (từ 145 itemsets ở 0.03 lên 9968 ở 0.006), vì nhiều tập mục hiếm hơn được phát hiện. Cả hai thuật toán cho cùng số lượng kết quả.
- **Độ dài trung bình itemset**: Tăng khi min_support giảm (từ 1.08 lên 2.20), vì các itemset dài hơn (3 mục) xuất hiện nhiều hơn.
- **Bộ nhớ đỉnh (Peak Memory)**: Apriori tiêu thụ bộ nhớ nhiều hơn FP-Growth, đặc biệt ở min_support thấp (lên đến 28GB), trong khi FP-Growth ổn định ở ~1.2GB. Điều này cho thấy FP-Growth hiệu quả hơn về bộ nhớ cho dữ liệu lớn.
- **Khuyến nghị**: Sử dụng FP-Growth cho min_support thấp để tiết kiệm bộ nhớ và thời gian. Apriori phù hợp cho min_support cao khi cần tốc độ nhanh.</content>

## 6. Insight từ Kết quả
**Insight #1:**  Các loại HERB MARKER (que đánh dấu thảo mộc) có xu hướng được mua cùng nhau 

Nhiều luật cho thấy khách hàng  thường mua kèm HERB MARKER THYME, CHIVES, ROSEMARY, PARSLEY, BASIL và MINT với confidence rất cao (≈ 90%) và lift lớn (> 70)

Diễn giải: 
Khách hàng không mua HERB MARKER một cách đơn lẻ mà thường mua nhiều loại HERB MARKER cùng lúc, phục vụ cho việc phân biệt các loại cây/nguyên liệu thảo mộc. 

**Insight #2:** Khách hàng có xu hướng mua trọn bộ sản phẩm cùng phong cách REGENCY

Các luật cho thấy mối liên hệ rất mạnh giữa: REGENCY SUGAR BOWL GREEN, REGENCY MILK JUG PINK, REGENCY TEAPOT ROSES, REGENCY TEA PLATE, REGENCY TEACUP AND SAUCER Với: Confidence cao (≈ 47–96%), Lift rất lớn (≈ 10–57)

Diễn giải:
Khi khách đã chọn một sản phẩm thuộc dòng REGENCY, khả năng rất cao họ sẽ mua thêm các sản phẩm REGENCY khác để đồng bộ bộ trà / bộ bàn ăn.

**Insight #3:** Hành vi mua mang tính bộ sưu tập – cùng thiết kế nhưng khác màu

Các luật cho thấy:

- REGENCY TEACUP AND SAUCER: các màu GREEN, PINK, ROSES thường được mua cùng nhau với Confidence cao (≈ 70%), Lift lớn (≈ 15)

- REGENCY TEA PLATE: các màu GREEN, PINK, ROSES thường được mua cùng nhau với Confidence cao (≈ 75%), Lift lớn (≈ 45)

Diễn giải:
Khách hàng mua sản phẩm không đơn thuần vì nhu cầu sử dụng, mà vì tính thẩm mỹ: sự đồng nhất về thiết kế nhưng đa đạng màu sắc.

**Insight #4:** Khách hàng có xu hướng mua trọn bộ sản phẩm dòng POPPY'S PLAYHOUSE  

Các luật cho thấy mối liên hệ rất mạnh giữa: POPPY'S PLAYHOUSE LIVINGROOM, BEDROOM, KITCHEN Với: Confidence cao (≈ 75%), Lift rất lớn (≈ 40)

Diễn giải: Khi khách đã chọn một sản phẩm thuộc dòng POPPY'S PLAYHOUSE, khả năng rất cao họ sẽ mua thêm các sản phẩm POPPY'S PLAYHOUSE khác để đủ bộ sưu tập.

**Insight #5:** Khách hàng có xu hướng mua trọn bộ sản phẩm dòng WOODEN CHRISTMAS SCANDINAVIAN

Các luật cho thấy mối liên hệ rất mạnh giữa: WOODEN CHRISTMAS SCANDINAVIAN HEART, STAR, TREE với: Confidence cao (≈ 70%), Lift lớn (≈ 30)

Diễn giải: Khi khách mua đồ trang trí giáng sinh thì thường mua đồng bộ cả cây, ngôi sao và trái tim.

## 7. Kết luận & Đề xuất Kinh doanh
**Đề xuất 1:** Bán combo theo bộ sưu tập

- Combo REGENCY: Sugar Bowl + Milk Jug + TEAPOT
- Combo POPPY'S PLAYHOUSE: LIVINGROOM + BEDROOM + KITCHEN

**Đề xuất 2:** Bán combo theo cùng thiết kế nhưng khác màu 

- Combo REGENCY TEACUP AND SAUCER: các màu GREEN + PINK + ROSES
- Combo REGENCY TEA PLATE: các màu GREEN + PINK + ROSES

**Đề xuất 3:** Xếp các sản phẩm theo phong cách REGENCY cùng một khu vực
bao gồm các sản phẩm
- REGENCY TEACUP AND SAUCER
- REGENCY TEA PLATE
- REGENCY SUGAR BOWL GREEN
- REGENCY MILK JUG PINK
- REGENCY TEAPOT ROSES

**Đề xuất 4:** Bán combo WOODEN CHRISTMAS SCANDINAVIAN khi gần Giáng sinh 

- Combo WOODEN CHRISTMAS SCANDINAVIAN: HEART + STAR + TREE
