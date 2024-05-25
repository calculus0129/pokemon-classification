from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from keras.models import load_model
import sys
import json


def preprocess_image(image_path, target_size):
    # Load the image
    img = load_img(image_path, target_size=target_size)
    # Convert the image to an array
    img_array = img_to_array(img)
    # Expand dimensions to match the batch size
    img_array = np.expand_dims(img_array, axis=0)
    # Normalize the image
    img_array /= 255.0
    return img_array

def predict(model, labels, image_path = 'example.gif'):
    # Example usage
    processed_image = preprocess_image(image_path, target_size=(224, 224))

    predictions = model.predict(processed_image)
    # print(predictions.shape) # (1, 307)
    # print(predictions)  # Outputs probability for each class
    pred_idx = np.argmax(predictions, axis=1)[0]

    predicted_label = labels[pred_idx]
    prob = predictions[0,pred_idx]
    return predicted_label, prob

if __name__ == '__main__':
    
    if len(sys.argv)-1 < 1:
        print(f'usage: python {sys.argv[0]} <image file name>')
        exit(0)
    model=load_model('pokemon_classifier_vgg16_1_model.h5')
    labels = []
    # Load list from a file
    with open('labels.json', 'r') as file:
        labels = json.load(file)

    print(f'length of labels: {len(labels)}')
    
    for i in sys.argv[1:]:
        print(predict(model, labels, i))
