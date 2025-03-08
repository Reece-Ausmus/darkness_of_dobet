from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)  # Enable CORS to allow communication with the frontend

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAP_FILE = os.path.join(BASE_DIR, "map.json")

@app.route('/get_map', methods=['GET'])
def get_map():
  try:
    # Read the JSON file
    with open(MAP_FILE, 'r') as file:
      data = json.load(file)

    # Return the data as a JSON response
    return jsonify(data), 200
  except FileNotFoundError:
    print("NO MAP")
    return jsonify({"error": "Map file not found"}), 404
  except json.JSONDecodeError:
    return jsonify({"error": "Error decoding JSON"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
