import pandas
import matplotlib.pyplot as plt
import numpy as np

bias_correction = False
standard_normalization = False
genearal_normalization = not standard_normalization
beta1 = 0.9
beta2 = 0.999

data = pandas.read_excel("datafile.xls")
data = data[["YEAR", "ANNUAL"]]

# General Normalization.

if genearal_normalization:
    data["ANNUAL"] = data["ANNUAL"] / np.max(data["ANNUAL"])

# Standard - Score Normalization of the temperature values.

if standard_normalization:
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

    # bias Correction for lower values of temperature.
    if i < 2 and bias_correction:
        vtemp = vtemp / (1 - beta1**i)
        stemp = stemp / (1 - beta2**i)

    Momentum[i - 1] = vtemp
    Rms[i - 1] = stemp

Adam = np.divide(Momentum, np.sqrt(np.abs(Rms)) + 10**-10)

plt.plot(data["YEAR"], data["ANNUAL"], color="blue", label="Data")
plt.plot(data["YEAR"], Momentum, color="red", label="EWMA (Momentum)")
plt.plot(data["YEAR"], Rms, color="yellow", label="RMS EWMA (RMSProp)")
plt.plot(data["YEAR"], Adam, color="green", label="Adam Curve")
plt.legend()
plt.ylabel("S-Score Normalized Temprature")
plt.xlabel("Year")
plt.show()
