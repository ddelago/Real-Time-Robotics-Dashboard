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
            // Convert coords to valid tile indexes
            var leftBottom = Tile.CreateAroundLocation(bottom, left, zoom);
            var topRight = Tile.CreateAroundLocation(top, right, zoom);

            var minX = Math.Min(leftBottom.X, topRight.X);
            var maxX = Math.Max(leftBottom.X, topRight.X);

            var minY = Math.Min(leftBottom.Y, topRight.Y);
            var maxY = Math.Max(leftBottom.Y, topRight.Y);

            var tiles = new TileRange(minX, minY, maxX, maxY, zoom);

            return tiles;
        }

        public void getTiles(TileRange range, int zoom)
        {
            // Request the map tile urls from the osm server of a specific zoom level. 
            var random = new Random();
            string text = "";
            foreach (var tile in range)
            {
                text += $"http://{_serverEndpoints[random.Next(0, 2)]}.tile.openstreetmap.org/{zoom}/{tile.X}/{tile.Y}.png\n";
            }

            // Get the path to save the tile urls to
            string docPath = AppDomain.CurrentDomain.BaseDirectory;
            string path = $"../../../tile-urls/tiles-{zoom}.txt";
            
            // Check if directory exists
            if (!Directory.Exists("../../../tile-urls"))
            {
                Directory.CreateDirectory("../../../tile-urls");
            }

            // Save the urls to file
            if (!File.Exists(path))
            {
                File.Create(path).Dispose();
                File.WriteAllText(path, text);
            }
            else if (File.Exists(path))
            {
                File.WriteAllText(path, text);
            }
        }

        static public void Main(String[] args)
        {
            var genTiles = new GenerateTiles();

            for(var zoom = 0; zoom <= 19; zoom++)
            {
                //UTA
                var tileRange = genTiles.calcTileRange(32.7, -97.16, 32.75, -97.06, zoom);

                //USA
                //var tileRange = genTiles.calcTileRange(15.28, -132.57, 53.76, -45.02, zoom);

                //World
                //var tileRange = genTiles.calcTileRange(-84.09, -183.55, 83.37, 169.78, zoom);

                //URC Utah
                //var tileRange = genTiles.calcTileRange(38.4, -110.8, 38.42, -110.78, zoom);

                genTiles.getTiles(tileRange, zoom);
            }
        }
    }
}
