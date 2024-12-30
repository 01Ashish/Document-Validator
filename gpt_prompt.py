import base64
import json
import requests
import os
from prompts_to_json import regex_search,convert_keys_to_camel_case,rename_degree_key
from dotenv import load_dotenv
from prompt import board_certificate_prompt, dea_prompt, pli_prompt, ofac_prompt, sam_prompt, medicare_opt_out_prompt, oig_prompt, npi_prompt, caqh_prompt 


load_dotenv()
api_key = os.getenv("api_key")

def process_image_first(image_path,user_input):
    
    
    if user_input["document_name"] == "npi":
        prompt = npi_prompt
    elif user_input["document_name"] == "caqh":
        prompt = caqh_prompt
    elif user_input["document_name"] == "dea":
        prompt = dea_prompt
    elif user_input["document_name"] == "professional_license":
        prompt = pli_prompt
    elif user_input["document_name"] == "ofac":
        prompt = ofac_prompt
    elif user_input["document_name"] == "sam":
        prompt = sam_prompt
    elif user_input["document_name"] == "medicare_opt_out":
        prompt = medicare_opt_out_prompt
    elif user_input["document_name"] == "oig":
        prompt = oig_prompt
    elif user_input["document_name"] == "board_certificate":
        prompt = board_certificate_prompt
    
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode("utf-8")

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-turbo",
    "messages": [
        {
            "role" : "system",
            "content" : prompt
        },
        {
        "role": "user",
        "content": [            
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            },
            f"Provided JSON Data to validate - {user_input}"
        ]
        }
    ],
    "max_tokens": 300,
    "temperature": 0.2
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
     # Check for response status and handle errors
    if response.status_code != 200:
        print("API Error:", response.status_code, response.text)
        return {"error": "API request failed", "details": response.text}

    # Try to parse the response, with error handling
    try:
        data = response.json()
        if "choices" in data:
            # Access the content safely
            var = data['choices'][0]['message']['content']
            print(var)
        else:
            print("Unexpected response format:", data)
            return {"error": "Unexpected response format", "details": data}
    except Exception as e:
        print("Error parsing JSON response:", e)
        return {"error": "JSON parsing error", "details": str(e)}
    # print(var)
    # board_name,line_of_business,license_number,issue_date, issued_to = regex_search_pli(var)
    # print("***************")
    # print(board_name,line_of_business,license_number,issue_date, issued_to)
    # return board_name,line_of_business,license_number,issue_date, issued_to
    try:
        result =  regex_search(var)
    except:
        result = var
    converted_data = convert_keys_to_camel_case(result)
    # if len(converted_data["documentInfo"][0].keys())>1:
    #     print(len(converted_data["documentInfo"][0].keys()))
    #     converted_data["documentInfo"][0]["validationType"]='yes'
    # else:
    #     converted_data
    return converted_data


def process_image_second(image_path):
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode("utf-8")

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role" : "system",
            "content" : """You are document extractor. A user sends you an image of a document and you tell them the required information.
            is this IRS Letter ? 
            if yes use the
            following JSON format: {
            "document_info":[
            {
            "key":"value"
            }
            ],
            }
           else "document_info":[
                {
                    'validation_type':"no"
                }
                ]"""
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "What is the business_name, tax_id_number ,employer_identification_number,validation_type,state"
            },
            {
            "type": "image_url", 
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    var = response.json()['choices'][0]['message']['content']
    # print(var)
    # name_of_business, tax_id_number, employer_identification_number = regex_search_irs(var)
    # print("***************")
    # print(name_of_business, tax_id_number, employer_identification_number)
    # return name_of_business, tax_id_number, employer_identification_number
    try:
        result =  regex_search(var)
    except:
        result = var
    converted_data = convert_keys_to_camel_case(result)
    if len(converted_data["documentInfo"][0].keys())>1:
        # print(len(converted_data["documentInfo"][0].keys()))
        converted_data["documentInfo"][0]["validationType"]='yes'
    else:
        converted_data
    return converted_data

def process_image_third(image_path):
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode("utf-8")

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role" : "system",
            "content" : """You are document extractor. A user sends you an image of a document and you tell them the required information.
            is this the bank letter?
            if yes, then
            Use the following JSON format: {
            "document_info":[
            {
            "key":"value"
            }
            ],
            }
           else "document_info":[
                {
                    'validation_type':"no"
                }
                ]"""
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "What is the account_name, account_number, routing_number , account_type, validation_type, state, bank_name"
            },
            {
            "type": "image_url", 
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    var = response.json()['choices'][0]['message']['content']
    # print(var)
    # account_name,account_number,routing_number,aba = regex_search_bankLetter(var)
    # print("***************")
    # print(account_name,account_number,routing_number,aba)
    # return account_name,account_number,routing_number,aba
    try:
        result =  regex_search(var)
    except:
        result = var
    converted_data = convert_keys_to_camel_case(result)
    if len(converted_data["documentInfo"][0].keys())>1:
        # print(len(converted_data["documentInfo"][0].keys()))
        converted_data["documentInfo"][0]["validationType"]='yes'
    else:
        converted_data
    return converted_data


def process_image_fourth(image_path):
    with open(image_path, "rb") as image:
        base64_image = base64.b64encode(image.read()).decode("utf-8")

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4o",
    "messages": [
        {
            "role" : "system",
            "content" : """You are document extractor. A user sends you an image of a document and you tell them the required information.
            is this the clinical laboratory improvement ammendments document?
            if yes,then
            Use the following JSON format: {
            "document_info":[
            {
            "key":"value"
            }
            ],
            }
            else "document_info":[
                {
                    'validation_type':"no"
                }
                ]
                **When extracting the dates, ensure it is in the yyyy-mm-dd format.**
                """
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "find clia_id, start_date, expiration_date ,business_name , certification_type,validation_type,state"
            },
            {
            "type": "image_url", 
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    var = response.json()['choices'][0]['message']['content']
    # print(var)
    # clia_id, start_date, expiration_date ,business_name , certification_type = regex_search_clia(var)
    # print("***************")
    # print(clia_id, start_date, expiration_date ,business_name , certification_type)
    # return clia_id, start_date, expiration_date ,business_name , certification_type
    try:
        result =  regex_search(var)
    except:
        result = var
    converted_data = convert_keys_to_camel_case(result)
    if len(converted_data["documentInfo"][0].keys())>1:
        # print(len(converted_data["documentInfo"][0].keys()))
        converted_data["documentInfo"][0]["validationType"]='yes'
    else:
        converted_data
    return converted_data


