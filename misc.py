def error_processing(response_data, success_code: int, failure_code: int, function_to_return=None):

    def check_error(response):
        if 'error' in response:
            return response, failure_code
        else:
            return response, success_code

    if function_to_return:
        return check_error(function_to_return)
    else:
        return check_error(response_data)