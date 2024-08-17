import matplotlib.pyplot as plt
import cv2
import pandas as pd

def generate_output(image_path, mapped_data):
    img = cv2.imread(image_path)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Segmented Objects with Annotations")
    plt.show()

    df = pd.DataFrame(mapped_data)
    print(df)

if __name__ == "__main__":
    image_path = 'data/input_images/sample_image.png'
    mapped_data = [{
        "object_id": "object_0",
        "description": "a book",
        "text_data": "The Art of Computer Programming",
        "summary": "This object appears to be a book. Extracted text: The Art of Computer Programming."
    }]
    generate_output(image_path, mapped_data)
