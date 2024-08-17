def summarize_attributes(description, text_data):
    summary = f"This object appears to be {description}. Extracted text: {text_data}."
    return summary

if __name__ == "__main__":
    description = "a book"
    text_data = "The Art of Computer Programming"
    summary = summarize_attributes(description, text_data)
    print(summary)
