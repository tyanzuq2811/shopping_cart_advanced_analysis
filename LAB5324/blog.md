# Phân Tích Độ Nhạy Tham Số Với Và Không Có Trọng Số Trong Khai Thác Luật Liên Kết: Kết Quả Thí Nghiệm Chi Tiết

## Giới Thiệu

Trong dự án phân tích giỏ hàng nâng cao, chủ đề 4 tập trung vào việc đánh giá độ nhạy của các tham số trong thuật toán khai thác luật liên kết (association rules). Chúng tôi so sánh luật thường (dựa trên tần suất xuất hiện) và luật có trọng số (dựa trên giá trị kinh doanh như giá bán sản phẩm). Mục tiêu là xác định ngưỡng tham số hợp lý cho hai kịch bản kinh doanh: khai thác hành vi mua phổ biến và tối đa hóa giá trị/doanh thu.

Dữ liệu sử dụng là bộ dữ liệu giao dịch của UK, đã được làm sạch, với 18,021 giao dịch và 4,007 sản phẩm duy nhất. Để tối ưu hiệu suất, chúng tôi lọc top 100 sản phẩm phổ biến nhất, giảm xuống 18,021 giao dịch và 100 sản phẩm. Basket được chuẩn bị dưới dạng ma trận nhị phân, và trọng số dựa trên UnitPrice của từng sản phẩm trong giao dịch.

## Phương Pháp Thực Hiện

### 1. Chuẩn Bị Dữ Liệu
- **Dữ liệu gốc**: `cleaned_uk_data.csv` với các cột InvoiceNo, Description, Quantity, UnitPrice.
- **Basket chuẩn bị**: Chuyển đổi thành ma trận nhị phân (1 nếu sản phẩm có trong giao dịch, 0 nếu không). Lọc top 100 items để giảm kích thước.
- **Trọng số**: Ma trận UnitPrice cho từng sản phẩm trong từng giao dịch, dùng để tính toán weighted support thực sự (tổng trọng số của giao dịch chứa itemset / tổng trọng số toàn bộ).

### 2. Thí Nghiệm Luật Thường
- **Thuật toán**: Apriori từ thư viện `mlxtend`.
- **Tham số thử nghiệm**:
  - `min_support`: [0.01, 0.02, 0.05, 0.1]
  - `min_confidence`: [0.1, 0.2, 0.3, 0.5]
  - `min_lift`: [1.0, 1.2, 1.5, 2.0]
- **Đầu ra**: Số lượng luật, danh sách luật, top sản phẩm.

### 3. Thí Nghiệm Luật Có Trọng Số
- **Thuật toán**: Apriori từ thư viện `apyori` với tính toán weighted support thủ công (tìm itemsets với min_support thấp, sau đó lọc theo weighted support).
- **Tham số thử nghiệm**:
  - `min_weighted_support`: [0.008, 0.01, 0.02, 0.05] (bắt đầu từ 0.008 để tránh thời gian chạy lâu)
  - `min_weighted_lift`: [1.0, 1.2, 1.5, 2.0]
- **Đầu ra**: Frequent itemsets với weighted support và rules (nếu có).

### 4. Phân Tích Độ Nhạy
- Vẽ biểu đồ số lượng luật theo tham số (sử dụng matplotlib và seaborn).
- Phân tích top sản phẩm xuất hiện trong luật.
- Quan sát sự thay đổi cấu trúc sản phẩm.

### 5. Rút Ra Ngưỡng
- Dựa trên kết quả, đề xuất ngưỡng cho hai mục tiêu.

## Kết Quả Thí Nghiệm

### Luật Thường (Regular Association Rules)
Thí nghiệm tạo ra tổng cộng 64 tổ hợp tham số, với số lượng luật dao động từ 3,319 đến 0.

- **Ví dụ kết quả** (dựa trên notebook cell 4 và 11):
  - min_support=0.01, min_confidence=0.1, min_lift=1.0: 3,319 luật
  - min_support=0.01, min_confidence=0.1, min_lift=2.0: 3,257 luật
  - min_support=0.1, min_confidence=0.5, min_lift=2.0: 0 luật (quá chặt)

- **Sự thay đổi số lượng luật**:
  - Giảm min_support tăng số luật đáng kể (từ 0.01: ~3,300 luật xuống 0.1: ít luật).
  - Tăng min_confidence và min_lift giảm số luật, nhưng ít ảnh hưởng hơn support.

- **Top sản phẩm trong luật** (dựa trên notebook cell 13, luật đầu tiên):
  - Các sản phẩm phổ biến như túi đựng và phụ kiện (ví dụ: JUMBO BAG RED RETROSPOT, LUNCH BAG RED RETROSPOT), cho thấy hành vi mua phổ biến của khách hàng UK.

### Luật Có Trọng Số (Weighted Association Rules)
Thí nghiệm tạo ra luật với weighted support, ưu tiên giao dịch có giá trị cao.

- **Ví dụ kết quả** (dựa trên notebook cell 11):
  - min_weighted_support=0.01, min_weighted_lift=1.0: 1,245 luật (ít hơn luật thường vì weighted support nghiêm ngặt hơn).
  - min_weighted_support=0.008: Nhiều luật hơn, nhưng thời gian chạy tăng.
  - Frequent itemsets: Với min_weighted_support=0.01, có itemsets như single items và pairs, nhưng ít pairs do dữ liệu giao dịch nhỏ.

- **Sự thay đổi số lượng luật**:
  - Tăng min_weighted_support giảm số luật nhanh chóng.
  - Weighted rules tập trung vào sản phẩm giá trị cao hơn (ví dụ: DOTCOM POSTAGE với support cao).

- **Top sản phẩm trong luật** (nếu có, dựa trên phân tích tương tự luật thường):
  - Ưu tiên sản phẩm đắt tiền hơn so với luật thường.

### Phân Tích Độ Nhạy
### Phân Tích Độ Nhạy
- **Biểu đồ số lượng luật** (ghi chú: Xem notebook cell 12 - Vẽ biểu đồ số lượng luật theo tham số):
<img width="858" height="548" alt="image" src="https://github.com/user-attachments/assets/e343b4da-9b3a-4110-913c-9d7a1eb289dc" />
<img width="862" height="551" alt="image" src="https://github.com/user-attachments/assets/97426a79-e443-4133-9595-dd762e7ec909" />

  - **Luật thường**: Biểu đồ line plot với x='min_support', y='num_rules', hue='min_confidence', style='min_lift'. Đường cong giảm mạnh khi tăng min_support (từ 0.01: ~3,300 luật xuống 0.1: 0 luật), phản ánh độ nhạy cao của tham số này. Hue theo min_confidence (0.1-0.5) và style theo min_lift (1.0-2.0) cho thấy confidence và lift ảnh hưởng ít hơn, chủ yếu làm mịn đường cong.
  - **Luật có trọng số**: Biểu đồ tương tự với x='min_weighted_support', y='num_rules', hue='min_weighted_lift'. Số luật ít hơn (ví dụ, 1,245 luật tại 0.01 so với 3,319 của luật thường), đường cong giảm nhanh hơn do weighted support nghiêm ngặt hơn, ưu tiên giao dịch giá trị cao. Độ nhạy cao với min_weighted_support, lift ảnh hưởng qua hue (1.0-2.0).
  - **So sánh độ nhạy**: Luật thường nhạy cảm với min_support (thay đổi lớn số luật), luật weighted nhạy cảm hơn với giá trị kinh doanh (ít luật nhưng chất lượng cao hơn). Thêm scatter plot hoặc heatmap có thể trực quan hóa tương quan giữa tham số (ví dụ, heatmap cho num_rules vs min_support và min_confidence).
<img width="724" height="548" alt="image" src="https://github.com/user-attachments/assets/033c0e08-1dab-4365-81a1-aae5b056bb63" />
<img width="714" height="550" alt="image" src="https://github.com/user-attachments/assets/3d2d97cf-bc90-4648-a1f5-7232ef3bc058" />

  - **Heatmap cho luật thường** (notebook cell 13): Pivot table trung bình num_rules theo min_support (hàng) và min_confidence (cột), màu Blues (sáng = nhiều luật, tối = ít luật). Annotations hiển thị số chính xác. Ví dụ, vùng min_support=0.01 và min_confidence=0.1 có ~3,300 luật (rất sáng), giảm dần khi tăng tham số. Cho thấy min_support ảnh hưởng mạnh nhất, min_confidence ít hơn.
  - **Heatmap cho luật có trọng số** (notebook cell 13): Tương tự, theo min_weighted_support và min_weighted_lift, màu Reds. Vùng min_weighted_support=0.01 và min_weighted_lift=1.0 có ~1,245 luật (ít hơn regular), giảm nhanh hơn do weighted support nghiêm ngặt. Phản ánh ưu tiên giá trị kinh doanh, độ nhạy cao với support hơn lift.
  - **So sánh heatmap**: Regular heatmap có vùng sáng rộng hơn (nhiều luật), weighted heatmap tối hơn và giảm nhanh, nhấn mạnh sự khác biệt trong độ nhạy tham số giữa hai phương pháp.

- **Cấu trúc sản phẩm** (ghi chú: Xem notebook cell 13):
  - Luật thường tập trung vào sản phẩm phổ biến.
  - Weighted ưu tiên sản phẩm giá trị cao, làm thay đổi top products.

- **Luật có giá trị kinh doanh cao** (ghi chú: Xem notebook cell 14):
  - Lọc luật với lift >2.0 và confidence >0.5. Weighted rules có thể có ít luật hơn nhưng chất lượng cao hơn.

## Ngưỡng Hợp Lý Đề Xuất

### Cho Khai Thác Hành Vi Mua Phổ Biến
- **Mục tiêu**: Tìm nhiều luật để hiểu pattern mua sắm chung.
- **Ngưỡng đề xuất** (dựa trên notebook cell 16):
  - min_support: 0.02 (cân bằng giữa số lượng và ý nghĩa)
  - min_confidence: 0.2
  - min_lift: 1.2
- **Lý do**: Support thấp tạo ~2,500 luật, đủ để phân tích mà không quá ồn.

### Cho Tối Đa Hóa Giá Trị/Doanh Thu
- **Mục tiêu**: Tập trung vào luật mạnh, có giá trị cao.
- **Ngưỡng đề xuất cho luật có trọng số** (dựa trên notebook cell 18):
  - min_weighted_support: 0.05
  - min_weighted_lift: 1.5
- **Ngưỡng đề xuất cho luật thường**:
  - min_support: 0.05
  - min_confidence: 0.3
  - min_lift: 1.5
- **Lý do**: Ngưỡng cao hơn lọc ra luật chất lượng, weighted ưu tiên giá trị kinh doanh.

## Công Cụ Và Thư Viện Sử Dụng
- **Python**: Ngôn ngữ chính.
- **mlxtend**: Cho Apriori và association_rules.
- **apyori**: Cho weighted Apriori với tính toán thủ công.
- **pandas, numpy**: Xử lý dữ liệu.
- **matplotlib, seaborn**: Trực quan hóa (ghi chú: Sử dụng trong notebook cell 12 để vẽ biểu đồ).
- **Jupyter Notebook**: Thực hiện và ghi chép.

## Kết Luận Và Khuyến Nghị
Phân tích độ nhạy cho thấy min_support là tham số quan trọng nhất. Luật thường hiệu quả cho hành vi phổ biến, luật có trọng số cho giá trị kinh doanh. Kết quả từ notebook cho thấy weighted rules ít hơn nhưng tập trung hơn.

Khuyến nghị: Sử dụng ngưỡng đề xuất. Thêm biểu đồ trực quan như heatmap cho tương quan tham số (có thể mở rộng notebook). Cho tương lai, thu thập dữ liệu transactions lớn hơn để tăng pairs trong weighted rules.
