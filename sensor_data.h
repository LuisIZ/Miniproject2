#ifndef SENSOR_DATA_H
#define SENSOR_DATA_H

#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <nlohmann/json.hpp>

class SensorData {
public:
    // Register a single sensor reading
    void register_one(int timestamp, const std::string& sensor_type, double read);

    // Register multiple sensor readings
    void register_many(const std::vector<std::tuple<int, std::string, double>>& readings);

    // Calculate the highest accumulated value for a given sensor type
    std::string highest_accumulated(const std::string& sensor_type);

    // Get data for a specific sensor type (for testing purposes)
    std::vector<std::pair<int, double>> get_data(const std::string& sensor_type) const;

private:
    std::unordered_map<std::string, std::vector<std::pair<int, double>>> data;
};

#endif // SENSOR_DATA_H
