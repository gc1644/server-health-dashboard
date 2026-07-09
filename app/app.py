from flask import Flask

from system import get_system_info

app = Flask(__name__)

@app.route("/system")
def home():
    return get_system_info()

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
