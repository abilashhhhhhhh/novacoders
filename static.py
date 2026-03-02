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


# Main Program
msg = input("Enter Message: ")
key = int(input("Enter Key (Shift Value): "))

cipher = encrypt(msg, key)
print("\nEncrypted Message:", cipher)

plain = decrypt(cipher, key)
print("Decrypted Message:", plain)

# verification input
verify = input(
    "\nEnter Key OR Encrypted Message to execute original message: "
)

if verify == str(key) or verify.upper() == cipher:
    print("Original Message:", msg.upper())
else:
    print("Verification failed! Message not executed.")
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)