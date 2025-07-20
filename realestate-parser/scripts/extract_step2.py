from bs4 import BeautifulSoup
import json
import re
import os

# Đường dẫn tới file HTML
html_path = os.path.join('..', 'data', 'step1.html')
output_path = os.path.join('..', 'data', 'step2_metajson')

# Đọc file HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Phân tích HTML bằng BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Tìm biến digitalData trong thẻ <script>
script_tags = soup.find_all('script')
digital_data = None
for script in script_tags:
    if 'var digitalData =' in script.text:
        json_str = re.search(r'var digitalData = ({.*?});', script.text, re.DOTALL)
        if json_str:
            digital_data = json.loads(json_str.group(1))
            break

if not digital_data:
    print("Không tìm thấy digitalData trong HTML")
    exit()

# Trích xuất dữ liệu cần thiết từ digitalData
property_data = {
    "address": digital_data['page']['pageInfo']['property']['address'],
    "bedrooms": digital_data['page']['pageInfo']['property']['bedrooms'],
    "bathrooms": digital_data['page']['pageInfo']['property']['bathrooms'],
    "parking": digital_data['page']['pageInfo']['property']['parking'],
    "internalArea": digital_data['page']['pageInfo']['property']['internalArea'],
    "landArea": digital_data['page']['pageInfo']['property']['landArea'],
    "price": digital_data['page']['pageInfo']['property']['price'],
    "saleMethod": digital_data['page']['pageInfo']['property']['saleMethod'],
    "agency": digital_data['page']['pageInfo']['property']['agency'],
    "agencyId": digital_data['page']['pageInfo']['property']['agencyId'],
    "agentNames": digital_data['page']['pageInfo']['property']['agentNames'],
    "images": digital_data['page']['pageInfo']['property']['images'],
    "photoCount": digital_data['page']['pageInfo']['property']['photoCount'],
    "floorPlansCount": digital_data['page']['pageInfo']['property']['floorPlansCount'],
    "hasFloorplan": digital_data['page']['pageInfo']['property']['hasFloorplan'],
    "hasPhoto": digital_data['page']['pageInfo']['property']['hasPhoto'],
    "hasDescription": digital_data['page']['pageInfo']['property']['hasDescription'],
    "descriptionHasPhone": digital_data['page']['pageInfo']['property']['descriptionHasPhone'],
    "descriptionHasEmail": digital_data['page']['pageInfo']['property']['descriptionHasEmail'],
    "postcode": digital_data['page']['pageInfo']['property']['postcode'],
    "state": digital_data['page']['pageInfo']['property']['state'],
    "suburb": digital_data['page']['pageInfo']['property']['suburb'],
    "primaryPropertyType": digital_data['page']['pageInfo']['property']['primaryPropertyType'],
    "secondaryPropertyType": digital_data['page']['pageInfo']['property']['secondaryPropertyType'],
    "propertyId": digital_data['page']['pageInfo']['property']['propertyId'],
    "structuredFeatures": digital_data['page']['pageInfo']['property']['structuredFeatures'],
    "nbnDetails": digital_data['page']['pageInfo']['nbnDetails'],
    "dateListed": digital_data['page']['pageInfo']['property']['dateListed'],
    "daysListed": digital_data['page']['pageInfo']['property']['daysListed'],
    "inspectionsCount": digital_data['page']['pageInfo']['property']['inspectionsCount'],
    "onlineAuctionAvailable": digital_data['page']['pageInfo']['property']['onlineAuctionAvailable'],
    "videoCount": digital_data['page']['pageInfo']['property']['videoCount'],
    "virtualTour": digital_data['page']['pageInfo']['property']['virtualTour']
}

# Lưu dữ liệu vào file JSON
with open(output_path, 'w', encoding='utf-8') as file:
    json.dump(property_data, file, indent=4)

print("Dữ liệu đã được trích xuất và lưu vào step2_meta.json")