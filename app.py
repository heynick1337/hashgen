from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hash_result = ""
    error = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        algorithm = request.form.get("algorithm", "md5")

        if not text:
            error = "Please enter some text to hash."
        else:
            try:
                if algorithm == "md5":
                    hash_result = hashlib.md5(text.encode()).hexdigest()
                elif algorithm == "sha1":
                    hash_result = hashlib.sha1(text.encode()).hexdigest()
                elif algorithm == "sha224":
                    hash_result = hashlib.sha224(text.encode()).hexdigest()
                elif algorithm == "sha256":
                    hash_result = hashlib.sha256(text.encode()).hexdigest()
                elif algorithm == "sha384":
                    hash_result = hashlib.sha384(text.encode()).hexdigest()
                elif algorithm == "sha512":
                    hash_result = hashlib.sha512(text.encode()).hexdigest()
                elif algorithm == "sha3_224":
                    hash_result = hashlib.sha3_224(text.encode()).hexdigest()
                elif algorithm == "sha3_256":
                    hash_result = hashlib.sha3_256(text.encode()).hexdigest()
                elif algorithm == "sha3_384":
                    hash_result = hashlib.sha3_384(text.encode()).hexdigest()
                elif algorithm == "sha3_512":
                    hash_result = hashlib.sha3_512(text.encode()).hexdigest()
                elif algorithm == "blake2s":
                    hash_result = hashlib.blake2s(text.encode()).hexdigest()
                elif algorithm == "blake2b":
                    hash_result = hashlib.blake2b(text.encode()).hexdigest()
                elif algorithm == "shake_128":
                    # shake_128 needs a length — 32 bytes = 64 hex chars
                    hash_result = hashlib.shake_128(text.encode()).hexdigest(32)
                else:
                    error = "Unknown algorithm selected."
            except Exception as e:
                error = f"Error generating hash: {str(e)}"

    return render_template("index.html", hash_result=hash_result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
