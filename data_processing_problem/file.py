import pandas as pd
import faker

fake = faker.Faker()

# Number of rows to generate
num_rows = 1000000  # 1 million rows, for example

data = {
    "first_name": [fake.first_name() for _ in range(num_rows)],
    "last_name": [fake.last_name() for _ in range(num_rows)],
    "address": [fake.address() for _ in range(num_rows)]    
}

df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv("input.csv", index=False)