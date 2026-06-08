import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>AI Cloud Security Architects</title></head>
<body style="font-family:Arial;max-width:800px;margin:50px auto;padding:20px">
<h1>AI Cloud Security Architects Platform</h1>
<p>Automated threat detection, vulnerability scanning, and compliance monitoring.</p>
<h2>Status</h2>
<p style="color:green">&#10003; Application Running</p>
<p style="color:green">&#10003; Security Dashboard Active</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "ai-cloud-security"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

