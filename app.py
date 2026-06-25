from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os
import json

# Load environment variables
load_dotenv()

# Load API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ GROQ_API_KEY not found in .env file")
else:
    print("✅ Groq API Key Loaded")

# Initialize Groq Client
client = Groq(api_key=api_key)

# Flask App
app = Flask(__name__)

# PDF Storage
pdf_text = ""

# Chat History File
CHAT_HISTORY_FILE = "chat_history.json"


# Load Existing Chat History
if os.path.exists(CHAT_HISTORY_FILE):

    with open(CHAT_HISTORY_FILE, "r") as file:
        conversation_history = json.load(file)

    print("✅ Previous chat history loaded")

else:

    conversation_history = []

    print("🆕 New chat history created")


# Save Chat History
def save_chat_history():

    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(conversation_history, file, indent=4)


# Home Route
@app.route("/")
def home():

    return render_template("index.html")


# Get Chat History Route
@app.route("/get_history", methods=["GET"])
def get_history():

    return jsonify({"history": conversation_history})


# Chat Route
@app.route("/chat", methods=["POST"])
def chat():

    global pdf_text
    global conversation_history

    try:

        data = request.get_json()

        user_message = data.get("message")

        print(f"\n🧑 User: {user_message}")

        # PDF Context
        if pdf_text.strip() != "":

            system_prompt = f"""
            You are a helpful AI assistant.

            Use the following PDF content when answering user questions.

            PDF Content:
            {pdf_text}
            """

        else:

            system_prompt = """
            You are a helpful AI assistant.
            """

        # Build Messages
        messages = [{"role": "system", "content": system_prompt}] + conversation_history

        # Add User Message
        messages.append({"role": "user", "content": user_message})

        # AI Response
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )

        bot_reply = response.choices[0].message.content

        # print(f"🤖 Bot: {bot_reply}")

        # Save User Message
        conversation_history.append({"role": "user", "content": user_message})

        # Save Bot Reply
        conversation_history.append({"role": "assistant", "content": bot_reply})

        # Save to JSON
        save_chat_history()

        return jsonify({"reply": bot_reply})

    except Exception as e:

        print("❌ ERROR:", e)

        return jsonify({"reply": f"Error: {str(e)}"})


# Upload PDF Route
@app.route("/upload_pdf", methods=["POST"])
def upload_pdf():

    global pdf_text

    try:

        file = request.files["pdf"]

        if not file:

            return jsonify({"message": "No PDF file uploaded"})

        # Read PDF
        reader = PdfReader(file)

        extracted_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                extracted_text += text + "\n"

        pdf_text = extracted_text

        print("✅ PDF Uploaded Successfully")

        return jsonify({"message": "PDF uploaded successfully!"})

    except Exception as e:

        print("❌ PDF ERROR:", e)

        return jsonify({"message": f"Error: {str(e)}"})


# Clear Memory Route
@app.route("/clear_memory", methods=["POST"])
def clear_memory():

    global conversation_history

    conversation_history = []

    save_chat_history()

    print("🗑️ Chat history cleared")

    return jsonify({"message": "Chat history cleared successfully!"})


# Run Flask App
if __name__ == "__main__":

    print("🚀 Starting Flask Server...")

    app.run(host="0.0.0.0", port=5000, debug=True)
