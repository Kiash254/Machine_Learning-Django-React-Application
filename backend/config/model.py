import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load the training data
data = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv')

# Clean up column names by removing extra spaces and quotes
data.columns = data.columns.str.strip().str.replace('"', '')

# Print the cleaned column names for verification
print("Cleaned columns in dataset:", data.columns)

# Check if expected columns are available after cleaning
if 'Height(Inches)' in data.columns and 'Weight(Pounds)' in data.columns:
    # Rename columns for convenience
    data = data.rename(columns={
        'Height(Inches)': 'Height',
        'Weight(Pounds)': 'Weight'
    })
    
    # Select feature columns (Height, Weight)
    X = data[['Height', 'Weight']]
    
    # Generate a dummy target variable, for example using even or odd index as class
    y = (data['Index'] % 2).astype(int)  # This will create binary classes: 0 and 1

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X, y)

    # Save the model to disk
    joblib.dump(model, 'model.pkl')
    print("Model trained and saved successfully with a dummy target variable.")
else:
    print("Expected columns 'Height(Inches)' and 'Weight(Pounds)' not found in dataset after cleaning.")
