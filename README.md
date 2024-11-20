**WQU Capstone project: Combining Technical Indicators with Black-Litterman For Advanced Portfolio Mangement**

**************************************************************************************************
THe 3 notebooks can be run to obtain the results after setting up the environment (described in next section)
1. nasdaq100_analysis_v5 - This file uses data_loader2.py to download the relevant data and executes our suggested strategy. THe output files obtained from here are comprehensive CSVs with outputs of a 60 day holding period and using the strategy, and a random allocation for every start date from 2023-01-03 (YYYY-MM-DD).
2. Random_Suggested_Backtest - This notebook uses the CSV outputs of the above file and performs a backtest and returns CSVs with performance metrics for both the random selection and suggested trading strategy.
3. Ema10_ema50 - Notebook containing modular code of the ema10/ema50 crossover stragey. Can be run for any start date/holding period/successive reinvest times. Run the notebook to obtain the performance metrics with a 60-day * 4 times, varied start dates (same as above 2 strategies). uses the same data loading function as nasdaq100_analysis_v5

   All 3 notebooks can be executed using run all to obtain the results demonstrated in our report

**************************************************************************************************************
1. Motivation
In this work, we are constructing a portfolio recommendation tool with the combination of the most popular technical rules - Relative Strength Index(RSI), Bollinger Band(BB) and Stochastic Indicator(SI). In Addition, the stocks are selected using a long term sharpe ratio and short term performance rank metrics. We have utilized a very long data series, the S&P 100 index from 2019 to 2024. Overall our results provide strong signals due to its support from recent technical indicators, long term fundamentals and short term performance. The empirical value from the combination of all indicators are tested against the slope of the stock to exclude any noise or false signals. The stocks which pass the test of all the indicators are fed to the Black Litterman model for asset allocation to our portfolio. Furthermore the returns of the recommended portfolio are tested against a random portfolio and portfolio generated from simple indicators. We see the buy signals and stock selection  from our tool provide better returns.

2. Data
The dataset can be accessible in ./historical_data, including:
Financial Data: This includes data from the S&P100 Index, Treasury Bond and all stocks in S&P100. We sourced our financial data from Yahoo Finance.
Technical Indicators: We included a variety of technical indicators such as RSI, Stochastic, and Bollinger Bands. These indicators provide valuable insights into different dimensions of price momentum, trend analysis, volatility, and volume dynamics.
3. The workflow
workflow
4. Project Setup & Execution
1. Creating a Virtual Environment
While there are several ways to set up a Python virtual environment for this project, we recommend using conda, a powerful package manager and environment manager from Anaconda. Conda makes it easy to create, save, load, and switch between project environments, and it can handle packages from Python and other languages as well. Alternatively, you can also use venv, a module provided by Python itself to create virtual environments. Please note you may require additional setup if you use venv.
Recommended Method: Using conda
Download and install conda by downloading the Anaconda distribution from here.
Create a virtual environment dedicated to this project by running the following commands using Anaconda Prompt:
conda create -n wqu_env python=3.9
conda activate wqu_env
Alternative Method: Using venv
If you prefer not to use conda, you can create a virtual environment using venv. To do this, navigate to the directory where you want to place the virtual environment, then run the venv module as a script:
Create environment
python3 -m venv wqu_env
        or 
python -m venv wqu_env
Activate environment
For Unix or MacOS:
source wqu_env/bin/activate
For Windows users using Git Bash:
source wqu_env/Scripts/activate
2. Clone the repository and install requirements
Clone this repository:
cd Capstone
Run the following command to install the required packages:
pip install -r requirements.txt

3. Run the pipeline


Run the 3 notebooks described above


Contributors
Suvodeep Pratik
