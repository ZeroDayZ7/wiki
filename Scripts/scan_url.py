import requests
import time

API_KEY = '3ce446a719cfe68b92564dc920e359020ae52a338fafa7d3e58852ffa7cd2e41'
url_to_scan = 'https://kreatywne.ai/wp-content/cache/min/1/wp-content/themes/salient/css/build/grid-system.css?ver=1753647088'
api_url = 'https://www.virustotal.com/api/v3/urls'

data = {'url': url_to_scan}
headers = {'x-apikey': API_KEY}

response = requests.post(api_url, data=data, headers=headers)

if response.status_code == 200:
    json_response = response.json()
    scan_id = json_response['data']['id']
    print('✅ URL przesłany do skanowania.')
    print('ID skanowania:', scan_id)

    # Czekamy 10 sekund, potem pobieramy raport
    time.sleep(10)
    report_url = f'https://www.virustotal.com/api/v3/analyses/{scan_id}'
    report_response = requests.get(report_url, headers=headers)

    if report_response.status_code == 200:
        analysis = report_response.json()
        stats = analysis['data']['attributes']['stats']
        print('\n🔍 Wyniki skanu:')
        print('Malicious  :', stats['malicious'])
        print('Suspicious :', stats['suspicious'])
        print('Harmless   :', stats['harmless'])
        print('Undetected :', stats['undetected'])
    else:
        print('❌ Błąd przy pobieraniu raportu:', report_response.status_code)
else:
    print('❌ Błąd:', response.status_code, response.text)
