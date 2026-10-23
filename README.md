# BATTLEZONE: FIRESTORM

A browser-based 3D battle royale prototype built for mobile and desktop.

## Current prototype features
- 3D battlefield with buildings, forest, and a military compound
- Weapon firing, ammo, reloading, health, armor, and healing
- AI enemies that pursue and attack the player
- Shrinking safe zone and last-survivor victory condition
- Desktop keyboard/mouse controls and mobile touch controls

## Run the browser game
Open `index.html` through a local static web server. Three.js is loaded from jsDelivr, so an internet connection is needed.

Quick local server (Python 3):
```sh
sh scripts/dev.sh
```
Then visit `http://localhost:8000`.

## Multi-language development scaffold
The repository now includes starter modules/tools in several languages so the project can grow into a larger game architecture:

| Language | Path | Purpose |
| --- | --- | --- |
| JavaScript | `index.html` | Current playable browser prototype |
| TypeScript | `shared/typescript/game-state.ts` | Shared multiplayer state contract |
| Go | `services/go-api/main.go` | Optional health/API service |
| Python | `tools/python/balance_check.py` | Offline weapon-balance checker |
| Ruby | `tools/ruby/balance_report.rb` | Offline weapon-balance report |
| Shell | `scripts/dev.sh` | Local development server launcher |
| C++ | `engine/cpp/combat_math.cpp` | Native combat math prototype |
| Rust | `engine/rust/safe-zone/` | Safe-zone math library with a unit test |
| C# | `engine/csharp/ZoneMath.cs` | Engine-independent safe-zone helper for a possible Unity port |
| Java | `services/java-matchmaking/MatchmakingHealth.java` | Minimal matchmaking-service health endpoint |

### Run the optional tools
- Python: `python3 tools/python/balance_check.py`
- Ruby: `ruby tools/ruby/balance_report.rb`
- C++: `c++ -std=c++17 engine/cpp/combat_math.cpp -o /tmp/battlezone-combat && /tmp/battlezone-combat`
- Rust: `cd engine/rust/safe-zone && cargo test`
- Java: `javac services/java-matchmaking/MatchmakingHealth.java && java -cp services/java-matchmaking MatchmakingHealth`
- Go: `go run services/go-api/main.go`

## Important architecture note
These are development starters, not yet connected to the browser game or to each other. The current Vercel deployment serves the static JavaScript game only; it does not run Go, Java, Python, Ruby, C++, Rust, or C# services. To make a real online battle royale, the next phase is to choose and deploy an authoritative multiplayer backend, then connect authentication, matchmaking, rooms, player state, and anti-cheat checks to the client. Using every language in production would add complexity, so each should only be kept where it has a clear job.

## Deploy to Vercel
Import this repository into Vercel. The browser prototype is static and does not require a build command. Set the output directory to `.`.

## Roadmap
This is still a single-player prototype. Dedicated servers, matchmaking, vehicles, online multiplayer, persistent player accounts, and production security remain future work.
