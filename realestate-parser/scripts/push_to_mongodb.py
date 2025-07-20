import json
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

# Đường dẫn tới file đầu vào và đầu ra
temp_input_path = os.path.join('..', 'data', 'temp_step4.json')
output_path = os.path.join('..', 'data', 'step4_finaljson')

# Kết nối với MongoDB
try:
    client = MongoClient('mongodb+srv://khoilh7705:0333503352Lhk%40@khoilh7705.xdst8xm.mongodb.net/')
    db = client['real_estate_db']
    properties_collection = db['properties']
    agencies_collection = db['agencies']
    agents_collection = db['agents']
    images_collection = db['images']
    schools_collection = db['schools']
except Exception as e:
    print(f"Không thể kết nối với MongoDB: {e}")
    exit()

# Đọc file JSON từ Step 4 tạm thời
try:
    with open(temp_input_path, 'r', encoding='utf-8') as file:
        temp_data = json.load(file)
except FileNotFoundError:
    print(f"Không tìm thấy file {temp_input_path}")
    exit()
except json.JSONDecodeError:
    print(f"Lỗi khi phân tích cú pháp file {temp_input_path}")
    exit()

# Thêm agency vào collection agencies
agency_id = ObjectId()
agency_data = {
    "agencyId": temp_data.get('agencyid', 'TEMP_AGENCY_ID'),
    "name": "Luton Properties Tuggeranong",
    "contactDetails": "02 61763448",
    "isArchived": False,
    "logo": "https://rimh2.domainstatic.com.au/KatbtKOyhgAN9pZ3GvSBFhJ3W68=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/Agencys/10312/searchlogo_10312.jpeg?date=638728801327769249",
    "banner": "https://rimh2.domainstatic.com.au/O79poanDssL4f_qNu4mM_ar9W9U=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/Agencys/10312/banner_10312.jpeg?date=638728801327769237",
    "logoSmall": "https://rimh2.domainstatic.com.au/KatbtKOyhgAN9pZ3GvSBFhJ3W68=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/Agencys/10312/searchlogo_10312.jpeg?date=638728801327769249",
    "profileUrl": "lutonpropertiestuggeranong-10312",
    "website": "http://www.luton.com.au/",
    "_id": agency_id
}
agencies_collection.insert_one(agency_data)

# Thêm agents vào collection agents
agent_ids = []
agent_data_list = [
    {
        "agentId": "1884714",
        "email": "kelsey.tracey@luton.com.au",
        "firstName": "Kelsey",
        "lastName": "Tracey",
        "phoneNumber": "0414 422 824",
        "isActiveProfilePage": True,
        "photo": "https://rimh2.domainstatic.com.au/VMjcup7r19YmwYavOHejaAXkS_U=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/10312/contact_1884714.jpeg?date=638727332779100000",
        "profileUrl": "https://www.domain.com.au/real-estate-agent/kelsey-tracey-1884714"
    },
    {
        "agentId": "1541777",
        "email": "michael.martin@luton.com.au",
        "firstName": "Michael",
        "lastName": "Martin",
        "phoneNumber": "0411748805",
        "isActiveProfilePage": True,
        "photo": "https://rimh2.domainstatic.com.au/0_a4UNChiY6gmw8FpVsBanqeHqQ=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/10312/contact_1894318.jpeg?date=638728004242500000",
        "profileUrl": "https://www.domain.com.au/real-estate-agent/michael-martin-1541777"
    }
]
for agent in agent_data_list:
    agent_id = ObjectId()
    agents_collection.insert_one({**agent, "_id": agent_id})
    agent_ids.append(agent_id)

# Thêm images vào collection images
image_ids = []
for image in temp_data.get('images', []):
    image_id = ObjectId()
    images_collection.insert_one({**image, "_id": image_id})
    image_ids.append(image_id)

# Thêm schools vào collection schools
school_ids = []
for school in temp_data.get('schools', []):
    school_id = ObjectId()
    schools_collection.insert_one({**school, "_id": school_id})
    school_ids.append(school_id)

# Chuyển đổi dữ liệu sang định dạng cuối cùng
final_data = {
    **{k: v for k, v in temp_data.items() if k not in ['agencyid', 'agentid', 'imageid', 'schoolid']},
    'agencyid': agency_id,
    'agentid': agent_ids,
    'imageid': image_ids,
    'schoolid': school_ids
}

# Lưu dữ liệu vào collection properties
properties_collection.insert_one(final_data)

# Lưu dữ liệu vào file JSON cuối cùng
with open(output_path, 'w', encoding='utf-8') as file:
    final_data_serializable = final_data.copy()
    final_data_serializable['agencyid'] = str(final_data['agencyid'])
    final_data_serializable['agentid'] = [str(id) for id in final_data['agentid']]
    final_data_serializable['imageid'] = [str(id) for id in final_data['imageid']]
    final_data_serializable['schoolid'] = [str(id) for id in final_data['schoolid']]
    json.dump(final_data_serializable, file, indent=4)

print(f"Dữ liệu đã được đẩy vào MongoDB và lưu vào {output_path} tại {05:57 PM +07, July 20, 2025}")