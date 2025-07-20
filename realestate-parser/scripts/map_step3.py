import json
import os

# Đường dẫn tới file đầu vào và đầu ra
input_path = os.path.join('..', 'data', 'step2_metajson')
output_path = os.path.join('..', 'data', 'step3_mappedjson')

# Đọc file JSON từ Step 2
with open(input_path, 'r', encoding='utf-8') as file:
    step2_data = json.load(file)

# Ánh xạ dữ liệu sang định dạng Step 3
mapped_data = {
    "agency": {
        "agencyId": step2_data["agencyId"],
        "name": step2_data["agency"],
        "contactDetails": "02 61763448",
        "isArchived": False,
        "logo": "https://rimh2.domainstatic.com.au/KatbtKOyhgAN9pZ3GvSBFhJ3W68=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/Agencys/10312/searchlogo_10312.jpeg?date=638728801327769249",
        "banner": "https://rimh2.domainstatic.com.au/O79poanDssL4f_qNu4mM_ar9W9U=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/Agencys/10312/banner_10312.jpeg?date=638728801327769237",
        "logoSmall": "https://rimh2.domainstatic.com.au/KatbtKOyhgAN9pZ3GvSBFhJ3W68=/filters:format(png):quality(80):no_upscale()/https://images.domain.com.au/img/Agencys/10312/searchlogo_10312.jpeg?date=638728801327769249",
        "profileUrl": "lutonpropertiestuggeranong-10312",
        "website": "http://www.luton.com.au/"
    },
    "agents": [
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
    ],
    "images": [{"category": "kitchen", "star": False, "url": img} for img in step2_data["images"]],
    "propertyforsale": {
        "architecturalStyle": "None",
        "area": {"totalarea": step2_data["landArea"], "unit": "sqM"},
        "bath": step2_data["bathrooms"],
        "bed": step2_data["bedrooms"],
        "city": "Unincorporated Act",
        "constructionYear": "N/A",
        "contactInfo": [
            {"email": "kelsey.tracey@luton.com.au", "firstName": "Kelsey", "lastName": "Tracey", "phoneNumber": "0414 422 824"},
            {"email": "michael.martin@luton.com.au", "firstName": "Michael", "lastName": "Martin", "phoneNumber": "0411748805"}
        ],
        "coordinates": {"lat": -35.425788, "lng": 149.1289621},
        "description": "",  # Cần lấy từ HTML nếu có
        "expectedPrice": None,
        "features": {
            "appliances": ["None"],
            "basement": "None",
            "buildingAmenities": ["None"],
            "coolingTypes": ["None"],
            "displayAddress": "fullAddress",
            "floorCovering": ["None"],
            "floorno": 1,
            "garage": step2_data["parking"],
            "heatingFuels": ["None"],
            "heatingTypes": ["None"],
            "indoorFeatures": ["None"],
            "outdoorAmenities": ["None"],
            "parking": ["Carport"],
            "roof": ["Other"],
            "rooms": ["None"],
            "view": ["None"]
        },
        "historySale": {"agencyId": step2_data["agencyId"], "soldDate": None, "soldPrice": None},
        "images": [{"category": "kitchen", "star": False, "url": img} for img in step2_data["images"]],
        "listingOption": "sale",
        "postcode": step2_data["postcode"],
        "pricing": {
            "authority": "for-sale",
            "councilBill": "",
            "priceIncludes": [""],
            "pricingOptions": step2_data["price"],
            "waterBillPeriod": "monthly"
        },
        "propertyType": step2_data["primaryPropertyType"],
        "published": False,
        "recommended": False,
        "slug": f"{step2_data['address'].replace(', ', '-').lower()}-{step2_data['propertyId']}",
        "stakeHolder": "agent",
        "state": step2_data["state"],
        "status": "for-sale",
        "street": step2_data["address"],
        "structuralRemodelYear": "N/A",
        "suburb": step2_data["suburb"],
        "title": "Character, Charm, Elevation",
        "url": f"https://www.domain.com.au/{step2_data['address'].replace(', ', '-').lower()}-{step2_data['propertyId']}"
    },
    "schools": [
        {
            "address": "Chisholm, ACT 2905",
            "distance": 1052.867250356091,
            "domainSeoUrlSlug": "caroline-chisholm-school-junior-campus-act-2905-50223",
            "educationLevel": "primary",
            "gender": "",
            "name": "Caroline Chisholm School - Junior Campus",
            "postCode": "2905",
            "state": "ACT",
            "status": "Open",
            "type": "Government",
            "url": "",
            "year": ""
        },
        # Thêm các trường khác tương tự
    ]
}

# Lưu dữ liệu vào file JSON
with open(output_path, 'w', encoding='utf-8') as file:
    json.dump(mapped_data, file, indent=4)

print("Dữ liệu đã được ánh xạ và lưu vào step3_mapped.json")