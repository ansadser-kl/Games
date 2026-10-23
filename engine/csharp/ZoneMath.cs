// Engine-independent C# safe-zone helper for a possible Unity port.
namespace Battlezone.Firestorm
{
    public readonly struct Zone
    {
        public readonly float X;
        public readonly float Z;
        public readonly float Radius;

        public Zone(float x, float z, float radius)
        {
            X = x;
            Z = z;
            Radius = radius < 0 ? 0 : radius;
        }

        public bool Contains(float x, float z)
        {
            float dx = x - X;
            float dz = z - Z;
            return dx * dx + dz * dz <= Radius * Radius;
        }
    }
}
