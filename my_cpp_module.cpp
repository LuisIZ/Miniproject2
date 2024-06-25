#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // Include this for STL conversions
#include "sensor_data.h"

namespace py = pybind11;

// Create Python bindings for the SensorData class
PYBIND11_MODULE(my_cpp_module, m) {
    py::class_<SensorData>(m, "SensorData")
        .def(py::init<>()) // Bind the constructor
        .def("register_one", &SensorData::register_one) // Bind register_one method
        .def("register_many", &SensorData::register_many) // Bind register_many method
        .def("highest_accumulated", &SensorData::highest_accumulated) // Bind highest_accumulated method
        .def("get_data", &SensorData::get_data); // Bind get_data method (for testing)
}
