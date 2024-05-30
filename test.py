import unittest
from src.betterstar import star # Ensure you are importing star, not the whole module
from matplotlib.path import Path

class TestStar(unittest.TestCase):
    def test_star(self):
        self.assertIsInstance(star, Path)  # Check if star is an instance of Path

if __name__ == '__main__':
    unittest.main()
