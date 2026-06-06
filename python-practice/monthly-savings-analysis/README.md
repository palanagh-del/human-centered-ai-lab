
# Monthly Savings Analysis Using Python and NumPy

## Project overview

This is a beginner Python project where I used NumPy to analyse six months of monthly savings data.

The project stores monthly savings values in a NumPy array and uses basic statistical functions to calculate:

- Total savings
- Maximum savings
- Average savings
- Standard deviation
- Variance
- Median savings
- Index of the month with the highest savings

The project is small, but it shows how Python can be used to organise numerical data, perform calculations, and generate simple insights from personal finance information.

---

## Why I built this project

I built this project as part of my Python learning journey.

My larger goal is to build AI and data-driven tools for personal finance decision support. Before building more advanced systems using LLMs, RAG, Streamlit, and user-facing interfaces, I am first strengthening my foundation in Python, numerical data handling, and simple analysis.

This project helped me practise how raw numbers can be converted into useful financial insights.

---

## Tools used

- Python
- NumPy
- Google Colab
- GitHub

---

## Dataset used

The project uses sample monthly savings data for six months:

```text
[5000, 7000, 6000, 8000, 7500, 9000]
```

These values represent monthly savings amounts in rupees.

---

## Python code

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

# Find the index of the month with maximum savings
max_savings_index = np.argmax(monthly_savings)
print(f"Index of month with maximum savings: {max_savings_index}")
```

---

## Output

```text
Monthly savings data:
[5000 7000 6000 8000 7500 9000]
Total monthly savings: 42500
Maximum monthly savings: 9000
Average monthly savings: 7083.333333333333
Standard deviation of monthly savings: 1328.77
Variance of monthly savings: 1763888.89
Median of monthly savings: 7250.0
Index of month with maximum savings: 5
```

---

## What the results show

The total savings over the six-month period is Rs 42,500.

The maximum monthly savings is Rs 9,000.

The average monthly savings is around Rs 7,083.

The median monthly savings is Rs 7,250.

The standard deviation shows that the monthly savings values vary by around Rs 1,329 from the average.

The highest savings value is at index 5. Since Python indexing starts from 0, index 5 refers to the sixth value in the array.

---

## What I learned

Through this project, I learned how to:

- Import and use NumPy
- Create a NumPy array
- Store financial data in Python
- Use `np.sum()` to calculate total savings
- Use `np.max()` to find the highest value
- Use `np.mean()` to calculate the average
- Use `np.std()` to understand variation
- Use `np.var()` to calculate variance
- Use `np.median()` to find the middle value
- Use `np.argmax()` to find the index of the highest value
- Document code and output clearly on GitHub

---

## Relevance to my larger learning path

This project is part of my broader learning path toward building AI-assisted financial decision-support tools.

It connects basic Python programming with personal finance data analysis. The same kind of logic can later be extended into more advanced projects, such as:

- Budget analysis tools
- Savings trackers
- Personal finance dashboards
- Streamlit apps
- RAG-based finance assistants
- User-facing financial explanation systems

This project is an early step in building the technical foundation needed for more advanced work in human-centered AI, RAG evaluation, and explainable financial decision-support systems.
