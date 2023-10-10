from flask import Flask, request, jsonify
from flask_cors import CORS
import pywifi
from pywifi import const

app = Flask(__name__)
CORS(app)

def scan_wifi_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Pilih antarmuka Wi-Fi yang akan digunakan

    iface.scan()
    scan_results = iface.scan_results()
    
    wifi_networks = []
    for result in scan_results:
        wifi_info = {
            'ssid': result.ssid,
            'security': get_security_type(result),
            'wps': get_wps_status(result),
        }
        wifi_networks.append(wifi_info)

    return wifi_networks

def get_security_type(scan_result):
    if scan_result.akm[0] == const.AKM_TYPE_NONE:
        return 'Open'
    elif scan_result.akm[0] == const.AKM_TYPE_WPA2PSK:
        return 'WPA2-PSK'
    elif scan_result.akm[0] == const.AKM_TYPE_WPAPSK:
        return 'WPA-PSK'
    else:
        return 'Unknown'
    
def get_wps_status(scan_result):
    if scan_result.akm[0] == const.AKM_TYPE_WPA2PSK:
        return 'Aktif'
    else:
        return 'Nonaktif'

@app.route('/api/wifi/security', methods=['GET'])
def get_wifi_security():
    try:
        wifi_networks = scan_wifi_networks()
        return jsonify({'wifi_networks': wifi_networks})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)