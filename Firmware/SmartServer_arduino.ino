#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "DHT.h"

// ================= USER CONFIGURATION =================
const char* ssid     = "Galaxy A33 5GF06F";         // <--- CHANGE THIS
const char* password = "vywa6030";     // <--- CHANGE THIS

// Paste your Webhook.site URL here for testing:
const char* serverName = "https://ingest-data-1054456615434.us-central1.run.app"; 

const char* apiKey = "AIzaSyDTGtnietNjMMlcm4GsPjQ56S6l19WzVwQ"; // Matches the Cloud Function later
#define DHTPIN 4
#define DHTTYPE DHT11
// ======================================================

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
  
  // 1. Connect to Wi-Fi
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  
  // Wait for connection
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected! IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Wait 10 seconds between posts
  delay(10000);

  // 2. Read Data
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // 3. Prepare JSON (The format agreed with Role B)
  StaticJsonDocument<200> doc;
  doc["device_id"] = "sensor_01";
  doc["temperature"] = t;
  doc["humidity"] = h;
  doc["api_key"] = apiKey;

  String jsonOutput;
  serializeJson(doc, jsonOutput);

  // 4. Send to Internet
  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");
    
    int httpResponseCode = http.POST(jsonOutput);
    
    Serial.print("Sending Data: ");
    Serial.println(jsonOutput);
    Serial.print("Response Code: ");
    Serial.println(httpResponseCode); // 200 means success
    
    http.end();
  }
  else {
    Serial.println("WiFi Disconnected");
  }
}