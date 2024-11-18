"""
The BL model takes a Bayesian approach to asset allocation. It combines a prior estimate of return with views on certain assets, to produce a 
posterior estimate of the expected returns.

Advantage of BL:

1. you can provide views on only a subset of assets and BL will propagate, taking into account the covariance with other assets.
2. you can provide confidence in your views
3. BL posterior returns results in much more stable portfolio than using mean historical return.


Black Litterman Allocation
https://pyportfolioopt.readthedocs.io/en/latest/BlackLitterman.html

Interactive BL implementation by Thomas Kirschenman
https://github.com/thk3421-models/cardiel
"""

from pypfopt import black_litterman, risk_models
from pypfopt import BlackLitterman
from pypfopt import EfficientFrontier, objective_functions
from pypfopt import DiscreteAllocation

from Collector import YahooFin
import yfinance as yf


class BlackLitterman:

    def __init__(self):

        self.delta = None
        self.prior = None
        self.mcaps = {}
        self.cov_shrinkage = None
        self.price = None # List of tickers to create a portfolio
        self.market_price = None # Any comparision ticker like S&P to refer the market return
        self.omega = None
        self.return_bl = None
        self.alloc = None
        self.weight = None

    def initialize_variables(self):
        y_price = YahooFin(ticker=["MSFT", "AMZN", "NAT", "BAC", "DPZ", "DIS", "KO", "MCD", "COST", "SBUX"])
        self.price = y_price.get_data()
        

        y_market_price = YahooFin(ticker=["SPY"])
        self.market_price = y_market_price.get_data()

        for t in y.ticker:
            s = yf.Ticker(t)
            self.mcaps[t] = s.info["marketCap"]

        self.cov_shrinkage = risk_models.CovarianceShrinkage(self.price).ledoit_wolf()
        self.delta = black_litterman.market_implied_risk_aversion(self.market_price)


    def evaluate_prior(self):

        """
            prior: N x 1 vector of prior expected return (by definition)
            Prior is quantified by the market-implied risk premium, which is the market's excess return divided by its variance:
            delta = ()
        """
        
        self.prior = black_litterman.market_implied_prior_returns(self.mcaps, self.delta, self.cov_shrinkage)

        # plot a brah 
        # market_prior.plot.barh(figsize=(10,5));

    def evaluate_view(self):
        """
        NOTE: We are using a absolute view for now. This will be replaced by the self.weighted metrics derived from
        the tuned FinLLM 

        viewdict = <call-back function>
        confidence = <call-back function>(viewdict)
        """
        viewdict = {
            "AMZN": 0.10,
            "BAC": 0.30,
            "COST": 0.05,
            "DIS": 0.05,
            "DPZ": 0.20,
            "KO": -0.05,  # 5% down
            "MCD": 0.15,
            "MSFT": 0.10,
            "NAT": 0.50, 
            "SBUX": 0.10
        }

        # Either use confidence to evaluate omega or evaluate uncertainity matrix omega by specifying 1 standard deviation
        # conidence intervals, i.e bounds which we think will containthe true return 68% of the time. This is better
        # than putting arbitary percentage .

        #----------------------------------------------------------------------------------------------------------
        # confidence =  [
        #     0.6,
        #     0.4,
        #     0.2,
        #     0.5,
        #     0.7, # confident in dominos
        #     0.7, # confident KO will do poorly
        #     0.7, 
        #     0.5,
        #     0.1,
        #     0.4
        # ]

        # bl = BlackLittermanModel(self.cov_shrinkage, pi=self.prior, absolute_views=viewdict, omega="idzorek", view_confidences=confidence)

        # self.omega = bl.omega

        # OR -------------------------------------------------------------------------------------------------------

        intervals = [
            (0, 0.25),
            (0.1, 0.4),
            (-0.1, 0.15),
            (-0.05, 0.1),
            (0.15, 0.25),
            (-0.1, 0),
            (0.1, 0.2),
            (0.08, 0.12),
            (0.1, 0.9),
            (0, 0.3)
        ]

        variances = []
        for lb, ub in intervals:
            sigma = (ub - lb)/2
            variances.append(sigma ** 2)

        self.omega = np.diag(variances)

    def evaluate_posterior(self):

        bl = BlackLittermanModel(self.cov_shrinkage, pi="market", market_caps=self.mcaps, risk_aversion=self.delta,\
                                    absolute_views=viewdict, omega=self.omega)
        # Posterior estimate of returns
        self.return_bl = bl.bl_returns()
        return_df = pd.DataFrame([self.market_prior, self.return_bl, pd.Series(viewdict)], index=["Prior", "Posterior", "Views"]).T

        # rets_df.plot.bar(figsize=(12,8));

        cov_mat_bl = bl.bl_cov()

    def portfolio_allocation(self):

        ef = EfficientFrontier(self.self.return_bl)
        ef.add_objective(objective_functions.L2_reg)
        ef.max_sharpe()
        self.weight = ef.clean_self.weight()
        # pd.Series(self.weight).plot.pie(figsize=(10,10));
        da = DiscreteAllocation(self.weight, prices.iloc[-1], total_portfolio_value=20000)
        self.alloc, leftover = da.lp_portfolio()
        print(f"Leftover: ${leftover:.2f}")
















