# import gradio as gr

# def greet(name):
#     return "Hello " + name + "!!"

# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo.launch()

from fastai.vision.all import *
import gradio as gr

def is_cat(x): return x[0].isupper()

<<<<<<< HEAD
learn = load_learner('bone-model.pkl')
=======
learn = load_learner('bone_model.pkl')
>>>>>>> 39037b2 (migrate)

categories = ('bone', 'broken bone')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

image = gr.Image(type='pil')
label = gr.Label()
<<<<<<< HEAD
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']
=======
examples = ['broken_bone.png', 'bone1.jpg']
>>>>>>> 39037b2 (migrate)

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch()
