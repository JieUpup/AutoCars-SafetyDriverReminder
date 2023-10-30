class DecisionEngine:
    def __init__(self):
        pass

    def process_data(self, fused_data):
        """Processes fused sensor data and returns decisions."""
        decisions = []

        decisions.extend(self._process_camera_data(fused_data['camera']))
        decisions.extend(self._process_radar_data(fused_data['radar']))

        # Extend this method to include other sensors' data (LIDAR, GPS, etc.)

        return decisions

    def _process_camera_data(self, camera_data):
        """Processes camera data and returns decisions."""
        decisions = []
        if camera_data['object_detected']:
            distance = camera_data['distance']
            object_type = camera_data['object_type']

            if object_type == "car":
                if distance < 10:
                    decisions.append("warn_collision_imminent")
                elif distance < 20:
                    decisions.append("warn_collision_possible")
            elif object_type == "pedestrian" and distance < 10:
                decisions.append("warn_pedestrian_near")

        return decisions

    def _process_radar_data(self, radar_data):
        """Processes radar data and returns decisions."""
        decisions = []
        if radar_data['object_speed'] > 70:  # just a random threshold
            decisions.append("warn_high_speed_vehicle_nearby")

        return decisions


def mockup_sensor_data():
    """Generates mockup sensor data for testing."""
    return {
        "camera": {
            "object_detected": True,
            "object_type": "car",
            "distance": 15
        },
        "lidar": {
            "object_detected": True,
            "distance": 20,
            "direction": "left"
        },
        "radar": {
            "object_speed": 75,
            "distance": 30
        },
        "gps": {
            "latitude": 40.730610,
            "longitude": -73.935242
        }
    }


if __name__ == "__main__":
    fused_data = mockup_sensor_data()
    decision_engine = DecisionEngine()
    decisions = decision_engine.process_data(fused_data)
    print(decisions)  # ['warn_collision_possible', 'warn_high_speed_vehicle_nearby']
