# CO2 emissions per capita vs GDP per capita: The case of Portugal

Hi! My applied econometrics exam of the last semester consisted in a time series analysis of the relation between CO2 emisssions and GDP per capita, trying to assess if the Cuznek Curve is present and which model best suits the data. The guidelines of the project required Gretl, but I am  now personally replicating it in Python. Requests and future development of this python project:

- Summary statistics & visualizations:

<img width="527" alt="Screenshot 2022-09-09 at 15 56 48" src="https://user-images.githubusercontent.com/103948003/189366946-644b40bc-6dcb-49c3-bce3-fc3a58d74fd4.png">

<img width="679" alt="Screenshot 2022-09-09 at 15 57 07" src="https://user-images.githubusercontent.com/103948003/189367008-b421fe94-7fde-46a9-b448-00705f64c6f4.png">

<img width="1380" alt="Screenshot 2022-09-10 at 14 32 41" src="https://user-images.githubusercontent.com/103948003/189483579-4ec48284-8ce1-4778-83ee-f4d2821a1d91.png">

<img width="1390" alt="Screenshot 2022-09-10 at 14 32 50" src="https://user-images.githubusercontent.com/103948003/189483582-602a367f-3dcc-45ad-8b53-dea3944b50cf.png">

We can see  that the growth rates (first difference of the log variables, bottom right corner) become stationary in comparison with the other variables forms, as deducible from the following time series plots:

![image](https://user-images.githubusercontent.com/103948003/189483600-4828cc0e-b0d0-416c-97fc-4f12eee8cf73.png)

The following graph shows a basic representation of GDP vs CO2 emissions:

<img width="454" alt="Screenshot 2022-09-10 at 14 56 15" src="https://user-images.githubusercontent.com/103948003/189484401-8f7e2191-419a-4d50-8f45-612eb002b101.png">

- Regressions:
  - Linear model
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
