from prometheus_client import start_http_server, Gauge
import time
import requests

print("[LOG] Starting Radic Promeheus Exporter")

prom_User = Gauge('radic_user_count', 'Users that are currently online with Radic')
pron_License = Gauge('radic_license_count', 'Licenes that are currently in the DB')

def process_request(t):
    userOnlineResponse = requests.get('https://radicmenu.xyz/api/v1/heartbeat/useronline')
    prom_User.set(userOnlineResponse.text)  

    licensesResponse = requests.get('https://radicmenu.xyz/api/v1/launcher/licenses')
    pron_License.set(licensesResponse.text)

    time.sleep(t)

if __name__ == '__main__':
    print("[LOG] Starting Radic Promeheus HTTP Server")
    start_http_server(8000)
    print("[LOG] Started Radic Promeheus HTTP Server")

    while True:
        process_request(10)
