from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input:
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                response = completion.choices[0].message["content"].strip()
            except Exception as e:
                response = f"Error: {str(e)}"
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))