from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = load_iris()
X = data.data
y = data.target
target_names = data.target_names

print("Dataset: Iris")
print(f"Samples: {X.shape[0]} total, {X.shape[1]} features, {len(target_names)} classes")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Split: {X_train.shape[0]} training, {X_test.shape[0]} testing")

k = 5
print(f"Algorithm: k-Nearest Neighbors (k={k})")

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(f"              Predicted")
print(f"              {' '.join(f'{name:>10}' for name in target_names)}")
for i, actual in enumerate(target_names):
    print(f"  {actual:10} {' '.join(f'{cm[i, j]:>10}' for j in range(len(target_names)))}")
