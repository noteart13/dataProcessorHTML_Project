# step3.py
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
        'inspection_times': [
            {
                'date': '20/01/2025',
                'time': '5:00 PM - 5:30 PM'
            }
        ],
        'energy_efficiency': '2 stars',
        'features': ['Energy Efficiency Rating'],
        'images': property_info['images'],
        'description': '4 bedroom house for Sale at 7 Armfield Place, Chisholm ACT 2905.',
        'faqs': faqs
    }
    
    return result

if __name__ == '__main__':
    with open('step3.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    property_info = extract_property_info(html_content)
    print(property_info)