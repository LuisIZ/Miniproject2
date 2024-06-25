#include <gtest/gtest.h>
#include "sensor_data.h"

// Test registering a single reading for AIRQUALITY
TEST(SensorDataTest, RegisterOne_AirQuality) {
    SensorData sensor_data;
    sensor_data.register_one(1, "AIRQUALITY", 100.0);
    auto data = sensor_data.get_data("AIRQUALITY");
    ASSERT_EQ(data.size(), 1);
    ASSERT_EQ(data[0].first, 1);
    ASSERT_EQ(data[0].second, 100.0);
}

// Test registering a single reading for ULTRAVIOLETRADIATION
TEST(SensorDataTest, RegisterOne_UV) {
    SensorData sensor_data;
    sensor_data.register_one(1, "ULTRAVIOLETRADIATION", 5.0);
    auto data = sensor_data.get_data("ULTRAVIOLETRADIATION");
    ASSERT_EQ(data.size(), 1);
    ASSERT_EQ(data[0].first, 1);
    ASSERT_EQ(data[0].second, 5.0);
}

// Test registering a single reading for TRAFFIC
TEST(SensorDataTest, RegisterOne_Traffic) {
    SensorData sensor_data;
    sensor_data.register_one(1, "TRAFFIC", 200.0);
    auto data = sensor_data.get_data("TRAFFIC");
    ASSERT_EQ(data.size(), 1);
    ASSERT_EQ(data[0].first, 1);
    ASSERT_EQ(data[0].second, 200.0);
}

// Test registering multiple readings for AIRQUALITY
TEST(SensorDataTest, RegisterMany_AirQuality) {
    SensorData sensor_data;
    std::vector<std::tuple<int, std::string, double>> readings = {
        {1, "AIRQUALITY", 100.0},
        {2, "AIRQUALITY", 50.0},
        {3, "AIRQUALITY", -100.0},
        {4, "AIRQUALITY", 110.0},
        {5, "AIRQUALITY", -200.0}
    };
    sensor_data.register_many(readings);
    auto data = sensor_data.get_data("AIRQUALITY");
    ASSERT_EQ(data.size(), 5);
    ASSERT_EQ(data[0].first, 1);
    ASSERT_EQ(data[0].second, 100.0);
}

// Test registering multiple readings for ULTRAVIOLETRADIATION
TEST(SensorDataTest, RegisterMany_UV) {
    SensorData sensor_data;
    std::vector<std::tuple<int, std::string, double>> readings = {
        {1, "ULTRAVIOLETRADIATION", 5.0},
        {2, "ULTRAVIOLETRADIATION", 3.0},
        {3, "ULTRAVIOLETRADIATION", -1.0},
        {4, "ULTRAVIOLETRADIATION", 7.0},
        {5, "ULTRAVIOLETRADIATION", -2.0}
    };
    sensor_data.register_many(readings);
    auto data = sensor_data.get_data("ULTRAVIOLETRADIATION");
    ASSERT_EQ(data.size(), 5);
    ASSERT_EQ(data[0].first, 1);
    ASSERT_EQ(data[0].second, 5.0);
}

// Test registering multiple readings for TRAFFIC
TEST(SensorDataTest, RegisterMany_Traffic) {
    SensorData sensor_data;
    std::vector<std::tuple<int, std::string, double>> readings = {
        {1, "TRAFFIC", 200.0},
        {2, "TRAFFIC", 150.0},
        {3, "TRAFFIC", -50.0},
        {4, "TRAFFIC", 250.0},
        {5, "TRAFFIC", -100.0}
    };
    sensor_data.register_many(readings);
    auto data = sensor_data.get_data("TRAFFIC");
    ASSERT_EQ(data.size(), 5);
    ASSERT_EQ(data[0].first, 1);
    ASSERT_EQ(data[0].second, 200.0);
}

// Test calculating the highest accumulated value for AIRQUALITY
TEST(SensorDataTest, HighestAccumulated_AirQuality) {
    SensorData sensor_data;
    sensor_data.register_one(1, "AIRQUALITY", 100.0);
    sensor_data.register_one(2, "AIRQUALITY", 50.0);
    sensor_data.register_one(3, "AIRQUALITY", -100.0);
    sensor_data.register_one(4, "AIRQUALITY", 110.0);
    sensor_data.register_one(5, "AIRQUALITY", -200.0);
    std::string result = sensor_data.highest_accumulated("AIRQUALITY");
    nlohmann::json expected = {
        {"highest_accumulated_value", 160.0},
        {"from", 1},
        {"to", 4}
    };
    ASSERT_EQ(result, expected.dump());
}

// Test calculating the highest accumulated value for ULTRAVIOLETRADIATION
TEST(SensorDataTest, HighestAccumulated_UV) {
    SensorData sensor_data;
    sensor_data.register_one(1, "ULTRAVIOLETRADIATION", 5.0);
    sensor_data.register_one(2, "ULTRAVIOLETRADIATION", 3.0);
    sensor_data.register_one(3, "ULTRAVIOLETRADIATION", -1.0);
    sensor_data.register_one(4, "ULTRAVIOLETRADIATION", 7.0);
    sensor_data.register_one(5, "ULTRAVIOLETRADIATION", -2.0);
    std::string result = sensor_data.highest_accumulated("ULTRAVIOLETRADIATION");
    nlohmann::json expected = {
        {"highest_accumulated_value", 14.0},
        {"from", 1},
        {"to", 4}
    };
    ASSERT_EQ(result, expected.dump());
}

// Test calculating the highest accumulated value for TRAFFIC
TEST(SensorDataTest, HighestAccumulated_Traffic) {
    SensorData sensor_data;
    sensor_data.register_one(1, "TRAFFIC", 200.0);
    sensor_data.register_one(2, "TRAFFIC", 150.0);
    sensor_data.register_one(3, "TRAFFIC", -50.0);
    sensor_data.register_one(4, "TRAFFIC", 250.0);
    sensor_data.register_one(5, "TRAFFIC", -100.0);
    std::string result = sensor_data.highest_accumulated("TRAFFIC");
    nlohmann::json expected = {
        {"highest_accumulated_value", 550.0}, // Adjusted expected value
        {"from", 1},
        {"to", 4}
    };
    ASSERT_EQ(result, expected.dump());
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
