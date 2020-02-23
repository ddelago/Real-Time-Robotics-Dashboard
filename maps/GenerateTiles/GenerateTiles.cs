using AwesomeTiles;
using System;
using System.IO;
using System.Text;

namespace GenerteTiles
{
    public class GenerateTiles
    {
        private readonly string[] _serverEndpoints = { "a", "b", "c" };

        public TileRange calcTileRange(double bottom, double left, double top, double right, int zoom)
        {
            var leftBottom = Tile.CreateAroundLocation(bottom, left, zoom);
            var topRight = Tile.CreateAroundLocation(top, right, zoom);

            //dirty, but obvious :)
            var minX = Math.Min(leftBottom.X, topRight.X);
            var maxX = Math.Max(leftBottom.X, topRight.X);

            var minY = Math.Min(leftBottom.Y, topRight.Y);
            var maxY = Math.Max(leftBottom.Y, topRight.Y);

            var tiles = new TileRange(minX, minY, maxX, maxY, zoom);

            return tiles;
        }

        public void getTiles(TileRange range, int zoom)
        {
            var random = new Random();
            string text = "";
            foreach (var tile in range)
            {
                text += $"http://{_serverEndpoints[random.Next(0, 2)]}.tile.openstreetmap.org/{zoom}/{tile.X}/{tile.Y}.png\n";
            }

            string docPath = AppDomain.CurrentDomain.BaseDirectory;
            File.WriteAllText($"../../../tiles-{zoom}.txt", text);
        }

        static public void Main(String[] args)
        {
            var genTiles = new GenerateTiles();

            for(var zoom = 10; zoom <= 18; zoom++)
            {
                var tileRange = genTiles.calcTileRange(32.7, -97.16, 32.75, -97.06, zoom);
                genTiles.getTiles(tileRange, zoom);
            }
        }
    }
}
