from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def hello_backend():
    try:
        if request.method == "GET":
            print("Received POST Request")
            return "Hello Backend", 201
    except Exception as e:
        print(f"Error : {e}")

    return "GET Request failed", 404

@main.route('/about_me', methods=['GET', 'POST', 'PUT', 'DELETE'])
def about_me():
    global data
    try:
        if request.method == "POST" or request.method == "PUT":
            print(f"Received {request.method} Request")

            data = request.get_json(force=True)

            return "Data received", 201
        
        if request.method == "GET":
            print("Received GET Request")
            return jsonify(data), 201
        
        if request.method == "DELETE":
            print("Received DELETE Request")
            del data
            return "Data deleted", 201

    except Exception as e:
        print("Hi")
        print(f"Error : {e}")

    return f"{request.method} Request failed", 404