from flask import Flask, request, render_template, session, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = "your-secret-key"  # セッション保存のため必須（適宜変更してください）

LM_API = os.getenv("LM_API", "http://localhost:1234/v1/chat/completions")

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":
        user_input = request.form["message"]
        session["chat_history"].append({"role": "user", "content": user_input})

        payload = {
            "model": "mistral:instruct",  # LM Studioで使っているモデル名に合わせる
            "messages": session["chat_history"],
            "temperature": 0.7,
            "max_tokens": 1024,
            "stream": False
        }

        headers = {
            "Authorization": "Bearer lm-studio",
            "Content-Type": "application/json"
        }

        try:
            res = requests.post(LM_API, json=payload, headers=headers)
            res.raise_for_status()
            data = res.json()
            assistant_reply = data["choices"][0]["message"]["content"]
        except Exception as e:
            assistant_reply = f"エラー: {str(e)}"

        session["chat_history"].append({"role": "assistant", "content": assistant_reply})
        session.modified = True
        return redirect(url_for("index"))

    return render_template("index.html", chat_history=session["chat_history"])

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
