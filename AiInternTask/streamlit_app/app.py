import streamlit as st
from segmentation_model import segment_image
from preprocessing import save_segmented_objects
from identification_model import identify_objects
from text_extraction_model import extract_text
from summarization_model import summarize_attributes
from data_mapping import map_data
from visualization import generate_output

def main():
    st.title("AI Image Segmentation and Object Analysis Pipeline")
    
    uploaded_file = st.file_uploader("Choose an image...", type="png")
    if uploaded_file is not None:
        image_path = f"data/input_images/{uploaded_file.name}"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(image_path, caption='Uploaded Image.', use_column_width=True)

        if st.button("Process Image"):
            prediction = segment_image(image_path)
            save_segmented_objects(prediction, image_path)

            object_details = []
            for i in range(len(prediction[0]['masks'])):
                obj_path = f'data/segmented_objects/object_{i}.png'
                description = identify_objects(obj_path)
                text_data = extract_text(obj_path)
                summary = summarize_attributes(description, text_data)
                mapped_data = map_data(f'object_{i}', description, text_data, summary)
                object_details.append(mapped_data)

            generate_output(image_path, object_details)
            st.write(object_details)

if __name__ == "__main__":
    main()
