from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [{"id": 1, "username": "Masai", "caption": "Post1"}]


@app.route("/api/view", methods=["GET"])
def view_posts():
    return jsonify(posts), 200


@app.route("/api/add", methods=["POST"])
def add_posts():
    new_post = request.get_json()
    if "id" not in new_post or "username" not in new_post or "caption" not in new_post:
        return jsonify({"error": "Invalid Data"}), 400
    posts.append(new_post)
    return jsonify({"message": "New Post Added"}), 201


if __name__ == "__main__":
    app.run()
