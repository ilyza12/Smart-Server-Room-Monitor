# CloudSense: Serverless IoT Server Room Monitoring System

**CloudSense** is a cloud-native IoT solution designed to monitor critical environmental conditions (temperature and humidity) in server rooms. It leverages the ESP32 microcontroller and Google Cloud Platform (GCP) to provide real-time telemetry, serverless data ingestion, and historical analytics.

---

## 📖 Project Overview
* **Objective:** Prevent server hardware failure by tracking compliance with ASHRAE thermal and humidity guidelines.
* **Architecture:** The ESP32 collects sensor data and transmits it via secure HTTP to a serverless Google Cloud Function. Data is warehoused in BigQuery and visualized on a Looker Studio dashboard.

## 🚀 Key Features
* **Real-Time Monitoring:** Updates temperature and humidity readings every 10 seconds.
* **Serverless Backend:** Uses Google Cloud Functions (Python) for "NoOps" scalability and cost efficiency.
* **Secure Transmission:** All data is encrypted using HTTPS.
* **Data Warehousing:** Persistent storage in Google BigQuery for long-term trend analysis.
* **Visualization:** Interactive dashboards using Looker Studio.

## 🛠️ Tech Stack
* **Hardware:** ESP32-WROOM-32, DHT11 Sensor.
* **Firmware:** C++ (Arduino IDE).
* **Cloud Services:** Google Cloud Functions, BigQuery, Looker Studio.
* **Communication:** HTTP (REST API), JSON.

---

## 🔌 Hardware Configuration
| Component | Description |
| :--- | :--- |
| **Microcontroller** | ESP32 Development Board (30-pin) |
| **Sensor** | DHT11 Temperature & Humidity Module |
| **Power** | Micro-USB Cable (5V) |
| **Connectivity** | 2.4 GHz Wi-Fi Network |

---

## 📡 API Reference
The ESP32 communicates with the Cloud Function via HTTP POST.

**Endpoint:** `https://[YOUR_REGION]-[PROJECT_ID].cloudfunctions.net/ingest-data`

**Payload Schema (JSON):**
```json
{
  "device_id": "sensor_01",
  "temperature": 30.2,
  "humidity": 54.0,
  "api_key": "YourSuperSecretKey"
}
```
---

## ⚙️ Setup & Installation

### ☁️ Phase 1: Google Cloud Platform (Backend)
1.  **BigQuery Setup:**
    * Create a dataset named `sensor_data`.
    * Create a table named `readings` with the schema:
        * `device_id` (STRING)
        * `temperature` (FLOAT)
        * `humidity` (FLOAT)
        * `timestamp` (TIMESTAMP)
2.  **Cloud Function Deployment:**
    * Navigate to **Cloud Run Functions** and create a function named `ingest-data`.
    * **Runtime:** Python 3.x
    * **Entry Point:** `ingest_sensor_data`
    * **Source Code:** Upload the files from the `backend/` folder.
    * **Environment Variables:** Ensure you set `PROJECT_ID`, `DATASET_ID`, and `TABLE_ID` in the `main.py` file.

### 🔌 Phase 2: Firmware (ESP32)
1.  **Prerequisites:** Install [Arduino IDE](https://www.arduino.cc/en/software).
2.  **Board Manager:** Add the Espressif URL to preferences and install the `esp32` board package.
    * *Select Board:* `DOIT ESP32 DEVKIT V1`
3.  **Library Installation:** Install the following via Library Manager:
    * `DHT sensor library` by Adafruit (v1.4.6)
    * `ArduinoJson` by Benoit Blanchon (v7.x)
4.  **Configuration:**
    * Open `SmartServer_arduino.ino`.
    * Update the `ssid`, `password`, and `serverName` (your Cloud Function URL).
    * Insert your `apiKey`.
5.  **Flash:** Connect ESP32 via USB (check COM port) and click Upload.

---

## Members:
1. Shereen Ilyza Binti Sheik Mujibu Rahman (164718)
2. Sabrina Binti Sofian (164740)
