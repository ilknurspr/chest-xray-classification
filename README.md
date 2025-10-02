# Chest X-Ray Pneumonia Detection

A CNN-based project for detecting pneumonia from chest X-ray images.

## What's This About?

I built a convolutional neural network that can look at chest X-rays and identify whether someone has pneumonia or not. It's a binary classifier that works pretty well - getting around 90%+ accuracy on the test set.

## Dataset

I used the Chest X-Ray Images dataset from Kaggle. It's got about 5,800 labeled X-ray images split into normal and pneumonia cases.

**Get the data:**
- Go to [this Kaggle dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- Download it (you'll need a Kaggle account)
- Unzip into a folder called `chest_xray`

The folder structure should look like:
chest_xray/
├── train/
├── test/
└── val/

## Running It

**Install dependencies:**
```bash
pip install tensorflow numpy matplotlib pillow scipy
Train the model:
bashpython3 train_model.py
It'll take a while - about an hour on CPU, maybe 15-20 minutes if you've got a GPU.
What I Built
The architecture is pretty straightforward:

4 convolutional blocks with batch normalization
Max pooling after each block
Dropout layers to prevent overfitting
Dense layer at the end for classification

I added some data augmentation (rotation, zoom, flips) to make it more robust since medical images can vary a lot.

## Results

After training for 10 epochs on my M1 Mac:
- Training accuracy: ~96%
- Test accuracy: **87.5%**
- AUC score: **95.4%**
- Training time: ~6 minutes (M1 chip)
