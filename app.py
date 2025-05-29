from flask import Flask, request, render_template, jsonify
import os
import fitz  # PyMuPDF
from werkzeug.utils import secure_filename
import glob
import requests
import base64
import json
import uuid
from gpt_prompt import process_image_first,process_image_second,process_image_third,process_image_fourth

app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'uploads'
PDF_FOLDER = os.path.join(UPLOAD_FOLDER, 'pdf')
IMAGE_FOLDER = os.path.join(UPLOAD_FOLDER, 'images')
CONVERTED_FOLDER = os.path.join(UPLOAD_FOLDER, 'converted')

for folder in [PDF_FOLDER, IMAGE_FOLDER, CONVERTED_FOLDER]:
    os.makedirs(folder, exist_ok=True)
[os.remove(f) for f in glob.glob(os.path.join(PDF_FOLDER, "*"))]
[os.remove(f) for ext in ('*.jpeg', '*.jpg', '*.png') for f in glob.glob(os.path.join(UPLOAD_FOLDER, ext))]
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_pdf_to_images(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image_filename = os.path.join(output_folder, f'page_{page_num + 1}.png')
        pix.save(image_filename)
        break
    return image_filename

def prompts_callback(image_file_path,user_input):
    # if document_name =='npi' or document_name =='caqh' : 
    #     result = process_image_first(image_file_path,user_input)
    # elif document_name =='professional license' or document_name =='dea':
    #     result = process_image_first(image_file_path,user_input)
    # elif document_name =='oig' or document_name =='ofac' or document_name =='sam' or document_name =='medicare opt out':
    #     result = process_image_first(image_file_path,user_input)
    # elif document_name =='board certificate':
    #     result = process_image_first(image_file_path,user_input)
    # else :
    #     result = "Invalid document name"   
    result = process_image_first(image_file_path,user_input) 

    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    user_input = request.form['user_input']
    file_url = request.form['file_url']
    
    try:
        user_input1 = json.loads(user_input)  # Convert string to JSON
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}, 400
    response = requests.get(file_url)
    if response.status_code == 200:    
        # Get the content type from the response headers
        content_type = response.headers.get('Content-Type')
        print("content_type: ", content_type)
        if 'pdf' in content_type:
            file_extension = 'pdf'            
        elif 'image' in content_type:
            if 'jpeg' in content_type:
                file_extension = 'jpg'
            elif 'jpg' in content_type:
                file_extension = 'jpg'
            elif 'png' in content_type:
                file_extension = 'png'
        elif 'jpg' in content_type:
            file_extension = 'jpg'
        elif 'png' in content_type:
            file_extension = 'png'
                
        content = response.content
        # pure_name = f'file_{1}'
        # extension = file
        unique_id = str(uuid.uuid4())
        ori_img_new = f"{unique_id}.{file_extension}"
        save_folder = PDF_FOLDER        
        # Save the content to a file
        if file_extension=='pdf':    
            image_path = os.path.join(save_folder, ori_img_new)
            
            with open(image_path, 'wb') as file:
                        file.write(content)
            image_file_path = convert_pdf_to_images(os.path.join(save_folder, ori_img_new), CONVERTED_FOLDER)
            print(image_file_path)
            result = prompts_callback(image_file_path,user_input1)   
        else:
            image_path = os.path.join(UPLOAD_FOLDER, ori_img_new)
            with open(image_path, 'wb') as file:
                        file.write(content)
            result = prompts_callback(image_path,user_input1)

        try:
            os.remove(image_path)
            if 'image_file_path' in locals() and os.path.exists(image_file_path):
                os.remove(image_file_path)
        except Exception as e:
            print(f"Error deleting temp files: {e}")
        return result
    
    else:
        return "Failed to fetch"
    

if __name__ == '__main__':
    app.run(debug=True)
    

