import random


class Sensor:
    """Base class for all sensors."""

    def __init__(self):
        self.status = "operational"

    def is_operational(self):
        return self.status == "operational"

    def get_data(self):
        raise NotImplementedError


class CameraSensor(Sensor):

    def get_data(self):
        # Mockup function to simulate camera data
        return {
            "object_detected": random.choice([True, False]),
            "object_type": random.choice(["car", "pedestrian", "sign", "none"]),
            "distance": random.uniform(5, 50)
        }


class LidarSensor(Sensor):

    def get_data(self):
        # Mockup function to simulate LIDAR data
        return {
            "object_detected": random.choice([True, False]),
            "distance": random.uniform(5, 50),
            "direction": random.choice(["left", "right", "front", "rear"])
        }


class RadarSensor(Sensor):

    def get_data(self):
        # Mockup function to simulate RADAR data
        return {
            "object_speed": random.uniform(0, 100),
            "distance": random.uniform(5, 50)
        }


class GPSSensor(Sensor):

    def get_data(self):
        # Mockup function to simulate GPS data
        return {
            "latitude": random.uniform(-90, 90),
            "longitude": random.uniform(-180, 180)
        }


class SensorIntegrationModule:

    def __init__(self):
        self.cameras = CameraSensor()
        self.lidar = LidarSensor()
        self.radar = RadarSensor()
        self.gps = GPSSensor()

    def get_sensor_data(self):
        fused_data = {}

        if self.cameras.is_operational():
            fused_data["camera"] = self.cameras.get_data()

        if self.lidar.is_operational():
            fused_data["lidar"] = self.lidar.get_data()

        if self.radar.is_operational():
            fused_data["radar"] = self.radar.get_data()

        if self.gps.is_operational():
            fused_data["gps"] = self.gps.get_data()

        return fused_data


if __name__ == "__main__":
    sim = SensorIntegrationModule()
    fused_data = sim.get_sensor_data()
    print(fused_data)

