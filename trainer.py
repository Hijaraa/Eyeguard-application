import os
import cv2
import numpy as np
from PIL import Image

# Ensure you have the required module for face recognition
if not hasattr(cv2, 'face'):
    raise ImportError("cv2.face module is not available in this OpenCV installation.")

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

def get_images_with_ids(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.startswith('.')]
    faces = []
    ids = []
    for single_image_path in image_paths:
        try:
            # Ensure the file is a valid image file
            if single_image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                face_img = Image.open(single_image_path).convert("L")  # Convert to grayscale
                face_np = np.array(face_img, np.uint8)
                # Extract ID from filename
                id_str = os.path.split(single_image_path)[-1].split(".")[1]
                id = int(id_str)
                print(f"Processing file {single_image_path} with ID {id}")
                faces.append(face_np)
                ids.append(id)
                cv2.imshow("training", face_np)
                cv2.waitKey(10)
            else:
                print(f"Skipping non-image file: {single_image_path}")
        except (IndexError, ValueError) as e:
            print(f"Skipping file {single_image_path}: {e}")

    return np.array(ids), faces

# Get the image paths and IDs
ids, faces = get_images_with_ids(path)
if len(faces) == 0 or len(ids) == 0:
    raise ValueError("No valid images found for training.")

# Train the recognizer
recognizer.train(faces, ids)
# Save the trained model
recognizer.save("recognizer/trainingdata.yml")
cv2.destroyAllWindows()
