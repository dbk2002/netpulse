import streamlit as st
import subprocess
import socket
import pandas as pd
import time

# Page config
st.set_page_config(page_title="NetPulse Network Monitor", layout="wide")

# Custom CSS
st.markdown("""
<style>

body {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
}

.device-card {
    padding: 15px;
    border-radius: 8px;
    margin-bottom: 10px;
    font-weight: bold;
}

.online {
    background-color: #2ecc71;
    color: white;
}

.offline {
    background-color: #e74c3c;
    color: white;
}

.unknown {
    background-color: #f1c40f;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# Display Logo
st.image("netpulse_logo.png", width=400)

# Title
st.title("NetPulse Network Monitoring Dashboard")
st.write("Real-time monitoring of network connectivity and device availability")

# Load devices
def load_devices():
    try:
        with open("devices.txt") as f:
            return [line.strip() for line in f]
    except:
        return ["google.com", "github.com", "8.8.8.8"]

devices = load_devices()

# Sidebar
st.sidebar.title("Control Panel")

st.sidebar.write("### Devices Monitored")

for d in devices:
    st.sidebar.write(f"📡 {d}")

st.sidebar.write("---")
st.sidebar.write("NetPulse Monitoring System")

# Function to check device
def check_device(device):

    start = time.time()

    try:
        ip = socket.gethostbyname(device)

        response = subprocess.run(
            ["ping", "-n", "1", device],
            capture_output=True
        )

        latency = round((time.time() - start) * 1000, 2)

        if response.returncode == 0:
            status = "Online"
        else:
            status = "Offline"

    except:
        ip = "N/A"
        status = "Error"
        latency = None

    return {
        "Device": device,
        "IP Address": ip,
        "Status": status,
        "Latency (ms)": latency
    }

# Run monitoring
results = []

for device in devices:
    results.append(check_device(device))

df = pd.DataFrame(results)

# Metrics
total_devices = len(df)
online_devices = df[df["Status"] == "Online"].shape[0]
offline_devices = df[df["Status"] == "Offline"].shape[0]

st.subheader("Network Overview")

col1, col2, col3 = st.columns(3)

col1.metric("📡 Total Devices", total_devices)
col2.metric("🟢 Online Devices", online_devices)
col3.metric("🔴 Offline Devices", offline_devices)

# Status Cards
st.subheader("Device Status")

for index, row in df.iterrows():

    if row["Status"] == "Online":
        st.markdown(
            f'<div class="device-card online">🟢 {row["Device"]} — ONLINE</div>',
            unsafe_allow_html=True
        )

    elif row["Status"] == "Offline":
        st.markdown(
            f'<div class="device-card offline">🔴 {row["Device"]} — OFFLINE</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="device-card unknown">⚠️ {row["Device"]} — UNKNOWN</div>',
            unsafe_allow_html=True
        )

# Table
st.subheader("Detailed Status Table")

def highlight_status(val):

    if val == "Online":
        return "background-color:#2ecc71;color:white"

    elif val == "Offline":
        return "background-color:#e74c3c;color:white"

    else:
        return "background-color:#f1c40f;color:black"

st.dataframe(df.style.applymap(highlight_status, subset=["Status"]))

# Latency graph
st.subheader("Network Latency")

latency_df = df.copy()
latency_df["Latency (ms)"] = latency_df["Latency (ms)"].fillna(0)

st.bar_chart(latency_df.set_index("Device")["Latency (ms)"])

# Refresh button
st.subheader("Monitoring Controls")

if st.button("Refresh Monitoring"):
    st.rerun()

# Download report
csv = df.to_csv(index=False)

st.download_button(
    label="Download Monitoring Report",
    data=csv,
    file_name="network_status_report.csv",
    mime="text/csv"
)