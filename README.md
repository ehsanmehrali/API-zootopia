# 🦊 Zootopia - Animal Info Web App

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-%20Web%20Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API: Ninjas](https://img.shields.io/badge/API-Ninjas-orange)](https://api-ninjas.com/api/animals)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)

<p>
Zootopia is a dynamic web application built with **Python** and **Flask** that allows users to search and explore detailed animal information. Users can input an animal name, filter by skin type, and view results as visually styled HTML cards.  
Animal data is fetched in real-time from an external API and cached locally in JSON format.
</p>
---

## 📁 Project Structure

```bash
    Zootopia/
├── app/
│   ├── static/
│   │     └── style.css
│   ├── templates/
│   │     └── animals_templates.html
│   ├── utils/
│   │     ├── init.py
│   │     └── serializer.py
│   └── data_managers/
│         ├── init.py
│         ├── data_fetcher.py
│         ├── load_html.py
│         └── load_json.py
├── animals_data/
│         └── animals_data.json
├── .env
├── .gitignore
├── animals_web_generator.py
├── requirements.txt
└── README.md
```
---

## 🚀 How to Run

### 1. Clone and Set Up

```bash
    git clone https://github.com/yourusername/Zootopia.git
    cd Zootopia
```

### 2. Set Environment Variables
Create a .env file in the root and add your API key:
```ini
    API_KEY=your_api_key_here
```
⚠️ Make sure .env is included in .gitignore.

### 3. Install Dependencies

```bash
    pip install -r requirements.txt
```
### 4. Run the App

```bash
    python animals_web_generator.py
```
Then open your browser and go to:
```cpp
    http://127.0.0.1:5000
```

---

## 🔍 How It Works
- On page load, users are prompted to enter an animal name.
- The app fetches data from the API Ninjas Animal API and stores it locally.
- Data is displayed in styled cards with additional filtering support by skin type.
- If no animal is found or input is invalid, the user is notified.

---

## 🧰 Technologies Used

- Python 🐍
- Flask 🌐
- HTML + CSS 🎨
- REST API
- JSON (local storage)
- python-dotenv for environment config

---

## ✅ Features
- 🔎 Real-time API integration for fresh animal data
- 🎛️ Filtering by animal characteristics (e.g. skin type)
- ⚠️ Error handling for empty or invalid input
- 💾 JSON-based local caching
- 🔐 Secure API key management with .env

---

## 📌 To Do
- Add pagination for large result sets
- Add species image thumbnails via a secondary API
- Improve 404 feedback with custom UI

---

## 🙌 Contribution
Feel free to fork this repo, make improvements, and open pull requests!

---

## 📄 License
MIT License © 2025 Ehsan Mehrali


