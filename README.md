# 🦊 Zootopia - Animal Info Web App

A simple yet fun project to display animal information as styled HTML cards, with support for filtering based on characteristics like skin type. Built with **Python** and **Flask**.

---

## 📁 Project Structure

```bash
    My-Zootopia/
        │
        ├─────────animals_data/
        │             └──animals_data.json
        ├─────────data_managers/
        │             ├──__init__.py
        │             ├──load_html.py
        │             └──load_json.py
        ├─────────static
        │             └──style.css
        ├─────────templates/
        │             └──animals_templates.html
        ├──animals_web_generator.py
        ├──.gitignore
        └──README.md
```
---

## 🚀 How to Run

### 1. Install Dependencies

Make sure you have Python and pip installed. Then run:

```bash
  pip install Flask
```
---
### 2. Run the App

Start the Flask development server with:

```bash
  python app.py
```

Then open your browser and go to:

```cpp
    http://127.0.0.1:5000
```

---

### 3. Using Filters
At the top of the page, there’s a dropdown menu to choose a filter such as Skin Type. Once selected, the animal cards will update to show only matching animals.

---

## 💻 Technologies Used
- Python 🐍
- Flask 🌐
- HTML & CSS 🎨
- JSON (as the data source)

---

## 🧠 Notes

- The original HTML structure is preserved. It is never overwritten — content is dynamically inserted.
- Filtering is handled via query parameters using GET requests.

---

