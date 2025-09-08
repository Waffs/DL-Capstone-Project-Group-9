# Install dependencies
# !pip install gradio torch torchvision --quiet

import gradio as gr
from PIL import Image
import torch
from torchvision import transforms
import torch.nn as nn
from torchvision.models import efficientnet_b0

# Define class names
class_names = ['fulani', 'hausa', 'igbo', 'yoruba']  # Replace with your actual classes

# Define the model architecture
def get_model(num_classes):
    model = efficientnet_b0(pretrained=False)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    return model

# Initialize and load the model weights
model = get_model(len(class_names))
model.load_state_dict(torch.load('efficientnetb0_weights.pth', map_location='cpu'))  # Your saved state_dict path
model.eval()

# Define image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Define prediction function
def predict(image):
    try:
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)
        image = transform(image).unsqueeze(0)
        with torch.no_grad():
            outputs = model(image)
            print("Logits:", outputs)  # see raw predictions
            probs = torch.softmax(outputs, dim=1)
            print("Probabilities:", probs)
            _, predicted = torch.max(outputs, 1)
        return class_names[predicted.item()]
    except Exception as e:
        return f"Error: {str(e)}"



# Launch Gradio interface
gr.Interface(fn=predict, inputs="image", outputs="label", 
             title="Nigerian Attire Classifier",
             description="Upload an image of Nigerian attire to classify it as Fulani, Hausa, Igbo, or Yoruba.").launch()
