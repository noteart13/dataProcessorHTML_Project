import json
import os

# Đường dẫn tới file đầu vào và đầu ra
input_path = os.path.join('..', 'data', 'step3_mappedjson')
temp_output_path = os.path.join('..', 'data', 'temp_step4.json')

# Đọc file JSON từ Step 3
with open(input_path, 'r', encoding='utf-8') as file:
    step3_data = json.load(file)

# Chuyển đổi dữ liệu (giữ nguyên cấu trúc, chỉ thêm ObjectId tạm thời)
transformed_data = {
    **step3_data['propertyforsale'],
    "agencyid": "TEMP_AGENCY_ID",
    "agentid": ["TEMP_AGENT1_ID", "TEMP_AGENT2_ID"],
    "imageid": [f"TEMP_IMAGE_{i}" for i in range(len(step3_data['images']))],
    "schoolid": [f"TEMP_SCHOOL_{i}" for i in range(len(step3_data['schools']))]
}

# Lưu dữ liệu tạm thời vào file JSON
with open(temp_output_path, 'w', encoding='utf-8') as file:
    json.dump(transformed_data, file, indent=4)

print("Dữ liệu đã được chuyển đổi và lưu vào step4_final.json")