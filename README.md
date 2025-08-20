# Tesco Customer Service Chatbot

A Python-based chatbot that answers **Tesco online grocery FAQs**. The chatbot uses **NLTK for natural language processing** and a simple **Flask web server** to provide responses via a browser interface. The front end is built with **HTML/CSS**.

## Features

* Answers common Tesco online grocery FAQs (delivery, payments, returns, etc.).
* Uses **NLTK** for tokenization and simple intent classification.
* Built with **modular scripts**:

  * `data/` – dataset of Tesco FAQs
  * `chatbot.py` – chatbot logic (NLTK-based)
  * `app.py` – Flask server to connect chatbot to web interface
  * `templates/` – HTML frontend
  * `static/` – CSS styling
* Can be extended with new intents and answers.

## Tech Stack

* **Python 3.9+**
* **NLTK** for NLP
* **Flask** for backend
* **HTML/CSS** for frontend
* Optional: **Visual Studio Code** for development

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/tesco-chatbot.git
   cd tesco-chatbot
   ```

2. **Create a virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Linux/Mac
   venv\Scripts\activate     # on Windows
   pip install -r requirements.txt
   ```

3. **Run the Flask server**

   ```bash
   python app.py
   ```

4. **Open your browser** at `http://127.0.0.1:5000/` to chat with the bot.

## Example

User: *"What is Tesco’s delivery policy?"*
Bot: *"Tesco offers home delivery slots for groceries. You can book through the website or app."*

## Future Improvements

* Integrate with **OpenAI GPT API** for more advanced responses.
* Add a **vector database (FAISS/Chroma)** for semantic FAQ retrieval.
* Deploy on **Heroku or AWS** for live access.

## License

MIT License – free to use and modify.
