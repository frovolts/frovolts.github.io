import pandas as pd

# 1. Load the raw CSV file downloaded directly from Google Forms
df = pd.read_csv("responses.csv")

# 2. Find every hidden "Enter" key (newline) and replace it with [NEWLINE]
df.replace(r'\r\n|\n|\r', ' [NEWLINE] ', regex=True, inplace=True)

# 3. Save the fixed data to a new file that your HTML portal can read flawlessly
df.to_csv("clean_responses.csv", index=False)

print("✨ Success! clean_responses.csv has been generated.")
