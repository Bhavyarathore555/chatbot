# DreamTeam Chatbot

## Overview

DreamTeam Chatbot is an intelligent AI-powered chatbot designed to provide interactive conversations with multiple advanced features like PDF document support, voice input, and chat history storage.

The chatbot allows users to ask questions, upload PDFs for context-based responses, interact using voice commands, and revisit previous conversations through stored chat history.

## Features

### AI Chat System

* Real-time conversation with the chatbot.
* Fast and interactive responses.

### PDF Support

* Upload PDF files.
* Extract and analyze PDF content.
* Ask questions based on uploaded documents.

### Voice Input

* Speak directly to the chatbot using microphone input.
* Converts speech into text for interaction.

### Chat History

* Automatically saves previous conversations.
* Allows users to review old chats.

### User-Friendly Interface

* Simple and clean UI.
* Easy interaction for both text and voice.

## How It Works

1. Open the chatbot interface.
2. Type a question or use voice input.
3. Upload a PDF for document-based questions.
4. The chatbot processes the input.
5. Responses are generated instantly.
6. Chat history is saved automatically.

## Tech Stack

* Python
* Flask
* HTML
* CSS
* JavaScript
* SQLite / JSON (for chat history)
* Speech Recognition
* PyPDF2 / PDFPlumber
* AI API Integration

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/DreamTeam-Chatbot.git
cd DreamTeam-Chatbot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000/
```

## Project Structure

DreamTeam-Chatbot/
│── app.py
│── templates/
│── static/
│── uploads/
│── chat_history/
│── requirements.txt
│── README.md

## Future Improvements

* Multi-language support
* File support beyond PDFs
* User authentication
* Cloud chat history storage

