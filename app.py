from flask import Flask, request, jsonify
import my_cpp_module
import logging

app = Flask(__name__)
sensor_data = my_cpp_module.SensorData()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/register_one', methods=['POST'])
def register_one():
    """
    Endpoint to register a single sensor reading.
    Expects a JSON payload with timestamp, type_of_sensor, and read.
    """
    try:
        data = request.json
        timestamp = data['timestamp']
        sensor_type = data['type_of_sensor']
        read = data['read']
        # Log the received data
        logging.debug(f"register_one called with: timestamp={timestamp}, sensor_type={sensor_type}, read={read}")
        sensor_data.register_one(timestamp, sensor_type, read)
        return jsonify({'result': 'OK'})
    except Exception as e:
        app.logger.error(f"Error in register_one: {e}")
        return jsonify({'result': 'error', 'message': str(e)}), 500

@app.route('/register_many', methods=['POST'])
def register_many():
    """
    Endpoint to register multiple sensor readings at once.
    Expects a JSON payload with a list of readings, each containing timestamp, type_of_sensor, and read.
    """
    try:
        data = request.json
        readings = [(r['timestamp'], r['type_of_sensor'], r['read']) for r in data['readings']]
        # Log the received data
        logging.debug(f"register_many called with: readings={readings}")
        sensor_data.register_many(readings)
        return jsonify({'result': 'OK'})
    except Exception as e:
        app.logger.error(f"Error in register_many: {e}")
        return jsonify({'result': 'error', 'message': str(e)}), 500

@app.route('/highest_accumulated', methods=['GET'])
def highest_accumulated():
    """
    Endpoint to get the highest accumulated value for a specific sensor type.
    Expects a query parameter 'type_of_sensor'.
    """
    try:
        sensor_type = request.args.get('type_of_sensor')
        # Log the received data
        logging.debug(f"highest_accumulated called with: sensor_type={sensor_type}")
        result = sensor_data.highest_accumulated(sensor_type)
        # Log the result
        logging.debug(f"highest_accumulated result: {result}")
        return result  # Return the result as a JSON string
    except Exception as e:
        app.logger.error(f"Error in highest_accumulated: {e}")
        return jsonify({'result': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
