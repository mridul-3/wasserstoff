import cv2
import os

def save_segmented_objects(prediction, image_path, output_dir='data/segmented_objects/'):
    img = cv2.imread(image_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, mask in enumerate(prediction[0]['masks']):
        mask = mask[0].mul(255).byte().cpu().numpy()
        ret,thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        x, y, w, h = cv2.boundingRect(contours[0])
        segmented_img = img[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(output_dir, f'object_{i}.png'), segmented_img)

if __name__ == "__main__":
    from models.segmentation_model import segment_image
    image_path = 'data/input_images/sample_image.png'
    prediction = segment_image(image_path)
    save_segmented_objects(prediction, image_path)
