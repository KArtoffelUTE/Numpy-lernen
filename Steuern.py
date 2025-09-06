import numpy as np
sales = np.array([
    [200, 220, 250],
    [180, 210, 230],
    [190, 200, 210]
])
tax_rate = np.array([0.19, 0.07, 0.19])

Brutto = sales * (1 + tax_rate)
print(f"Bruttopreise:\n {Brutto}")

Umsatz = np.sum(Brutto, axis=1)
print(f"Umsatz pro Zeile:\n {Umsatz}")

Max_umsatz = np.max(Umsatz)
Max_umsatz_pos = np.argmax(Umsatz)
print(f"Max Umsatz: {Max_umsatz}, (Index {Max_umsatz_pos})")