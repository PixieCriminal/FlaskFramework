from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        'id': 1, 
        'title': 'Groceries',
        'description': 'Milk, bread, ice cream, tomatoes, capsicums, chillies, rice, ladyfingers, apples',
        'done': False
    },
    {
        'id': 2
        'title': 'Books'
        'description': 'Grit, Harry Potter And The Cursed Child, Little Women, Oliver Twist, Moby Dick, Tom Gates: Excellent Excuses, Tom Gates: Genius Ideas',
        'done': False
    }

]

@app.route("/add-data", methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data."
        })

task = {
    'id': tasks[-1]['id']+1,
    'title': request.json['title'],
    'description': request.json.get['description'],
    'done': False
}

def add_task():
    if tasks.append(task):
        return jsonify({
            "status": "success",
            "message": "Your task was added successfully."
        })

@app.route("/add-data", methods = ['GET'])
def get_task():
    return jsonify({
        'data': task
    })
