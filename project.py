from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt(text, key):
    encrypted = ""
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - 65
            encrypted += chr((x + key) % 26 + 65)
        else:
            encrypted += char
    return encrypted


def decrypt(text, key):
    decrypted = ""
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - 65
            decrypted += chr((x - key) % 26 + 65)
        else:
            decrypted += char
    return decrypted


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        key = int(request.form["key"])
        result = encrypt(message, key)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)