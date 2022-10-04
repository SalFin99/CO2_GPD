from statsmodels import *
from scipy import stats
import statsmodels.stats.diagnostic as sms
from statsmodels.compat import lzip
import statsmodels.stats.outliers_influence as oi


def normalityTest(model):
    jb = stats.jarque_bera(model.resid)
    print("Jarque-Bera test for normality of residuals \n ")
    print(f'Statistic: {jb[0]:.4f}, p-value: {jb[1]}')

def LMtestAutocorrelation(model):
    name = ["Statistic", "p-value", "F-test statistic", "F-test p-value"]
    lm_test = sms.acorr_breusch_godfrey(model, nlags=3)
    print("\nLM test for autocorrelation: \n")
    print(lzip(name, lm_test))

def whiteTest(model):
    # define labels to use for output of White's test
    labels = ['Test Statistic', 'Test Statistic p-value', 'F-Statistic', 'F-Test p-value']
    white_test = sms.het_white(model.resid, model.model.exog)
    print("\nWhite's test for heteroskedasticity")
    print(lzip(labels, white_test))

def ramseyResetTest(model):
    print("Ramsey reset test for model specification: ")
    print(oi.reset_ramsey(model, degree=2))

#def chowTest(model, years):

def cusumTest(model_resids):
    labels = ['Test Statistic', ' p-value','Tabulated critical values, respectively for alpha = 1%, 5% and 10%']

    print("\nCusum test for parameter stability: ")

    cusum_res=sms.breaks_cusumolsresid(model_resids, ddof=5)
    print(lzip(labels, cusum_res))
