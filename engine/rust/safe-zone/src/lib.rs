//! Deterministic safe-zone helpers for future server-side gameplay.
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct SafeZone {
    pub x: f32,
    pub z: f32,
    pub radius: f32,
}

impl SafeZone {
    pub fn contains(&self, x: f32, z: f32) -> bool {
        let dx = x - self.x;
        let dz = z - self.z;
        dx * dx + dz * dz <= self.radius.max(0.0).powi(2)
    }

    pub fn damage_per_second(&self, x: f32, z: f32, outside_damage: f32) -> f32 {
        if self.contains(x, z) { 0.0 } else { outside_damage.max(0.0) }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn checks_inside_and_outside() {
        let zone = SafeZone { x: 0.0, z: 0.0, radius: 10.0 };
        assert!(zone.contains(3.0, 4.0));
        assert!(!zone.contains(11.0, 0.0));
        assert_eq!(zone.damage_per_second(11.0, 0.0, 2.0), 2.0);
    }
}
