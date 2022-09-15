# CO2 emissions per capita vs GDP per capita: The case of Portugal

Hi! My applied econometrics exam of the last semester consisted in a time series analysis of the relation between CO2 emisssions and GDP per capita, trying to assess if the Cuznek Curve is present and which model best suits the data. The guidelines of the project required Gretl, but I am now personally writing some part of it in Python. As the assessment of the best model for every functional form has already been carried out, i will only code the models which were choosen for every form.

- Summary statistics & visualizations:

GDP_perCap  logGDP_perCap  logDiffGDP_perCap
count    149.000000     149.000000         148.000000
mean    7938.705366       8.452257           0.019299
std     8295.177506       1.010704           0.040228
min     1486.000000       7.303843          -0.114410
25%     1962.000000       7.581720          -0.004474
50%     2879.000000       7.965198           0.020095
75%    12894.000000       9.464517           0.042307
max    27035.599610      10.204910           0.149593


Annual_CO2_emissions_TperCap  logAnnual_CO2_emissions_TperCap  \
count                    149.000000                       149.000000   
mean                       1.774626                        -0.115513   
std                        2.005871                         1.271783   
min                        0.005100                        -5.278515   
25%                        0.407600                        -0.897469   
50%                        0.633000                        -0.457285   
75%                        2.745700                         1.010036   
max                        6.715700                         1.904448   

logDiffAnnual_CO2_emissions_TperCap  
count                           148.000000  
mean                              0.046568  
std                               0.263543  
min                              -0.593225  
25%                              -0.033819  
50%                               0.027173  
75%                               0.085629  
max                               2.649210  


We can see  that the growth rates (first difference of the log variables, bottom right corner) become stationary in comparison with the other variables forms, as deducible from the following time series plots:

<img width="1380" alt="Screenshot 2022-09-10 at 14 32 41" src="https://user-images.githubusercontent.com/103948003/189483579-4ec48284-8ce1-4778-83ee-f4d2821a1d91.png">

<img width="1390" alt="Screenshot 2022-09-10 at 14 32 50" src="https://user-images.githubusercontent.com/103948003/189483582-602a367f-3dcc-45ad-8b53-dea3944b50cf.png">

The following graph shows a basic representation of GDP vs CO2 emissions:

<img width="454" alt="Screenshot 2022-09-10 at 14 56 15" src="https://user-images.githubusercontent.com/103948003/189484401-8f7e2191-419a-4d50-8f45-612eb002b101.png">

- Regressions:
  - Linear model:

                                          OLS Regression Results                                 
        ========================================================================================
        Dep. Variable:     Annual_CO2_emissions_TperCap   R-squared:                       0.995
        Model:                                      OLS   Adj. R-squared:                  0.995
        Method:                           Least Squares   F-statistic:                     168.3
        Date:                          Thu, 15 Sep 2022   Prob (F-statistic):           7.84e-53
        Time:                                  16:14:48   Log-Likelihood:                 78.918
        No. Observations:                           148   AIC:                            -145.8
        Df Residuals:                               142   BIC:                            -127.9
        Df Model:                                     5                                         
        Covariance Type:                            HC0                                         
        ==============================================================================
        coef    std err          z      P>|z|      [0.025      0.975]
        ------------------------------------------------------------------------------
        const          0.0126      0.014      0.916      0.359      -0.014       0.040
        GDP_perCap     0.0002   4.46e-05      4.797      0.000       0.000       0.000
        GDP_lag1      -0.0002    4.3e-05     -4.966      0.000      -0.000      -0.000
        CO2_lag1       0.9885      0.065     15.164      0.000       0.861       1.116
        dummy1989      0.6851      0.049     14.005      0.000       0.589       0.781
        dummy2003     -0.4138      0.104     -3.988      0.000      -0.617      -0.210
        ==============================================================================
        Omnibus:                       22.190   Durbin-Watson:                   2.120
        Prob(Omnibus):                  0.000   Jarque-Bera (JB):              124.734
        Skew:                           0.047   Prob(JB):                     8.21e-28
        Kurtosis:                       7.496   Cond. No.                     2.12e+05
        ==============================================================================


  - Nonlinear model
  - Logarithmic model
  - First-difference model
  - Quantile regression

- Diagnostic tests:
  - Heteroskedasticity
  - Autocorrelation tests
  - Mispecification tests

- Time-series models:
  - AR
  - MA
  - ARMA

:)
