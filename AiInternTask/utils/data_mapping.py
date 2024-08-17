import json

def map_data(object_id, description, text_data, summary):
    data = {
        "object_id": object_id,
        "description": description,
        "text_data": text_data,
        "summary": summary
    }
    return data

if __name__ == "__main__":
    object_id = "object_0"
    description = "a book"
    text_data = "The Art of Computer Programming"
    summary = "This object appears to be a book. Extracted text: The Art of Computer Programming."
    mapped_data = map_data(object_id, description, text_data, summary)
    print(json.dumps(mapped_data, indent=4))
