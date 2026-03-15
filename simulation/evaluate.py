import torch
import numpy as np
from src.models.gru_model import IntrusionDetectionGRU
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings('ignore')

print("Evaluating latest model...")
# Load the test data
X_test = torch.load('data/processed/X_test.pt')
y_test = torch.load('data/processed/y_test.pt')

# Load the verified model
model = IntrusionDetectionGRU()
model.load_state_dict(torch.load('saved_models/local_verified_gru.pth', map_location='cpu'))
model.eval()

# To binary classification (0 = Benign, 1 = Any Attack)
y_test_binary = (y_test != 0).long()

with torch.no_grad():
    outputs = model(X_test)
    predictions = torch.argmax(outputs, dim=1)
    predictions_binary = (predictions != 0).long()

cm = confusion_matrix(y_test_binary.numpy(), predictions_binary.numpy())
tn, fp, fn, tp = cm.ravel()
accuracy = (tn + tp) / (tn + fp + fn + tp)

print(f"\nTotal Samples: {len(y_test)}")
print(f"Accuracy: {accuracy*100:.2f}%")
print("\nConfusion Matrix:")
print("                 Predicted Benign | Predicted Attack")
print(f"Actual Benign | {tn:14d} | {fp:15d}")
print(f"Actual Attack | {fn:14d} | {tp:15d}")
