import pandas as pd
import random
from datetime import datetime, timedelta

# Number of events/readings
N = 1000

# Start date for the dummy dataset
start_date = datetime(2023, 1, 1, 0, 0, 0)

# List to store the dummy data
data = []

for i in range(N):
    event_date = start_date + timedelta(seconds=i * 10)  # 10 seconds interval
    camera_data = {
        "object_detected": random.choice([True, False]),
        "object_type": random.choice(["car", "pedestrian", "sign", "none"]),
        "distance_camera": random.uniform(5, 50)
    }
    lidar_data = {
        "object_detected_lidar": random.choice([True, False]),
        "distance_lidar": random.uniform(5, 50),
        "direction": random.choice(["left", "right", "front", "rear"])
    }
    radar_data = {
        "object_speed": random.uniform(0, 100),
        "distance_radar": random.uniform(5, 50)
    }
    gps_data = {
        "latitude": random.uniform(-90, 90),
        "longitude": random.uniform(-180, 180)
    }

    # Combining all data
    combined_data = {
        "timestamp": event_date,
        **camera_data,
        **lidar_data,
        **radar_data,
        **gps_data
    }

    data.append(combined_data)

# Creating a DataFrame and saving to CSV
df = pd.DataFrame(data)
df.to_csv('sensor_data.csv', index=False)
