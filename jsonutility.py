import json

print ('Hello World')

def normalize(data):
    if isinstance(data,str):
        return normalize_json(data)
    elif isinstance(data,(list,tuple,set)):
        return normalize_array(data)
    elif isinstance(data,(dict)):
        return normalize_map(data)
    else:
        return data


#Check if String is JSON
def is_json(data);
    try:
        json_object = json.loads(data)
    except ValueError as e:
        return False
    return True
    
#Convert JSON String to JSON
def to_json(data):
    if is_json(data):
        return json.loads(data)

#Convert 
def normalize_array():
    pass

def normalize_json():
    pass

def normalize_map():
    pass
