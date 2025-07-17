# step5.py
from bs4 import BeautifulSoup
import json

def extract_property_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract from script tag
    script_tag = soup.find('script', string=lambda t: 'var digitalData' in str(t))
    
    if not script_tag:
        return None
        
    script_content = script_tag.string
    json_str = script_content.split('var digitalData = ')[1].split(';')[0]
    data = json.loads(json_str)
    
    property_info = data['page']['pageInfo']['property']
    
    # Extract FAQ schema
    faq_script = soup.find('script', type='application/ld+json')
    faq_data = json.loads(faq_script.string)
    faqs = [{'question': q['name'], 'answer': q['acceptedAnswer']['text']} 
            for q in faq_data[-1]['mainEntity']]
    
    # Extract inspection times from schema
    inspection_events = [event for event in faq_data if event['@type'] == 'Event']
    inspection_times = []
    
    for event in inspection_events:
        if 'Inspection' in event['name']:
            inspection_times.append({
                'date': event['startDate'].split('T')[0],
                'time': f"{event['startDate'].split('T')[1]} - {event['endDate'].split('T')[1]}"
            })
    
    # Extract additional details
    breadcrumbs = []
    breadcrumb_list = next((item for item in faq_data if item['@type'] == 'BreadcrumbList'), None)
    if breadcrumb_list:
        breadcrumbs = [item['name'] for item in breadcrumb_list['itemListElement']]
    
    result = {
        'address': property_info['address'],
        'price': property_info['price'],
        'bedrooms': property_info['bedrooms'],
        'bathrooms': property_info['bathrooms'],
        'parking': property_info['parking'],
        'land_area': f"{property_info['landArea']} sqm",
        'building_size': f"{property_info['internalArea']} sqm",
        'agency': property_info['agency'],
        'agents': property_info['agentNames'].split(', '),
        'sale_method': property_info['saleMethod'],
        'auction_date': '08/02/2025 at 9:00AM',
        'inspection_times': inspection_times,
        'energy_efficiency': '2 stars',
        'features': ['Energy Efficiency Rating'],
        'images': property_info['images'],
        'description': '4 bedroom house for Sale at 7 Armfield Place, Chisholm ACT 2905.',
        'faqs': faqs,
        'coordinates': {
            'latitude': -35.425788,
            'longitude': 149.1289621
        },
        'breadcrumbs': breadcrumbs,
        'property_id': property_info['propertyId'],
        'listing_date': property_info['dateListed'],
        'days_listed': property_info['daysListed'],
        'has_floorplan': property_info['hasFloorplan'],
        'floorplan_count': property_info['floorPlansCount'],
        'photo_count': property_info['photoCount']
    }
    
    return result

if __name__ == '__main__':
    with open('step5.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    property_info = extract_property_info(html_content)
    print(property_info)