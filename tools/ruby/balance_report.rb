#!/usr/bin/env ruby
# Offline weapon report helper for BATTLEZONE: FIRESTORM.
weapons = [
  { name: "Rifle", damage: 24.0, rate: 7.5 },
  { name: "SMG", damage: 15.0, rate: 11.0 },
  { name: "Marksman", damage: 55.0, rate: 2.0 }
]

puts "BATTLEZONE: FIRESTORM — Ruby weapon report"
weapons.sort_by { |weapon| -(weapon[:damage] * weapon[:rate]) }.each do |weapon|
  dps = weapon[:damage] * weapon[:rate]
  puts format("%-10s %5.1f damage/sec", weapon[:name], dps)
end
