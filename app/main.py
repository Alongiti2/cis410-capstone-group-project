import os
from flask import Flask, render_template_string
import pymysql

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>AI Cloud Security Architects LLC</title>
<style>
  body { font-family: Arial, sans-serif; max-width: 800px; margin: 60px auto; padding: 20px; }
  h1 { color: #1a73e8; }
  .status { padding: 12px; border-radius: 6px; margin: 10px 0; }
  .ok { background: #e6f4ea; color: #137333; }
  .err { background: #fce8e6; color: #c5221f; }
</style></head>
<body>
<h1>AI Cloud Security Architects LLC</h1>
<p>Secure cloud infrastructure — CIS 410 Capstone</p>
<h2>System Status</h2>
{% if db_ok %}
  <div class="status ok">✓ Cloud SQL connected successfully</div>
{% else %}
  <div class="status err">✗ Cloud SQL connection failed: {{ db_error }}</div>
{% endif %}
<div class="status ok">✓ Application running on Cloud Run</div>
<h2>Team</h2>
<ul>
  <li>Delphin Zaki — Project Lead</li>
  <li>Abduba — Team Member</li>
  <li>Sayed — Team Member</li>
  <li>Seela — Team Member</li>
  <li>Asefa — Team Member</li>
  <li>Elis — Team Member</li>
  <li>Sahil — Team Member</li>
</ul>
</body></html>
"""

@app.route("/")
def index():
    db_ok = False
    db_error = ""
    try:
        db_pass = open("/run/secrets/db-password").read().strip() if os.path.exists("/run/secrets/db-password") else os.environ.get("DB_PASSWORD", "")
        conn = pymysql.connect(
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            user=os.environ.get("DB_USER", "app"),
            password=db_pass,
            database=os.environ.get("DB_NAME", "appdb"),
            connect_timeout=3
        )
        conn.close()
        db_ok = True
    except Exception as e:
        db_error = str(e)
    return render_template_string(HTML, db_ok=db_ok, db_error=db_error)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
