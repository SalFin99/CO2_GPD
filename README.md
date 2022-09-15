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

        Notes:
        [1] Standard Errors are heteroscedasticity robust (HC3)

        This adjusted model has an optimal adjusted R-squared value of more than 99%, indicating a stronger explanatory capacity compared to the previous model, and a p-value of the F test which is zero. In this case, the coefficient for GDP per capita is extremely low



  - Nonlinear model

                                    OLS Regression Results                                 
        ========================================================================================
        Dep. Variable:     Annual_CO2_emissions_TperCap   R-squared:                       0.995
        Model:                                      OLS   Adj. R-squared:                  0.995
        Method:                           Least Squares   F-statistic:                     55.93
        Date:                          Thu, 15 Sep 2022   Prob (F-statistic):           6.24e-24
        Time:                                  20:25:12   Log-Likelihood:                 80.623
        No. Observations:                           148   AIC:                            -149.2
        Df Residuals:                               142   BIC:                            -131.3
        Df Model:                                     5                                         
        Covariance Type:                            HC3                                         
        ================================================================================
        coef    std err          z      P>|z|      [0.025      0.975]
        --------------------------------------------------------------------------------
        const           -0.0566      0.019     -3.007      0.003      -0.094      -0.020
        GDP_perCap    4.384e-05   1.54e-05      2.844      0.004    1.36e-05     7.4e-05
        sqGDP_percap -1.104e-09   3.74e-10     -2.953      0.003   -1.84e-09   -3.71e-10
        CO2_lag1         0.9297      0.072     12.954      0.000       0.789       1.070
        dummy1989        0.7024     36.175      0.019      0.985     -70.199      71.604
        dummy1999        0.7598    639.439      0.001      0.999   -1252.518    1254.037
        ==============================================================================
        Omnibus:                       28.157   Durbin-Watson:                   2.220
        Prob(Omnibus):                  0.000   Jarque-Bera (JB):               73.132
        Skew:                           0.736   Prob(JB):                     1.32e-16
        Kurtosis:                       6.113   Cond. No.                     3.13e+09
        ==============================================================================

        Notes:
        [1] Standard Errors are heteroscedasticity robust (HC3)

        This model has a very good adjusted R squared value of more than 99%,  also the squared GDP variable is now significant and some of tests can be accepted. Indeed, autocorrelation is not present anymore and we have stability in the parameters’ coefficient


  - Logarithmic model

        To adjust this model, we robustified our standard errors and we introduced three significant dummies (1872, 1874, 1878) and a lag of the dependent variable. The dummies can be explained mentioning the golpe of Saldanha Oliveira, in 1870, which was followed by a period of major political turmoil and financial difficulties

        OLS Regression Results                            
        ==============================================================================
        Dep. Variable:                 logCO2   R-squared:                       0.990
        Model:                            OLS   Adj. R-squared:                  0.989
        Method:                 Least Squares   F-statistic:                     2512.
        Date:                Thu, 15 Sep 2022   Prob (F-statistic):          1.25e-136
        Time:                        20:41:30   Log-Likelihood:                 101.20
        No. Observations:                 148   AIC:                            -190.4
        Df Residuals:                     142   BIC:                            -172.4
        Df Model:                           5                                         
        Covariance Type:                  HC3                                         
        =================================================================================
        coef    std err          z      P>|z|      [0.025      0.975]
        ---------------------------------------------------------------------------------
        const            -1.5388      1.046     -1.471      0.141      -3.589       0.512
        logGDP_perCap     0.1840      0.123      1.497      0.134      -0.057       0.425
        lag_logCO2        0.8259      0.114      7.257      0.000       0.603       1.049
        dummy1872         2.0077      1.221      1.645      0.100      -0.385       4.400
        dummy1874        -0.4435      3.112     -0.143      0.887      -6.543       5.655
        dummy1877        -0.5932      1.864     -0.318      0.750      -4.246       3.060
        ==============================================================================
        Omnibus:                       37.685   Durbin-Watson:                   2.034
        Prob(Omnibus):                  0.000   Jarque-Bera (JB):              508.086
        Skew:                           0.237   Prob(JB):                    4.68e-111
        Kurtosis:                      12.065   Cond. No.                         236.
        ==============================================================================

        Notes:
        [1] Standard Errors are heteroscedasticity robust (HC3)

        As we can assess by looking at the coefficients, an increase of one percent in GDP per capita produces a 0.184% increase in CO2 emissions per capita. The dummies are all significant, showing a larger positive impact for the year 1872 and negative impacts for 1874 and 1877. The adjusted R-squared and F-tests confirms that the model is well performing.


  - First-difference model

                                  OLS Regression Results                                    
        ===============================================================================================
        Dep. Variable:     logDiffAnnual_CO2_emissions_TperCap   R-squared:                       0.405
        Model:                                             OLS   Adj. R-squared:                  0.384
        Method:                                  Least Squares   F-statistic:                     1324.
        Date:                                 Thu, 15 Sep 2022   Prob (F-statistic):          5.97e-116
        Time:                                         20:52:03   Log-Likelihood:                 110.39
        No. Observations:                                  146   AIC:                            -208.8
        Df Residuals:                                      140   BIC:                            -190.9
        Df Model:                                            5                                         
        Covariance Type:                                   HC3                                         
        =====================================================================================
        coef    std err          z      P>|z|      [0.025      0.975]
        -------------------------------------------------------------------------------------
        const                 0.0045      0.015      0.302      0.762      -0.024       0.033
        logDiffGDP_perCap     1.0361      0.266      3.895      0.000       0.515       1.557
        lag1_DiffCO2          0.0713      0.132      0.541      0.589      -0.187       0.330
        lag2_DiffCO2         -0.0992      0.074     -1.334      0.182      -0.245       0.047
        dummy1875             0.8397      0.052     16.283      0.000       0.739       0.941
        dummy1877            -0.5087      0.503     -1.012      0.312      -1.494       0.477
        ==============================================================================
        Omnibus:                       37.323   Durbin-Watson:                   2.311
        Prob(Omnibus):                  0.000   Jarque-Bera (JB):              546.889
        Skew:                           0.135   Prob(JB):                    1.76e-119
        Kurtosis:                      12.478   Cond. No.                         25.2
        ==============================================================================

        Notes:
        [1] Standard Errors are heteroscedasticity robust (HC3)

        We have to note that the first lag of the dependent variable is not significant, but when included it concurs to correct autocorrelation and to get stable coefficients.
        The interpretation of this model suggest that a 1% increase in the growth rate of GDP per capita produces a 1.03% increase in the growth rate of CO2 emissions per capita. The adjusted R-square is not particularly high, as it is not able to explain approximately 62% of variation in the growth rate of CO2 emissions per capita.





- Time-series models:
  - AR
  - MA
  - ARMA

:)
