import numpy as np

temps = np.array([
    [12, 14, 15, 14],
    [13, 15, 14, 16],
    [15, 16, 16, 17],
    [14, 14, 15, 15],
    [13, 13, 14, 14],
    [12, 12, 13, 13],
    [11, 12, 12, 11]
])

durschnitte = np.mean(temps, axis = 1)
print(f"Durchschnitt pro Tag: {durschnitte}")

wärmster_tag = np.argmax(durschnitte)
print(f"Wärmster Tag: {wärmster_tag + 1}")

Wochendurchschnitt = np.mean(durschnitte)
print(f"Wochendurchschnitt: {Wochendurchschnitt}")

