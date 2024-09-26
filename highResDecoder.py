#TODO: Make this work with GIT

import base64

def decode_base64_image(base64_string, output_file_path):
    try:
        image_data = base64.b64decode(base64_string)

        with open(output_file_path, 'wb') as image_file:
            image_file.write(image_data)
        
        print(f"Image successfully saved as {output_file_path}")

    except Exception as e:
        print(f"Error decoding image: {e}")

base64_image = "YOUR_BASE64_HIGHRES_IMAGE/VIDEO_STRING_HERE"

try:
    base64_image = base64_image + "="
except:
    base64_image = base64_image + "=="    
decode_base64_image(base64_image, 'output_image.jpg')
