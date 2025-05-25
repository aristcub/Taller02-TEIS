from flask import Flask, render_template
from app_poke.routes import pokenea_bp
import os

app = Flask(
    __name__,
    template_folder=os.path.join("app", "templates"),
    static_folder=os.path.join("app", "static")
)

app.register_blueprint(pokenea_bp, url_prefix="/pokenea")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
