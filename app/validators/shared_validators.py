def check_fields(form_data, data_keys):
    """ Validates that all fields have been provided with data """
    keylist = []
    error_message = {}
    if not form_data:
            error_message['data error'] = "No data found"
    else:
        for input_key, input_value in form_data.items():
            keylist.append(input_key)
        
        for key_item in data_keys:
            """ Confirms all field are provided """
            if key_item not in keylist:
                error_message['key error'] = "{} is missing".format(key_item)
            else:
                if type(form_data[key_item]) is str:
                    if form_data[key_item].strip() == "":
                        """ Confirms all fields have values """
                        error_message['value error'] = "{} is missing a value".format(key_item)
                else:
                    pass
    return error_message