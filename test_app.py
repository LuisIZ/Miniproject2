import pytest
import requests

# Test registering a single reading for AIRQUALITY
def test_register_one_airquality():
    response = requests.post('http://localhost:5000/register_one', json={
        'timestamp': 1,
        'type_of_sensor': 'AIRQUALITY',
        'read': 100.0
    })
    assert response.json()['result'] == 'OK'

# Test registering a single reading for ULTRAVIOLETRADIATION
def test_register_one_uv():
    response = requests.post('http://localhost:5000/register_one', json={
        'timestamp': 1,
        'type_of_sensor': 'ULTRAVIOLETRADIATION',
        'read': 5.0
    })
    assert response.json()['result'] == 'OK'

# Test registering a single reading for TRAFFIC
def test_register_one_traffic():
    response = requests.post('http://localhost:5000/register_one', json={
        'timestamp': 1,
        'type_of_sensor': 'TRAFFIC',
        'read': 200.0
    })
    assert response.json()['result'] == 'OK'

# Test registering multiple readings for AIRQUALITY
def test_register_many_airquality():
    response = requests.post('http://localhost:5000/register_many', json={
        'readings': [
            {'timestamp': 1, 'type_of_sensor': 'AIRQUALITY', 'read': 100.0},
            {'timestamp': 2, 'type_of_sensor': 'AIRQUALITY', 'read': 50.0},
            {'timestamp': 3, 'type_of_sensor': 'AIRQUALITY', 'read': -100.0},
            {'timestamp': 4, 'type_of_sensor': 'AIRQUALITY', 'read': 110.0},
            {'timestamp': 5, 'type_of_sensor': 'AIRQUALITY', 'read': -200.0}
        ]
    })
    assert response.json()['result'] == 'OK'

# Test registering multiple readings for ULTRAVIOLETRADIATION
def test_register_many_uv():
    response = requests.post('http://localhost:5000/register_many', json={
        'readings': [
            {'timestamp': 1, 'type_of_sensor': 'ULTRAVIOLETRADIATION', 'read': 5.0},
            {'timestamp': 2, 'type_of_sensor': 'ULTRAVIOLETRADIATION', 'read': 3.0},
            {'timestamp': 3, 'type_of_sensor': 'ULTRAVIOLETRADIATION', 'read': -1.0},
            {'timestamp': 4, 'type_of_sensor': 'ULTRAVIOLETRADIATION', 'read': 7.0},
            {'timestamp': 5, 'type_of_sensor': 'ULTRAVIOLETRADIATION', 'read': -2.0}
        ]
    })
    assert response.json()['result'] == 'OK'

# Test registering multiple readings for TRAFFIC
def test_register_many_traffic():
    response = requests.post('http://localhost:5000/register_many', json={
        'readings': [
            {'timestamp': 1, 'type_of_sensor': 'TRAFFIC', 'read': 200.0},
            {'timestamp': 2, 'type_of_sensor': 'TRAFFIC', 'read': 150.0},
            {'timestamp': 3, 'type_of_sensor': 'TRAFFIC', 'read': -50.0},
            {'timestamp': 4, 'type_of_sensor': 'TRAFFIC', 'read': 250.0},
            {'timestamp': 5, 'type_of_sensor': 'TRAFFIC', 'read': -100.0}
        ]
    })
    assert response.json()['result'] == 'OK'

# Test highest accumulated value for AIRQUALITY
def test_highest_accumulated_airquality():
    response = requests.get('http://localhost:5000/highest_accumulated', params={
        'type_of_sensor': 'AIRQUALITY'
    })
    result = response.json()
    assert result['highest_accumulated_value'] == 260.0 # Updated value
    assert result['from'] == 1
    assert result['to'] == 4

# Test highest accumulated value for ULTRAVIOLETRADIATION
def test_highest_accumulated_uv():
    response = requests.get('http://localhost:5000/highest_accumulated', params={
        'type_of_sensor': 'ULTRAVIOLETRADIATION'
    })
    result = response.json()
    assert result['highest_accumulated_value'] == 19.0 # Updated value
    assert result['from'] == 1
    assert result['to'] == 4

# Test highest accumulated value for TRAFFIC
def test_highest_accumulated_traffic():
    response = requests.get('http://localhost:5000/highest_accumulated', params={
        'type_of_sensor': 'TRAFFIC'
    })
    result = response.json()
    assert result['highest_accumulated_value'] == 750.0 # Updated value
    assert result['from'] == 1
    assert result['to'] == 4

if __name__ == '__main__':
    pytest.main()
