import cv2
import numpy as np
import matplotlib.pyplot as plt
from transformers import pipeline, DepthEstimationPipeline

estimator = pipeline(task="depth-estimation", model="Intel/dpt-large")

# image = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = "https://plus.unsplash.com/premium_photo-1695517712559-8f89dd1aa69b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

result = estimator(images=image)
np_image = np.squeeze(np.array(result["predicted_depth"].cpu().detach().numpy(), dtype=np.uint8))

print("max value:", np.max(np_image))
print("min value:", np.min(np_image))

fig = plt.figure()
plt.imshow(np_image, cmap='gray')
plt.show()