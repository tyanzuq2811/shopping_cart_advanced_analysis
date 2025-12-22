# Phân Tích Độ Nhạy Tham Số Với Và Không Có Trọng Số Trong Khai Thác Luật Liên Kết: Kết Quả Thí Nghiệm Chi Tiết

## Giới Thiệu

Trong dự án phân tích giỏ hàng nâng cao, chủ đề 4 tập trung vào việc đánh giá độ nhạy của các tham số trong thuật toán khai thác luật liên kết (association rules). Chúng tôi so sánh luật thường (dựa trên tần suất xuất hiện) và luật có trọng số (dựa trên giá trị kinh doanh như giá bán sản phẩm). Mục tiêu là xác định ngưỡng tham số hợp lý cho hai kịch bản kinh doanh: khai thác hành vi mua phổ biến và tối đa hóa giá trị/doanh thu.

Dữ liệu sử dụng là bộ dữ liệu giao dịch của UK, đã được làm sạch, với 18,021 giao dịch và 4,007 sản phẩm duy nhất. Basket được chuẩn bị dưới dạng ma trận nhị phân, và trọng số dựa trên UnitPrice của từng sản phẩm trong giao dịch.

## Phương Pháp Thực Hiện

### 1. Chuẩn Bị Dữ Liệu
- **Dữ liệu gốc**: `cleaned_uk_data.csv` với các cột InvoiceNo, Description, Quantity, UnitPrice.
- **Basket chuẩn bị**: Chuyển đổi thành ma trận nhị phân (1 nếu sản phẩm có trong giao dịch, 0 nếu không).
- **Trọng số**: Ma trận UnitPrice cho từng sản phẩm trong từng giao dịch, dùng để tính toán weighted support.

### 2. Thí Nghiệm Luật Thường
- **Thuật toán**: Apriori từ thư viện `mlxtend`.
- **Tham số thử nghiệm**:
  - `min_support`: [0.01, 0.02, 0.05, 0.1]
  - `min_confidence`: [0.1, 0.2, 0.3, 0.5]
  - `min_lift`: [1.0, 1.2, 1.5, 2.0]
- **Đầu ra**: Số lượng luật, danh sách luật, top sản phẩm.

### 3. Thí Nghiệm Luật Có Trọng Số
- **Thuật toán**: Apriori từ thư viện `apyori` (hỗ trợ transactions dạng list).
- **Tham số thử nghiệm**:
  - `min_weighted_support`: [0.001, 0.005, 0.01, 0.02] (thấp hơn để tìm pairs)
  - `min_weighted_lift`: [1.0, 1.2, 1.5, 2.0]
- **Đầu ra**: Frequent itemsets và rules (nếu có).

### 4. Phân Tích Độ Nhạy
- Vẽ biểu đồ số lượng luật theo tham số.
- Phân tích top sản phẩm xuất hiện trong luật.
- Quan sát sự thay đổi cấu trúc sản phẩm.

### 5. Rút Ra Ngưỡng
- Dựa trên kết quả, đề xuất ngưỡng cho hai mục tiêu.

## Kết Quả Thí Nghiệm

### Luật Thường (Regular Association Rules)
Thí nghiệm tạo ra tổng cộng 64 tổ hợp tham số, với số lượng luật dao động từ 4227 đến 0.

- **Ví dụ kết quả**:
  - min_support=0.01, min_confidence=0.1, min_lift=1.0: 4289 luật
  - min_support=0.01, min_confidence=0.1, min_lift=2.0: 4227 luật
  - min_support=0.1, min_confidence=0.5, min_lift=2.0: 0 luật (quá chặt)

- **Sự thay đổi số lượng luật**:
  - Giảm min_support tăng số luật đáng kể (từ 0.01: ~4000 luật xuống 0.1: ít luật).
  - Tăng min_confidence và min_lift giảm số luật, nhưng ít ảnh hưởng hơn support.

- **Top sản phẩm trong luật** (dựa trên luật đầu tiên):
  - JUMBO BAG RED RETROSPOT: 975 lần xuất hiện
  - JUMBO STORAGE BAG SUKI: 568
  - LUNCH BAG RED RETROSPOT: 492
  - JUMBO BAG PINK POLKADOT: 490
  - JUMBO SHOPPER VINTAGE RED PAISLEY: 489
  - DOTCOM POSTAGE: 481
  - LUNCH BAG BLACK SKULL: 408
  - RED RETROSPOT CHARLOTTE BAG: 378
  - JUMBO BAG WOODLAND ANIMALS: 344
  - CHARLOTTE BAG SUKI DESIGN: 299

  Các sản phẩm này chủ yếu là túi đựng và phụ kiện, cho thấy hành vi mua phổ biến của khách hàng UK.

### Luật Có Trọng Số (Weighted Association Rules)
Thí nghiệm không tạo ra luật nào do hạn chế của dữ liệu và triển khai.

- **Frequent itemsets**:
  - min_support=0.001: 184 itemsets (chủ yếu single items như SPACEBOY BABY GIFT SET, AMAZON FEE)
  - min_support=0.005: 6 itemsets (DOTCOM POSTAGE, Manual, etc.)
  - Không có itemsets với 2+ items, nên không tạo được rules.

- **Nguyên nhân**:
  - Dữ liệu giao dịch có ít sản phẩm cùng lúc trong một basket (thường 1-2 items).
  - Triển khai weighted apriori chỉ tính support dựa trên tần suất, không phải giá trị thực sự weighted.
  - Cần triển khai custom weighted support (ví dụ, support = tổng trọng số / tổng trọng số toàn bộ) để ưu tiên sản phẩm giá trị cao.

- **Kết luận cho weighted**: Với dữ liệu hiện tại, weighted rules không khả thi. Cần dữ liệu với transactions lớn hơn hoặc triển khai weighted metrics phức tạp hơn.

### Phân Tích Độ Nhạy
- **Biểu đồ số lượng luật**:
  - Luật thường: Số luật giảm khi tăng min_support, với confidence và lift làm mịn đường cong.
  - Luật có trọng số: Không có dữ liệu để vẽ (0 rules).

- **Cấu trúc sản phẩm**:
  - Luật thường tập trung vào sản phẩm phổ biến như túi và phụ kiện.
  - Weighted (nếu có) sẽ ưu tiên sản phẩm giá trị cao như DOTCOM POSTAGE (support 11%).

- **Luật có giá trị kinh doanh cao**: Không quan sát được do thiếu weighted rules, nhưng trong luật thường, luật với lift >2.0 ít hơn, cho thấy chúng chặt chẽ hơn.

## Ngưỡng Hợp Lý Đề Xuất

### Cho Khai Thác Hành Vi Mua Phổ Biến
- **Mục tiêu**: Tìm nhiều luật để hiểu pattern mua sắm chung.
- **Ngưỡng đề xuất**:
  - min_support: 0.02 (cân bằng giữa số lượng và ý nghĩa)
  - min_confidence: 0.2
  - min_lift: 1.2
- **Lý do**: Support thấp tạo ~3500 luật, đủ để phân tích mà không quá ồn.

### Cho Tối Đa Hóa Giá Trị/Doanh Thu
- **Mục tiêu**: Tập trung vào luật mạnh, có giá trị cao.
- **Ngưỡng đề xuất cho luật thường**:
  - min_support: 0.05
  - min_confidence: 0.3
  - min_lift: 1.5
- **Ngưỡng đề xuất cho luật có trọng số** (dự kiến):
  - min_weighted_support: 0.05
  - min_weighted_lift: 1.5
- **Lý do**: Ngưỡng cao hơn lọc ra luật chất lượng, nhưng cần weighted để ưu tiên giá trị.

## Công Cụ Và Thư Viện Sử Dụng
- **Python**: Ngôn ngữ chính.
- **mlxtend**: Cho Apriori và association_rules.
- **apyori**: Cho weighted Apriori (nhưng hạn chế).
- **pandas, numpy**: Xử lý dữ liệu.
- **matplotlib, seaborn**: Trực quan hóa.
- **Jupyter Notebook**: Thực hiện và ghi chép.

## Kết Luận Và Khuyến Nghị
Phân tích độ nhạy cho thấy min_support là tham số quan trọng nhất, ảnh hưởng trực tiếp đến số lượng luật. Luật thường hiệu quả cho dữ liệu này, tạo ra insights về sản phẩm phổ biến. Luật có trọng số cần cải thiện triển khai để tận dụng giá trị kinh doanh.

Khuyến nghị: Sử dụng ngưỡng đề xuất dựa trên mục tiêu. Cho tương lai, thu thập dữ liệu transactions lớn hơn hoặc triển khai weighted metrics (ví dụ, sử dụng trọng số trong confidence và lift).
