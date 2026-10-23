// Optional native combat-math prototype. Compile:
// c++ -std=c++17 -Wall -Wextra -pedantic engine/cpp/combat_math.cpp -o /tmp/battlezone-combat
#include <algorithm>
#include <iostream>
#include <string>

struct Weapon {
    std::string name;
    float damage;
    float rounds_per_second;
};

float damage_per_second(const Weapon& weapon) {
    return std::max(0.0f, weapon.damage) * std::max(0.0f, weapon.rounds_per_second);
}

int main() {
    const Weapon rifle{"Rifle", 24.0f, 7.5f};
    std::cout << "BATTLEZONE: FIRESTORM — " << rifle.name
              << " DPS: " << damage_per_second(rifle) << '\n';
    return 0;
}
