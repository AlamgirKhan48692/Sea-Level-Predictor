#           This is the Test Module for the project.


import unittest
import Sea_Level_Predictor

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot_exists(self):
        ax = Sea_Level_Predictor.draw_plot()
        self.assertIsNotNone(ax, "Expected a matplotlib Axes object returned.")
        self.assertTrue(hasattr(ax, 'plot'), "Returned object is not a matplotlib Axes.")

if __name__ == "__main__":
    unittest.main()