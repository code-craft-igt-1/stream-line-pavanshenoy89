#include <iostream>
#include <cstdlib>
#include <ctime>

double generateTemperature() {
    double minTemp = 36.0;
    double maxTemp = 40.0;
    return minTemp + static_cast<double>(rand()) / (static_cast<double>(RAND_MAX / (maxTemp - minTemp)));
}

int generatePulseRate() {
    int minPulseRate = 60;
    int maxPulseRate = 100;
    return minPulseRate + rand() % (maxPulseRate - minPulseRate + 1);
}

int generateSPO2() {
    int minSPO2 = 90;
    int maxSPO2 = 100;
    return minSPO2 + rand() % (maxSPO2 - minSPO2 + 1);
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    // Send fifty sets of readings
    for (int i = 0; i < 50; i++) {
        double temperature = generateTemperature();
        int pulseRate = generatePulseRate();
        int spo2 = generateSPO2();

        std::cout << "Temperature = " << temperature << ", Pulse Rate = " << pulseRate << ", SPO2 = " << spo2 << std::endl;
    }

    return 0;
}