

board_certificate_prompt = """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a board certificate ?  
                if yes then 
                    1. If image/document consist provided name(Name that is present in the provided JSON) 
                    2. check if image/document consist Board Name. If yes then give validation type as yes else give validation as no 
                else give validation type no
                Note - For Name and Board name don't be case sensitive
                Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                Only provide the following JSON Data not anything else
                also give explanation in json 
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """


dea_prompt = """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a DEA Certificate/Document ?  
                if yes then check
                    1. If image/document consist provided name(Name that is present in the provided JSON) 
                    2. if image/document consist License Number. If yes(both correct name and license no. is present) then give validation type as yes else give validation as no 
                else give validation type no
                Note - The License Number in the document may appear in a different format than in the JSON. Examples include:
                            - If JSON has 12346, the document may display it as RD12346.
                            - If JSON has PK2244, the document may display it as 2244.
                            - If JSON has RSD6734893, the document may display it as RSD-6734893.
                       For Name don't be case sensitive
                       Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                       License  No. and DEA No. are same thing here.
                       First Name and Last Name can be reverse because some document are U.S. Based and Document can be having no middle name or having first initial of middle name.
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """

pli_prompt = """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a Professional License certificate/Document ?  
                if yes then check
                    1. If image/document consist provided name(Name that is present in the provided JSON) 
                    2. if image/document consist License Number. If yes(both correct name and license no. is present) then give validation type as yes else give validation as no 
                else give validation type no
                Note - The License Number in the document may appear in a different format than in the JSON. Examples include:
                            - If JSON has 12346, the document may display it as RD12346.
                            - If JSON has PK2244, the document may display it as 2244.
                            - If JSON has RSD6734893, the document may display it as RSD-6734893.
                       For Name don't be case sensitive
                       Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                       First Name and Last Name can be reverse because some document are U.S. Based and Document can be having no middle name or having first initial of middle name.
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """


ofac_prompt = """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a OFAC(Office of Foreign Assets Control) Document ?  
                if yes then 
                    1. check if image/document consist provided name(Name that is present in the provided JSON). 
                        If yes(it consist provider name) then find status if matches not found then give validation_type 'yes' else 'no' 
                else give validation type no
                Note - For Name don't be case sensitive
                Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                NPI no. are of always 10 Digit.
                Only provide the following JSON Data not anything else 
                First Name and Last Name can be reverse because some document are U.S. Based and Document can be having no middle name or having first initial of middle name.
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """
sam_prompt = """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a SAM(System for Award Management) Document ?  
                if yes then 
                    1. check in keyword search section if image/document consist provided name(Name that is present in the provided JSON) anywhere in the image  
                        If yes(it consist name) then find status if matches not found then give validation_type 'yes' else 'no' 
                else give validation type no
                Note -For Name don't be case sensitive
                Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                NPI no. are of always 10 Digit.
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """
        

medicare_opt_out_prompt = """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a image/document of search tool interface for the 'Provider Opt-Out Affidavits Look-up Tool'?   
                if yes then 
                    1. check if image/document consist pNPI Number (npi that is present in provided json). 
                        If yes then find status if matches not found then give validation_type 'yes' else 'no' 
                else give validation type no
                Note - For Name don't be case sensitive
                Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                NPI no. are of always 10 Digit.
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """

       
oig_prompt =  """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a O.I.G. (Office Of Inspector General) letter/document ?   
                if yes then 
                    1. check if image/document consist provided name(Name that is present in the provided JSON) anywhere in the image . 
                        If yes(it consist name) then find status if matches found then give validation_type 'no' else 'yes' 
                else give validation type no
                Note - For Name don't be case sensitive
                Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """
npi_prompt = """
                You are a document analyzer. A user sends you an image of a document, and you determine 
                is this snapshot a NPI document/certificate from NPI registry site.
                if yes then 
                    1. If image/document consist provided name(Name that is present in the provided JSON) 
                    2. check if image/document consist NPI Number. If yes then give validation type as yes else give validation as no 
                else give validation type no
                Note - For Name don't be case sensitive
                Provider entire name should be exactly same (except case e.g. uppercase , lower case)
                NPI no. are of always 10 Digit.
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """

caqh_prompt = """
                You are a document analyzer. A user sends you an image of a document, and you determine 
                is this image a CAQH document/summary report.
                if yes then 
                    1. If image/document consist provider name(Name that is present in the provided JSON) 
                    2. check if image/document consist NPI Number. If yes then give validation type as yes else give validation as no 
                else give validation type no
                Note - For Provider Name don't be case sensitive and dont check middle name or middle name initials focus on only first and last name
                NPI no. are of always 10 Digit.
                Only provide the following JSON Data not anything else 
                also give explanation in json
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no",
                            "explanation": "explanation"
                        }}
                    ]
                }}
                """
rough =         """
                You are document extractor. A user sends you a document and you tell them the required information.
                is this a board certificate ?  
                if yes then 
                    1. If image/document consist provided name(Name that is present in the provided JSON) 
                    2. check if image/document consist Board Name. If yes then give validation type as yes else give validation as no 
                else give validation type no
                Note - Name and Board name can be case sensitive
                Only provide the following JSON Data not anything else 
                If yes, use the following JSON format: {{
                    "document_info": [
                        {{
                            "validation_type": "yes"
                        }}
                    ]
                }}
                Otherwise, return: {{
                    "document_info": [
                        {{
                            "validation_type": "no"
                        }}
                    ]
                }}
                """