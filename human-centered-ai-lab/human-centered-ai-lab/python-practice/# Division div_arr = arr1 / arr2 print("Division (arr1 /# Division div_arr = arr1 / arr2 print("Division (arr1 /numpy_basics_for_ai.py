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

# Find the index of the month with maximum savings
max_savings_index = np.argmax(monthly_savings)
print(f"Index of month with maximum savings: {max_savings_index}")
