import functions_framework
from google.cloud import bigquery
from datetime import datetime
import json
import logging

# --- CONFIGURATION ---
PROJECT_ID = "cpc357-project-481709" 
DATASET_ID = "sensor_data"
TABLE_ID = "readings"
SECRET_API_KEY = "AIzaSyDTGtnietNjMMlcm4GsPjQ56S6l19WzVwQ"

# THRESHOLDS
TEMP_CRITICAL = 33.0    # RED ALERT - overheating
HUMID_WARNING_MIN = 15.0 # Below - Static Electricity Risk
HUMID_WARNING_MAX = 60.0 # Above 60% - Rust/Short Circuit Risk

client = bigquery.Client(project=PROJECT_ID)

@functions_framework.http
def ingest_sensor_data(request):
    # 1. Setup Data
    try:
        request_json = request.get_json(silent=True)
        if not request_json:
            return (json.dumps({"error": "No JSON"}), 400)
    except Exception as e:
        return (json.dumps({"error": str(e)}), 400)

    # 2. Security Check
    sent_key = request_json.get("api_key")
    if sent_key != SECRET_API_KEY:
        print(json.dumps({"severity": "WARNING", "message": f"Security Breach: Invalid Key {sent_key}"}))
        return (json.dumps({"error": "Unauthorized"}), 401)

    # 3. Extract Data
    device_id = request_json.get("device_id")
    temp = request_json.get("temperature")
    humid = request_json.get("humidity")

    # --- CODE-BASED ALERTS (LOGGING) ---
    # This prints special JSON that makes Google Cloud Console turn RED 🔴
    alert_status = "NORMAL"
    
    if temp is not None:
        t_val = float(temp)
        if t_val > TEMP_CRITICAL:
            alert_status = "CRITICAL_TEMP"
            # 🔴 SEVERITY: ERROR (Shows up Red in Dashboard)
            print(json.dumps({
                "severity": "ERROR",
                "message": f"🚨 OVERHEATING RISK: {t_val}C is above limit!",
                "device_id": device_id
            }))

    if humid is not None:
        h_val = float(humid)
        if h_val > HUMID_WARNING_MAX:
            # Too Wet
            # 🟡 SEVERITY: WARNING (Shows up Yellow in Dashboard)
            print(json.dumps({
                "severity": "WARNING",
                "message": f"⚠️ HIGH HUMIDITY: {h_val}% detected.",
                "device_id": device_id
            }))
        elif h_val < HUMID_WARNING_MIN:
            # Too Dry
            print(json.dumps({
                "severity": "WARNING",
                "message": f"⚡ LOW HUMIDITY: {h_val}% < 15%",
                "device_id": device_id
            }))
    # -----------------------------------

    # 4. Insert into BigQuery
    rows_to_insert = [{
        "device_id": device_id,
        "temperature": temp,
        "humidity": humid,
        "timestamp": datetime.utcnow().isoformat()
    }]

    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    errors = client.insert_rows_json(table_ref, rows_to_insert)

    if errors == []:
        # Send a response back to Arduino telling it if there is an alert
        return (json.dumps({"status": "success", "alert": alert_status}), 200)
    else:
        print(json.dumps({"severity": "ERROR", "message": f"Database Fail: {errors}"}))
        return (json.dumps({"error": str(errors)}), 500)