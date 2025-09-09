# 💊 Data Doctor 💊

**Data Doctor** is a Python library for cleaning, preprocessing, transforming, and validating pandas DataFrames with an optional PyQt GUI for non-technical users.

---

## Features

- **Data Cleaning**
  - Remove duplicates
  - Fill missing values with mean, median, or custom strategies
  - Standardize string columns (trim, lowercase)
  - Email validation

- **Data Transformation**
  - Normalize numeric columns
  - Encode categorical variables

- **Validation**
  - Check for missing values, duplicates, and column types

- **Pipeline Support**
  - Run cleaning, transformation, and validation in a single workflow

---

## Installation

```bash
# Clone the repo
git clone https://github.com/noahharshbarger/data-doctor.git
cd data-doctor

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install package in editable mode
pip install -e .[dev]
```

## Usage
```bash
import pandas as pd
from data_doctor.cleaner import DataCleaner
from data_doctor.pipeline import DataPipeline

# Example DataFrame
df = pd.DataFrame({
    "name": ["Alice", "Bob", None, "Charlie"],
    "age": [25, None, 30, 22],
    "email": ["alice@test.com", "bob@test.com", "invalid_email", None]
})

# Using DataCleaner
cleaner = DataCleaner(df.copy())
df_cleaned = (cleaner
              .drop_duplicates()
              .fill_missing(strategy="mean")
              .standardize_strings()
              .run_email_validation("email"))

# Using DataPipeline
pipeline = DataPipeline(df.copy())
df_pipeline = (pipeline
               .run_basic_cleaning()
               .run_transformations())
validation_report = pipeline.validate()

print(df_pipeline)
print(validation_report)
```

## Testing
```bash
# Run all tests
pytest tests/ 
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request. 

## Licensure
MIT License
© Noah Harshbarger
