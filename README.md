**WQU Capstone project: Combining Technical Indicators with Black-Litterman For Advanced Portfolio Mangement**
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

Run the data_loader.py under utils to download the required data.
Use nasdaq100_analysis.ipynb to generate all the metrics
Use the benchmark_strategy.ipynb to generate the results

Contributors
Suvodeep
Pratik
