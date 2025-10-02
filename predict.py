"""
Chest X-Ray Pneumonia Prediction
Use trained model to predict on new X-ray images
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import argparse
import os

# Constants
IMG_SIZE = 150
MODEL_PATH = 'best_model.keras'

def load_model(model_path):
    """Load the trained model"""
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")
    
    print(f"Loading model from {model_path}...")
    model = keras.models.load_model(model_path)
    print("Model loaded successfully!")
    return model

def preprocess_image(image_path):
    """Preprocess a single image for prediction"""
    # Load and resize
    img = Image.open(image_path).convert('RGB')
    img = img.resize((IMG_SIZE, IMG_SIZE))
    
    # Convert to array and normalize
    img_array = np.array(img) / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array, img

def predict_image(model, image_path, show=True):
    """Make prediction on a single image"""
    # Preprocess
    img_array, original_img = preprocess_image(image_path)
    
    # Predict
    prediction = model.predict(img_array, verbose=0)[0][0]
    
    # Interpret
    if prediction > 0.5:
        diagnosis = "PNEUMONIA"
        confidence = prediction
        color = 'red'
    else:
        diagnosis = "NORMAL"
        confidence = 1 - prediction
        color = 'green'
    
    # Print results
    print(f"\nPrediction Results:")
    print(f"  Diagnosis: {diagnosis}")
    print(f"  Confidence: {confidence:.2%}")
    print(f"  Raw Score: {prediction:.4f}")
    
    # Show image
    if show:
        plt.figure(figsize=(8, 6))
        plt.imshow(original_img, cmap='gray')
        plt.title(f'Diagnosis: {diagnosis}\nConfidence: {confidence:.2%}', 
                 color=color, fontsize=14, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    return diagnosis, confidence, prediction

def predict_batch(model, image_paths):
    """Predict on multiple images"""
    results = []
    
    print(f"\nProcessing {len(image_paths)} images...\n")
    
    for i, img_path in enumerate(image_paths, 1):
        print(f"[{i}/{len(image_paths)}] {os.path.basename(img_path)}")
        
        try:
            diagnosis, confidence, raw = predict_image(model, img_path, show=False)
            results.append({
                'image': os.path.basename(img_path),
                'diagnosis': diagnosis,
                'confidence': confidence,
                'raw_score': raw
            })
            print(f"  → {diagnosis} ({confidence:.2%})")
            
        except Exception as e:
            print(f"  Error: {str(e)}")
    
    # Summary
    print(f"\nSummary:")
    normal = sum(1 for r in results if r['diagnosis'] == 'NORMAL')
    pneumonia = sum(1 for r in results if r['diagnosis'] == 'PNEUMONIA')
    print(f"  Normal: {normal}")
    print(f"  Pneumonia: {pneumonia}")
    
    return results

def main():
    parser = argparse.ArgumentParser(description='Predict pneumonia from chest X-rays')
    parser.add_argument('images', nargs='+', help='Image file(s) or directory')
    parser.add_argument('--model', default=MODEL_PATH, help='Model path')
    parser.add_argument('--no-show', action='store_true', help='Don\'t display images')
    
    args = parser.parse_args()
    
    # Load model
    model = load_model(args.model)
    
    # Collect image paths
    image_paths = []
    for path in args.images:
        if os.path.isdir(path):
            for ext in ['.jpg', '.jpeg', '.png']:
                image_paths.extend([os.path.join(path, f) for f in os.listdir(path) 
                                   if f.lower().endswith(ext)])
        elif os.path.isfile(path):
            image_paths.append(path)
    
    if not image_paths:
        print("No valid images found!")
        return
    
    # Predict
    if len(image_paths) == 1:
        predict_image(model, image_paths[0], show=not args.no_show)
    else:
        predict_batch(model, image_paths)

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("Chest X-Ray Pneumonia Prediction")
        print("=" * 50)
        print("\nUsage:")
        print("  Single image:")
        print("    python3 predict.py path/to/image.jpg")
        print("\n  Multiple images:")
        print("    python3 predict.py img1.jpg img2.jpg")
        print("\n  Directory:")
        print("    python3 predict.py path/to/images/")
        print("\nOptions:")
        print("  --model PATH    Model file (default: best_model.keras)")
        print("  --no-show       Don't display images")
    else:
        main()