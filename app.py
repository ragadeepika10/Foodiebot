

#testing

from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR OPEN AI API KEY"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"reply": "Error: Message is required."}), 400

    try:
        # Make a request to OpenAI's API
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use gpt-4o if available, otherwise use gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )

        # Extract and send the response back to the frontend
        bot_reply = response.choices[0].message['content'].strip()
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
