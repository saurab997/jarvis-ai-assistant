# Jarvis AI Assistant

A voice-controlled AI assistant built with Python that can perform tasks like opening websites, playing music, fetching news, and answering questions using OpenAI.

---

## Features

* Voice Recognition
* Wake Word Detection ("Jarvis")
* AI-Powered Responses
* Music Playback
* Browser Automation
* News Fetching
* Text-to-Speech Responses
* Modular Project Structure

---

## Technologies Used

* Python
* OpenAI API
* SpeechRecognition
* gTTS
* pygame
* requests
* pyttsx3

---

## Project Structure

```bash
jarvis-ai-assistant/
│
├── assets/
│   └── screenshots/
│
├── data/
│   └── history.json
│
├── modules/
│   ├── ai.py
│   ├── commands.py
│   ├── musiclibrary.py
│   ├── news.py
│   └── speech.py
│
├── .env
├── .gitignore
├── client.py
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate virtual environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux/Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_newsapi_key
```

---

## Run the Project

```bash
python main.py
```

---

## Example Commands

* "Jarvis"
* "Open Google"
* "Open YouTube"
* "Play Yellow"
* "Tell me the news"
* "What is artificial intelligence?"

---

## Screenshots

```bash
assets/screenshots/
```
---

## Future Improvements

* Chat history storage
* Weather updates
* PDF summarization
* Face recognition login
* Mobile application
* Smart home integration

---

## Learning Outcomes

This project helped me learn:

* API integration
* Speech recognition
* Modular programming
* Python automation
* Text-to-speech systems
* Error handling
* Project structuring

---

## Author

Saurab Dhakal

---

## License

This project is for educational and portfolio purposes.
