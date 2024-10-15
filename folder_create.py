import os
import shutil

# 기본 폴더 경로 설정 (dev 폴더가 있는 경로로 변경)
base_dir = "C:/dev"

# 생성할 폴더 구조
folder_structure = {
    "01_projects": ["stock_dashboard", "qr_code_attendance", "personal_blog"],
    "02_learning": ["python", "javascript"],
    "03_journal": ["01_jan", "02_feb", "03_mar", "04_apr", "05_may", "06_jun", "07_jul", "08_aug", "09_sep", "10_oct", "11_nov", "12_dec"]
}

# 폴더 생성 함수
def create_folders(base_dir, structure):
    for parent_folder, sub_folders in structure.items():
        parent_path = os.path.join(base_dir, parent_folder)
        os.makedirs(parent_path, exist_ok=True)
        for sub_folder in sub_folders:
            sub_folder_path = os.path.join(parent_path, sub_folder)
            os.makedirs(sub_folder_path, exist_ok=True)

# 파일 이동 함수 (지정된 폴더로 파일을 이동하는 예시)
def move_files(base_dir):
    # 이동시키려는 파일 경로를 추가하세요
    file_mappings = {
        "README.md": "01_projects/stock_dashboard",
        "mac_env.md": "tools"
    }

    for file_name, destination in file_mappings.items():
        source_path = os.path.join(base_dir, file_name)
        destination_path = os.path.join(base_dir, destination, file_name)

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print(f"Moved {file_name} to {destination}")

# 스크립트 실행
create_folders(base_dir, folder_structure)
move_files(base_dir)
