# 🌊 Sea Level Predictor

This project analyzes sea level trends and uses linear regression to **predict future sea levels** based on historical data from the U.S. Environmental Protection Agency (EPA).

---

## 📁 Files in this Repository

- `Sea_Level_Predictor.py`: Contains the function to generate the sea level plot with regression lines.
- `main.py`: Runs the predictor script to generate the visualization.
- `epa-sea-level.csv`: Historical global sea level data from the EPA.
- `sea_level_plot.png`: Output plot showing past data and future sea level predictions.
- `test_module.py`: Unit tests to validate plot generation and regression logic.

---

## 📈 Features

- Uses **scatter plot** to show historical sea level rise.
- Fits two **linear regression lines**:
  - One using all available data.
  - One using data from the year 2000 onward.
- Predicts sea level rise **through the year 2050**.

---

## 📦 Requirements

This project uses the following Python libraries:

```bash
pip install pandas matplotlib scipy


▶️ How to Run
To generate the sea level prediction plot:

bash
Copy
Edit
python main.py
This will output and save the plot as sea_level_plot.png.


✅ Testing
To run unit tests:

bash
Copy
Edit
python -m unittest test_module.py



📬 Contact
For questions or contributions, feel free to open an issue or fork the repository.
