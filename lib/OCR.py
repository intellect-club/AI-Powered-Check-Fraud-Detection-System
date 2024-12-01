import os
import easyocr

reader = easyocr.Reader(['en'])

def extract_rip_from_image(input_file):
    
    try:
        results = reader.readtext(input_file)
        extracted_text = " ".join([res[1] for res in results]) 

        print(f"Extracted Text: {extracted_text}")

        extracted_list = extracted_text.split(' ')

        for i in extracted_list:
            if i.isnumeric() and len(i) == 20:
                return i

    except Exception as e:
        print(f"Error processing {image_file}: {e}")