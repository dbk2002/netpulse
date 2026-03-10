# NetPulse – Network Monitoring Dashboard

NetPulse is a lightweight network monitoring dashboard built using Python and Streamlit.  
It monitors connectivity, DNS resolution, and latency of multiple devices in real time.

## Features

- Monitor multiple network devices
- Online / Offline status detection
- DNS resolution for each device
- Latency measurement using ping
- Interactive dashboard UI
- Device status cards with visual indicators
- Network latency visualization
- Downloadable monitoring report (CSV)

## Tech Stack

- Python
- Streamlit
- Pandas
- Socket
- Subprocess

## Project Structure
```
netpulse-dashboard
│
├── app.py # Main dashboard application
├── devices.txt # List of devices/domains to monitor
├── netpulse_logo.png # Project logo
└── README.md # Project documentation
```

## ⚙️ Installation
### 1️⃣ Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/netpulse-dashboard.git
```

### 2️⃣ Navigate to the Project Folder
```
cd netpulse-dashboard
```

### 3️⃣ Install Required Dependencies
```
pip install streamlit pandas
```

### 4️⃣ Run the Application
```
streamlit run app.py
```

### Then open in your browser:
```
http://localhost:8501
```

----------------------------------------

## 📡 Usage

1. Add devices or domains in the **devices.txt** file.

Example:
google.com
github.com
8.8.8.8
cloudflare.com


2. Run the dashboard using Streamlit.

3. The system will:

- Check device connectivity
- Resolve IP addresses
- Measure latency
- Display online/offline status

4. Use the **Download Report** button to export monitoring results.

---

## 📊 Dashboard Overview

The NetPulse dashboard provides:

- Network overview metrics
- Device status cards
- Detailed device status table
- Network latency graph
- Monitoring controls

---

## 🎯 Use Case

This project demonstrates:

- Basic **network monitoring concepts**
- **real-time data visualization**
- building dashboards using **Streamlit**
- using Python for **network diagnostics**

It can serve as a **foundation for more advanced monitoring systems**.

---

## 👨‍💻 Author

**Dhanush B K**

---

## ⭐ Future Improvements

- Real-time auto-refresh monitoring
- Network topology visualization
- Historical latency tracking
- Email or alert notifications for device downtime
