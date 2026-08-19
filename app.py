import subprocess
import re
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DMR TG Switcher</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: system-ui, sans-serif; background: #121212; color: #fff; text-align: center; padding-top: 50px; }
        .card { background: #1e1e1e; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
        input { padding: 10px; font-size: 18px; width: 140px; text-align: center; border-radius: 5px; border: 1px solid #444; background: #2a2a2a; color: #fff; }
        button { padding: 10px 20px; font-size: 18px; border-radius: 5px; border: none; background: #007bff; color: white; cursor: pointer; margin-left: 8px; }
        button:hover { background: #0056b3; }
        .msg { margin-top: 15px; font-weight: bold; color: #28a745; }
    </style>
</head>
<body>
    <div class="card">
        <h2>DMR Talkgroup Control</h2>
        <form method="POST">
            <input type="text" name="tg" placeholder="504" required pattern="[0-9]+" autofocus>
            <button type="submit">Submit</button>
        </form>
        {% if msg %}<div class="msg">{{ msg }}</div>{% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    if request.method == "POST":
        tg = request.form.get("tg", "").strip()
        if re.match(r"^\d+$", tg):
            cmd = ["sudo", "/opt/MMDVM_Bridge/dvswitch.sh", "tune", tg]
            try:
                subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                msg = f"Tuned to TG {tg}"
            except Exception as e:
                msg = f"Error: {e}"
        else:
            msg = "Numbers only!"
    return render_template_string(HTML, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
