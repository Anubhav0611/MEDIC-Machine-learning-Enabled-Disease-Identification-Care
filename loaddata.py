import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load the Excel file
df = pd.read_csv('Training.csv')  # Use sheet_name='Sheet1' if needed


# Split features and label
X = df.drop('prognosis', axis=1)
y = df['prognosis']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape)
# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Save the model to a file
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('random_forest_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Step 7: Predict on test data
y_pred = loaded_model.predict(X_test)

# Step 8: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy * 100:.2f}%\n")

print("📊 Classification Report:")
print(classification_report(y_test, y_pred))