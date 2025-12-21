import papermill as pm
import os

# Đường dẫn gốc tới file spmf.jar của bạn (dùng raw string r"..." để tránh lỗi ký tự \)
JAR_PATH = r"D:\DataEngineer\DataMining\shopping_cart_advanced_analysis\src\spmf2.jar"

# Tạo thư mục lưu kết quả chạy
os.makedirs("notebooks/runs", exist_ok=True)

def run_all():
    # --- BƯỚC 1: LÀM SẠCH DỮ LIỆU (HUIM) ---
    # Sửa: Tên file đúng là '01_data_cleaning_huim.ipynb'
    print("Step 1: Data Cleaning for HUIM...")
    pm.execute_notebook(
        'notebooks/01_data_cleaning_huim.ipynb',  # <--- Đã sửa tên file
        'notebooks/runs/01_clean_out.ipynb'
    )
    
    # --- BƯỚC 2: CHUẨN BỊ UTILITY ---
    # Sửa: Tên file đúng là '02_utility_preparation.ipynb'
    print("Step 2: Utility Preparation...")
    pm.execute_notebook(
        'notebooks/02_utility_preparation.ipynb', # <--- Đã sửa tên file
        'notebooks/runs/02_utility_out.ipynb'
    )
    
    # --- BƯỚC 3: KHAI THÁC HUIM (EFIM) ---
    # Sửa: Tên file đúng là '03_huim_modelling.ipynb'
    print("Step 3: Mining HUIM...")
    pm.execute_notebook(
        'notebooks/03_huim_modelling.ipynb',      # <--- Đã sửa tên file
        'notebooks/runs/03_huim_out.ipynb'
    )
    
    print("=== HOÀN THÀNH TOÀN BỘ PIPELINE HUIM ===")

if __name__ == "__main__":
    run_all()