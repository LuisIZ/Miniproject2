import my_cpp_module

# Create an instance of SensorData
sensor_data = my_cpp_module.SensorData()

# Register a single reading
sensor_data.register_one(1, 'AIRQUALITY', 100.0)

# Print the highest accumulated value for AIRQUALITY
print(sensor_data.highest_accumulated('AIRQUALITY'))
