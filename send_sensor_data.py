import requests
import datetime
import random
import time

# 🔗 This is Power BI Push URL
POWER_BI_URL = "https://api.powerbi.com/beta/d9d17d7a-f0f9-480c-8cb8-e162329aaa91/datasets/75d2300d-adcc-4ad6-a18c-20c63582a7e5/rows?experience=power-bi&key=wGyyLi9RmwrEgIramKCsvlccc3jg9kDH8euc%2BOYWp2wM7oYu25c1SJ6IjzMPobxgHlHbvzbpvGHJ%2FhoPzM734A%3D%3D"

# 🌡️ Function to simulate sensor data
def generate_sensor_data():
    return [{
        "timestamp": datetime.datetime.now().isoformat(),
        "temperature": round(random.uniform(22, 35), 2),
        "humidity": round(random.uniform(40, 90), 2),
        "light_level": round(random.uniform(0, 100), 1),
       "motion": "Detected" if random.random() > 0.5 else "None",
        "air_quality_index": random.randint(50, 150),
        "noise_level": round(random.uniform(30, 80), 1),

        "location": "Lab Room",

        # ✅ Static min/max for Gauge visual
        "min_light": 0,
        "max_light": 100
    }]

# 🔁 Loop to send data every 10 seconds
while True:
    data = generate_sensor_data()
    response = requests.post(POWER_BI_URL, json=data)

    if response.status_code == 200:
        print("✅ Sent:", data)
    else:
        print("❌ Error:", response.status_code, response.text)

    time.sleep(10)

