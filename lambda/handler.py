import json

def lambda_handler(event, context):
    

    response = {}
    print(event)


    statusCode = 200

    response["statusCode"] = statusCode
    response["body"] = json.dumps(event)
    return response
