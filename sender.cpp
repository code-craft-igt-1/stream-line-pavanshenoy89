#include <iostream>
#include <cstdlib>
#include <ctime>

const float MIN_TEMP = 50;
const float MAX_TEMP = 125;
const float MIN_PULSE_RATE = 50;
const float MAX_PULSE_RATE = 150;
const float MIN_SPO2 = 50;
const float MAX_SPO2 = 100;

float generateSensorReading(float minValue, float maxValue) {
    return minValue + static_cast<float>(rand()) / (static_cast<float>(RAND_MAX / (maxValue - minValue)));
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    // Send fifty sets of readings
    for (int i = 0; i < 50; i++) {
        float temperature = generateSensorReading(MIN_TEMP, MAX_TEMP);
        float pulseRate = generateSensorReading(MIN_PULSE_RATE, MAX_PULSE_RATE);
        float spo2 = generateSensorReading(MIN_SPO2, MAX_SPO2);
        std::cout << "Temperature = " << temperature << ", Pulse Rate = " << pulseRate << ", SPO2 = " << spo2 << std::endl;
    }
    return 0;
}