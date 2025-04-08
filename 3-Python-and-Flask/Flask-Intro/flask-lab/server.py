from flask import Flask, make_response, request
from data import data

# Usually __name__ = __main__
app = Flask("My first app")

# Define a route this way:
@app.route("/")
def home():
    return {"name": "Shahan"}

# Explicitly set response status code
@app.route("/no-content")
def no_content():
    return ("No content found", 404)

# Explicitly set response status code - 2nd way (using make_response())
@app.route("/explicit-status")
def explicit_status():
    resp = make_response("Explicitly setting status code using make_response()")
    resp.status_code = 404
    return resp

# Some exercise
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"message": f"Data of length {len(data)} found"}
        else:
            return {"message": "Data is empty"}, 500
    except NameError:
        return {"message": "Data not found"}, 404
    
# Getting the query params from the URL. In the browser paste: http://127.0.0.1:5000/name_search?q=tanya
@app.route("/name_search")
def name_search():
    """Find a person in the database.

    Returns:
        json: Person if found, with status of 200
        404: If not found
        422: If argument 'q' is missing
    """
    query = request.args.get('q')

    if not query:
        return {"message": "Query parameter 'q' is missing"}, 422
    
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person
        
    return {"message": "Person not found"}, 404

# Dynamic routing
@app.route("/person/<var_name>")
def find_by_uuid(var_name):
    for person in data:
        if person["id"] == str(var_name):
            return person
    return {"message": "Person not found"}, 404

# Defining the http method explicitly
@app.route("/person", methods=['POST'])
def create_person():
    new_person = request.get_json()
    if not new_person:
        return {"message": "Invalid input, no data provided"}, 400
    data.append(new_person)
    return {"message": "Person created successfully"}, 201