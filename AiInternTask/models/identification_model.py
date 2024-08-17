import torch
import torchvision

def identify_objects(image_path):
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    img = Image.open(image_path)
    transform = T.Compose([T.ToTensor()])
    img = transform(img)

    with torch.no_grad():
        prediction = model([img])

    return prediction

if __name__ == "__main__":
    image_path = 'data/segmented_objects/object_0.png'
    prediction = identify_objects(image_path)
    print(prediction)
