#           This is the main file for the project.
#           IT is used to run the Sea Level Predictor project.


from Sea_Level_Predictor import draw_plot
import unittest
import test_module

# Call the function to generate and save the plot
draw_plot()

unittest.main(module=test_module, verbosity=2)
