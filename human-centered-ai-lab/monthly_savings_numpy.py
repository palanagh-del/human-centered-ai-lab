# Monthly Savings Analysis Using NumPy

## Code

```python
import numpy as np

monthly_savings = np.array([5000, 7000, 6000, 8000, 7500, 9000])
print("Monthly savings data:")

print(monthly_savings)

# Calculate the total sum of monthly savings
total_savings = np.sum(monthly_savings)
print(f"Total monthly savings: {total_savings}")

# Find the maximum monthly savings
max_savings = np.max(monthly_savings)
print(f"Maximum monthly savings: {max_savings}")

# Calculate the average monthly savings
average_savings = np.mean(monthly_savings)
print(f"Average monthly savings: {average_savings}")

# Calculate the standard deviation of monthly savings
std_savings = np.std(monthly_savings)
print(f"Standard deviation of monthly savings: {std_savings:.2f}")

# Calculate the variance of monthly savings
var_savings = np.var(monthly_savings)
print(f"Variance of monthly savings: {var_savings:.2f}")

# Calculate the median of monthly savings
median_savings = np.median(monthly_savings)
print(f"Median of monthly savings: {median_savings}")

Monthly savings data:
[5000 7000 6000 8000 7500 9000]
Total monthly savings: 42500
Maximum monthly savings: 9000
Average monthly savings: 7083.333333333333
Standard deviation of monthly savings: 1328.77
Variance of monthly savings: 1763888.89
Median of monthly savings: 7250.0
Index of month with maximum savings: 5
# Find the index of the month with maximum savings
max_savings_index = np.argmax(monthly_savings)
print(f"Index of month with maximum savings: {max_savings_index}")
