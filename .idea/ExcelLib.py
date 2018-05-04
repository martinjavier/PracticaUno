# Import `os`
import os
# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'LIBRO1.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('HOJA1')
