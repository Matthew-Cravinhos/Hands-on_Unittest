from test_data import *

ret_val=[] # move the list here so it isn't overwritten each time the function is called
def json_search(key,input_object):
    
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                temp={k:v}
                ret_val.append(temp)
            if isinstance(v, dict):
                json_search(key,v)
            elif isinstance(v, list):
                for item in v:
                    if not isinstance(item, (str,int)):
                        json_search(key,item)
    else:
        for val in input_object:
            if not isinstance(val, (str,int)):
                json_search(key,val)
    return ret_val
print(json_search("issueSummary",data))