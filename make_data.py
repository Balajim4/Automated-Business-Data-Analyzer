import pandas as pd
import random

# Generating 100 rows of fake employee data
data = {
    'Department': ['IT', 'HR', 'Marketing', 'Sales', 'Finance'] * 20,
    'Employee_Age': [random.randint(22, 60) for _ in range(100)],
    'Salary_USD': [random.randint(40000, 120000) for _ in range(100)],
    'Years_at_Company': [random.randint(1, 15) for _ in range(100)]
}

df = pd.DataFrame(data)
df.to_csv('sample_company_data.csv', index=False)
print("CSV created successfully! You can rest your eyes now.")