from statsmodels.compat import lzip
from scipy import stats
import statsmodels.stats.diagnostic as sms

def normalityTest(model):
    jb = stats.jarque_bera(model.resid)
    print(f'Jarque-Bera test ---- statistic: {jb[0]:.4f}, p-value: {jb[1]}')

def LMtestAutocorrelation(model):
    name = ["LM test statistic", "p-value", "F-test statistic", "F-test p-value"]
    lm_test = sms.acorr_breusch_godfrey(model, nlags=3)
    print(lzip(name, lm_test))
