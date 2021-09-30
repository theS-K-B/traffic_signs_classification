import streamlit as st
from PIL import Image, ImageOps
import numpy as np
from keras.models import load_model
model = load_model('traffic_recognition.h5')

classes = { 1:'Speed limit (20km/h)',
    2:'Speed limit (30km/h)',
    3:'Speed limit (50km/h)',
    4:'Speed limit (60km/h)',
    5:'Speed limit (70km/h)',
    6:'Speed limit (80km/h)',
    7:'End of speed limit (80km/h)',
    8:'Speed limit (100km/h)',
    9:'Speed limit (120km/h)',
    10:'No passing',
    11:'No passing veh over 3.5 tons',
    12:'Right-of-way at intersection',
    13:'Priority road',
    14:'Yield',
    15:'Stop',
    16:'No vehicles',
    17:'Veh > 3.5 tons prohibited',
    18:'No entry',
    19:'General caution',
    20:'Dangerous curve left',
    21:'Dangerous curve right',
    22:'Double curve',
    23:'Bumpy road',
    24:'Slippery road',
    25:'Road narrows on the right',
    26:'Road work',
    27:'Traffic signals',
    28:'Pedestrians',
    29:'Children crossing',
    30:'Bicycles crossing',
    31:'Beware of ice/snow',
    32:'Wild animals crossing',
    33:'End speed + passing limits',
    34:'Turn right ahead',
    35:'Turn left ahead',
    36:'Ahead only',
    37:'Go straight or right',
    38:'Go straight or left',
    39:'Keep right',
    40:'Keep left',
    41:'Roundabout mandatory',
    42:'End of no passing',
    43:'End no passing veh > 3.5 tons' }



st.title("Traffic Sign Classification")
st.set_option('deprecation.showfileUploaderEncoding', False)

@st.cache(allow_output_mutation=True)


def load_image(image_file):
	img = Image.open(image_file)
	return img 

def classify(image):
  image = image.resize((32,32))
  image = np.expand_dims(image, axis=0)
  image = np.array(image)
  pred = model.predict([image])[0] 
  pred = np.argmax(pred,axis=0)
  print(pred+1)
  sign = classes[pred+1]
  print(sign)
  st.success(sign)
  meta_img = load_image('Meta\{}.png'.format(pred))
  return meta_img

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    img = load_image(uploaded_file)
    col1, col2 = st.columns(2)
    col1.image(img, width=300, caption=uploaded_file.name)
    if st.button('Classify'):
      meta_img = classify(img)
      col2.image(meta_img, width=300)



    


