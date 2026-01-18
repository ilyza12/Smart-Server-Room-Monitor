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

## Members:
1. Shereen Ilyza Binti Sheik Mujibu Rahman (164718)
2. Sabrina Binti Sofian (164740)
