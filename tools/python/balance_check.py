#!/usr/bin/env python3
"""Small offline balance sanity-check for BATTLEZONE: FIRESTORM."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Weapon:
    name: str
    damage: float
    rounds_per_second: float
    magazine: int
    reload_seconds: float

    @property
    def dps(self) -> float:
        return self.damage * self.rounds_per_second

    @property
    def reload_fraction(self) -> float:
        return self.magazine / (self.magazine + self.reload_seconds * self.rounds_per_second)

def main() -> None:
    weapons = [
        Weapon("Rifle", 24, 7.5, 30, 2.0),
        Weapon("SMG", 15, 11.0, 32, 1.7),
        Weapon("Marksman", 55, 2.0, 12, 2.4),
    ]
    print("BATTLEZONE: FIRESTORM — weapon balance")
    for weapon in sorted(weapons, key=lambda item: item.dps, reverse=True):
        print(f"{weapon.name:10} DPS={weapon.dps:6.1f}  "
              f"magazine={weapon.magazine:2}  "
              f"reload uptime={weapon.reload_fraction:.0%}")
    if any(w.damage <= 0 or w.rounds_per_second <= 0 for w in weapons):
        raise SystemExit("Invalid weapon values: damage and fire rate must be positive.")

if __name__ == "__main__":
    main()
