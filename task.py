import matplotlib.pyplot as plt
from scipy.integrate import quad

def composite_trapezoidal(f, a, b, n):
    h = (b - a) / n
    y_values = []
    for i in range(n + 1):
        x = a + i * h
        y_values.append(f(x))
    interior_sum = sum(y_values[1:-1])
    weighted_bracket = (
        y_values[0] + 2 * interior_sum + y_values[-1]
    )
    integral = (h / 2) * weighted_bracket
    print(f"h = {h:.4f}")
    print(f"Weighted bracket = {weighted_bracket:.4f}")
    return integral

# TASK 1
def f(x):
    return x ** 2
a = 0
b = 2
n = 4
exact_value = 8 / 3
print("TASK 1 - COMPOSITE TRAPEZOIDAL RULE")
test_value = composite_trapezoidal(f, a, b, n)
print(f"Trapezoidal result = {test_value:.6f}")
print(f"Exact value = {exact_value:.6f}")

# TASK 2
print("\nTASK 2 - COMPARISON WITH SCIPY QUAD")
library_value, _ = quad(f, a, b)
results = []
for n in [4, 8]:
    trapezoidal_value = composite_trapezoidal(f, a, b, n)
    absolute_difference = abs(trapezoidal_value - library_value)
    percentage_difference = (
        absolute_difference / abs(library_value)
    ) * 100
    results.append((
        n,
        trapezoidal_value,
        library_value,
        absolute_difference,
        percentage_difference
    ))

print("\nn     Trapezoidal     Library value     Absolute diff.     Percentage diff.")
for row in results:
    print(
        f"{row[0]:<5} {row[1]:<15.6f} {row[2]:<16.6f} "
        f"{row[3]:<17.6f} {row[4]:.4f}%"
    )

# TASK 3
time = list(range(25))
concentration = [
    12, 14, 15, 17, 20, 23, 27, 30, 32, 31,
    29, 26, 24, 22, 21, 23, 25, 28, 30, 29,
    26, 22, 18, 15, 14
]
h = time[1] - time[0]
n = len(concentration) - 1
interior_sum = sum(concentration[1:-1])
weighted_bracket = (
    concentration[0] + 2 * interior_sum + concentration[-1]
)
total_load = (h / 2) * weighted_bracket
print("\nTASK 3 - POLLUTANT LOAD")
print(f"Number of strips = {n}")
print(f"h = {h} hour")
print(f"Weighted bracket = {weighted_bracket}")
print(f"Total pollutant load = {total_load:.2f} mg*h/L")
plt.plot(time, concentration, marker="o")
plt.xlabel("Time (h)")
plt.ylabel("Concentration (mg/L)")
plt.title("Pollutant Concentration vs Time")
plt.grid(True)
plt.show()