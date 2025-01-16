from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

def evaluate_model(model, X_train, X_val, y_train, y_val):
    model.fit(X_train, y_train)
    val_pred = model.predict(X_val)
    val_accuracy = accuracy_score(y_val, val_pred)
    return val_accuracy, model

def select_best_model(models, X_train, X_val, y_train, y_val):
    best_accuracy = 0
    best_model = None
    
    for model in models:
        accuracy, trained_model = evaluate_model(model, X_train, X_val, y_train, y_val)
        print(f"Modell: {type(model).__name__}, Validierungs-Accuracy: {accuracy:.4f}")
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = trained_model
    
    return best_model, best_accuracy

def prepare_data(X, y):
    X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_train_full, y_train_full, test_size=0.2, random_state=42)
    return X_train, X_val, X_test, y_train, y_val, y_test 