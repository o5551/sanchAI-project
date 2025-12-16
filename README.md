
# 🌤️ SanchAI Analytics – Weather Assistant

A minimal full-stack web application built as part of the **SanchAI Analytics Tech Assessment**.
The application allows users to ask weather-related questions for any city using natural language.
The backend leverages **LangChain with an LLM via OpenRouter** to intelligently decide when to invoke a weather tool and respond with a human-readable answer.

---

## 🧠 Project Overview

* **Frontend:** React
* **Backend:** FastAPI
* **LLM Integration:** LangChain + OpenRouter
* **Functionality:**
  Users enter a query like *“What’s the weather in Pune?”* and receive a natural language weather response.

---

## ⚙️ Tech Stack

| Layer        | Technology                    |
| ------------ | ----------------------------- |
| Frontend     | React (JavaScript)            |
| Backend      | FastAPI (Python)              |
| AI / LLM     | LangChain + OpenRouter        |
| Weather Data | wttr.in (no API key required) |

---

## 🔄 Application Flow

1. User enters a query in the React frontend.
2. Frontend sends the query to the FastAPI backend.
3. Backend passes the query to a LangChain agent.
4. The agent analyzes the query and decides whether to invoke the weather tool.
5. Weather tool fetches real-time weather data.
6. LLM formats the response in natural language.
7. Response is returned and displayed in the frontend.

---

## 📁 Project Structure

```
SanchAI-Analytics/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── weather_tool.py
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── src/
    └── package.json
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/o5551/sanchAI-project.git
cd sanchAI-project
```

---

### 2️⃣ Backend Setup

#### Create virtual environment

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Create `.env` file

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

#### Run backend server

```bash
uvicorn main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

---

### 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will start at:

```
http://localhost:3000
```

---

## 🧪 Example Query

**Input:**

```
What is the weather in Mumbai?
```

**Output:**

```
It is 28°C in Mumbai. Weather is Partly cloudy.
```

---

## ✨ Key Features

* Natural language query handling
* Intelligent tool invocation using LangChain agents
* Real-time weather data
* Simple and clean UI
* Extensible architecture for adding more tools

---

## 📌 Notes

* Weather data is fetched using **wttr.in**, which does not require an API key.
* LLM access is provided via **OpenRouter**.
* The project focuses on clarity and correctness rather than overengineering.

---

## 👤 Author

**Omkar More**

---

## 🔑 Access

GitHub repository access has been shared with **`pyaf`** as per the assessment instructions.

---

## 📄 License

This project is created solely for evaluation purposes as part of a technical assessment.

---




