from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle file upload
        file = request.files.get("file")
        if file:
            # TODO: Process the uploaded image with CNN model
            pass
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
