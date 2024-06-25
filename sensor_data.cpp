#include "sensor_data.h"
#include <iostream>
#include <limits>

// Register a single sensor reading
void SensorData::register_one(int timestamp, const std::string& sensor_type, double read) {
    data[sensor_type].emplace_back(timestamp, read);
}

// Register multiple sensor readings
void SensorData::register_many(const std::vector<std::tuple<int, std::string, double>>& readings) {
    for (const auto& [timestamp, sensor_type, read] : readings) {
        data[sensor_type].emplace_back(timestamp, read);
    }
}

// Calculate the highest accumulated value for a given sensor type
std::string SensorData::highest_accumulated(const std::string& sensor_type) {
    if (data.find(sensor_type) == data.end() || data[sensor_type].empty()) {
        return R"({"highest_accumulated_value": -1.0, "from": -1, "to": -1})";
    }

    double max_sum = std::numeric_limits<double>::lowest();
    double current_sum = 0;
    int start = -1, best_start = -1, best_end = -1;

    for (size_t i = 0; i < data[sensor_type].size(); ++i) {
        if (current_sum <= 0) {
            current_sum = data[sensor_type][i].second;
            start = data[sensor_type][i].first;
        } else {
            current_sum += data[sensor_type][i].second;
        }

        if (current_sum > max_sum) {
            max_sum = current_sum;
            best_start = start;
            best_end = data[sensor_type][i].first;
        }
    }

    nlohmann::json result = {
        {"highest_accumulated_value", max_sum},
        {"from", best_start},
        {"to", best_end}
    };

    return result.dump();
}

// Get data for a specific sensor type (for testing purposes)
std::vector<std::pair<int, double>> SensorData::get_data(const std::string& sensor_type) const {
    auto it = data.find(sensor_type);
    if (it != data.end()) {
        return it->second;
    }
    return {};
}
