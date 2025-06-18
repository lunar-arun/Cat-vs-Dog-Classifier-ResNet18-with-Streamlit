import torch
import torchvision.transforms as transforms
import timm

# Determine the device to be used for computation (GPU if available, otherwise CPU)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the ResNet18 model with specific configurations
model = timm.create_model('resnet18', pretrained=False, num_classes=1, drop_rate=0.5)

# Load the model's state dictionary from a saved checkpoint
model.load_state_dict(torch.load('packages/ResNet18_Model/dog_cat_classifier.pth', map_location=device))

# Move the model to the appropriate device
model.to(device)

# Set the model to evaluation mode (important for inference)
model.eval()

# Define image transformations to be applied before feeding the image into the model
transform = transforms.Compose([
    # Resize the image to 128x128 pixels
    transforms.Resize((128, 128)),
    # Convert the image to a tensor
    transforms.ToTensor(),
    # Normalize the image with pre-defined mean and standard deviation values
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Define a function for making predictions based on an input image
def predict_image(image):
    # Apply the transformations to the image and add a batch dimension
    image = transform(image).unsqueeze(0).to(device)
    
    # Perform inference with no gradient calculation (since we are not training)
    with torch.no_grad():
        # Get the model's output
        output = model(image)
        # Apply the sigmoid function to obtain the prediction probability
        prediction_prob = torch.sigmoid(output).item()
    
    # Return 'Cat' if prediction probability is <= 0.5, otherwise return 'Dog'
    return 'Dog' if prediction_prob > 0.5 else 'Cat'
