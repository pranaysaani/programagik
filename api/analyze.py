# This function is called whenever someone accesses /api/analyze

def handler(request):
    return {
        "statusCode": 200,
        "body": "Hello from Python!"
    }