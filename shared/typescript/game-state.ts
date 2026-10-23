// Shared API contract for future multiplayer/client integration.
export type MatchPhase = "lobby" | "dropping" | "active" | "finished";

export interface PlayerSnapshot {
  id: string;
  health: number;
  armor: number;
  alive: boolean;
  x: number;
  y: number;
  z: number;
}

export interface MatchSnapshot {
  matchId: string;
  phase: MatchPhase;
  serverTimeMs: number;
  alivePlayers: number;
  safeZone: { x: number; z: number; radius: number };
  players: PlayerSnapshot[];
}

export function isValidPlayerSnapshot(value: unknown): value is PlayerSnapshot {
  if (typeof value !== "object" || value === null) return false;
  const p = value as Record<string, unknown>;
  return typeof p.id === "string"
    && typeof p.health === "number" && p.health >= 0 && p.health <= 100
    && typeof p.armor === "number" && p.armor >= 0 && p.armor <= 100
    && typeof p.alive === "boolean"
    && typeof p.x === "number" && typeof p.y === "number" && typeof p.z === "number";
}
