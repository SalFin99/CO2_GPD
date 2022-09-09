# CO2 emissions per capita vs GDP per capita: The case of Portugal

Hi! My applied econometrics exam of the last semester consisted in a time series analysis of the relation between CO2 emisssions and GDP per capita, trying to assess if the Cuznek Curve is present and which model best suits the data.
The guidelines of the project required Gretl, but I am  now personally replicating it in Python.

Requests and future development of this python project:

- Summary statistics:

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

- Regressions:
  - Linear model
  - Nonlinear model
  - Logarithmic model
  - First-difference model
  - Quantile regression

- t-test, p-values, confidence intervals, F-tests
- Diagnostic tests:
  - Heteroskedasticity
  - Autocorrelation tests
  - Mispecification tests

- Time-series models:
  - AR
  - MA
  - ARMA

:)
