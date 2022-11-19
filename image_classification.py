from transformers import BeitFeatureExtractor, BeitForImageClassification
from PIL import Image
import requests
import cv2
from torchsummary import summary
import numpy as np


url = 'https://images.unsplash.com/photo-1668027686570-aff6795ed3c1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80' 
image = Image.open(requests.get(url, stream=True).raw)

# image = Image.open("G:\Mijn Drive\Photo\'s\\20171110_112125.jpg")


feature_extractor = BeitFeatureExtractor.from_pretrained('microsoft/beit-base-patch16-224-pt22k-ft22k')
model = BeitForImageClassification.from_pretrained('microsoft/beit-base-patch16-224-pt22k-ft22k')
inputs = feature_extractor(images=image, return_tensors="pt")

# summary(model, input_size=(3, 224, 224))
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 21,841 ImageNet-22k classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])

cv2.imshow('image', np.array(image))
cv2.waitKey(5000)