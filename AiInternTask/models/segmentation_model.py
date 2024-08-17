import torch
import torchvision
from PIL import Image
import torchvision.transforms as T

def segment_image(image_path):
    model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    img = Image.open(image_path)
    transform = T.Compose([T.ToTensor()])
    img = transform(img)

    with torch.no_grad():
        prediction = model([img])

    return prediction

if __name__ == "__main__":
    image_path = 'data/input_images/sample_image.png'
    prediction = segment_image(image_path)
    print(prediction)
