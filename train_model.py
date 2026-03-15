import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

X = data[['python_skill','problem_solving','coding_experience']]
y = data['level']

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

# Save model
pickle.dump(model, open("skill_model.pkl","wb"))

print("Model trained successfully")