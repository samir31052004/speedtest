import speedtest
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Create a Speedtest object
    st = speedtest.Speedtest()
    st.get_best_server()

    # Perform download and upload tests
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping
    server_info = st.results.server
    client_info = st.results.client
    share_url = st.results.share()
    # Prepare the results
    results = {
        
        'Download_Speed': f"{download_speed:.2f} Mbps",
        'Upload_Speed': f"{upload_speed:.2f} Mbps",
        'Ping': f"{ping:.2f} ms",
        'S_Name': f"{server_info['name']}",
        'S_Country': f"{server_info['country']}",
        'S_Location': f"{server_info['host']}",
        'S_Latency': f"{server_info['latency']} ms",
        'C_IP_Address': f"{client_info['ip']}",
        'C_ISP': f"{client_info['isp']}",
        'C_Country': f"{client_info['country']}",
        'C_Timestamp': f"{st.results.timestamp}",
        'Img_Url':share_url
    }

    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
