"""
Annual Monthly(and Seasonal) Temperature of India from 1901 - 2017 Dataset.
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np

bias_correction = False
standard_normalization = True
genearal_normalization = not standard_normalization
beta1 = 0.9
beta2 = 0.999


"""
Intuitions:
--> The First Exponentially Weighted Moving Average is Sensitive towards the change in direction of the plot,
    which is a little smoothened due to the Weighted average more focusing on the historical values of the Original plot,
    which in terms retains the overall "momentum" of the plot. 
--> Whereas the Second EWMA is particularly sensitive towards the Overall direction of the Original plot,
    while smothening and averaging out all the nearby change in directions.
--> The Adam Curve is Sensitive Towards all the big changes in the directions of the original plot 
    as well as the curve moves along the overall direction of the Original plot. 

P.S while using the bias correction the graphs explodes in certain regions.
"""


data = pandas.read_excel("datafile.xls")
data = data[["YEAR", "ANNUAL"]]

# General Normalization.

if genearal_normalization:
    norm = "General"
    data["ANNUAL"] = np.divide(data["ANNUAL"], np.max(data["ANNUAL"]))

# Standard - Score Normalization of the temperature values.

if standard_normalization:
    norm = "S-Score"
    s = np.std(data["ANNUAL"])
    data["ANNUAL"] -= np.mean(data["ANNUAL"])
    data["ANNUAL"] = data["ANNUAL"] / s

stemp = 0
Momentum = np.zeros((data["YEAR"].shape[0],))

vtemp = 0
Rms = np.zeros((data["YEAR"].shape[0],))

for i in range(1, data["ANNUAL"].shape[0] + 1):
    vtemp = beta1 * (vtemp) + (1 - beta1) * data["ANNUAL"][i - 1]
    stemp = beta2 * (stemp) + (1 - beta2) * data["ANNUAL"][i - 1]**2

    # bias Correction.
    if bias_correction:
        vtemp /= (1 - beta1**i)
        stemp = stemp / (1 - beta2**i)

    Momentum[i - 1] = vtemp
    Rms[i - 1] = stemp

Adam = np.divide(Momentum, (np.sqrt(np.abs(Rms)) + 10**-10))

plt.plot(data["YEAR"], data["ANNUAL"], color="blue",
         label=f"{norm} Normalized Temprature")
plt.plot(data["YEAR"], Momentum, color="red",
         label=f"EWMA (Momentum), beta1 : {beta1}")
plt.plot(data["YEAR"], Rms, color="yellow",
         label=f"RMS EWMA (RMSProp), beta2 : {beta2}")
plt.plot(data["YEAR"], Adam, color="green",
         label=f"Adam Curve, Bias Correction: {bias_correction}")

plt.legend()
plt.ylabel("Temprature")
plt.xlabel("Year")
plt.show()
