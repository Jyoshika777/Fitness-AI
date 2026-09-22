# 🏋️ Fitness AI Agent

A personalized **AI-powered fitness plan generator** built using **Python, Flask, LangGraph, LangChain, Ollama, and Llama 3.2**.

The application collects basic fitness information from the user and generates a personalized workout plan with exercises, sets, repetitions, warm-up, cool-down, recovery, nutrition guidance, and progress tracking.

---

## ✨ Features

* 🧑 Personalized fitness plans
* 🎯 Goal-based workout recommendations
* 📅 Weekly workout schedule
* 💪 Exercise, sets, and repetitions
* ⏱️ Workout duration customization
* 🏠 Equipment-based workout planning
* 🔥 Warm-up and cool-down guidance
* 💤 Rest and recovery recommendations
* 🥗 Basic nutrition guidance
* 📊 AI-based plan evaluation
* 🤖 Local AI processing using Ollama
* 🌐 Simple and responsive Flask web interface
* 🔒 No external AI API key required

---

## 🛠️ Technologies Used

| Technology   | Purpose            |
| ------------ | ------------------ |
| Python       | Core programming   |
| Flask        | Web application    |
| LangGraph    | AI agent workflow  |
| LangChain    | LLM integration    |
| Ollama       | Local AI runtime   |
| Llama 3.2 3B | Language model     |
| HTML         | Frontend structure |
| CSS          | Frontend styling   |

---

## 🏗️ Project Structure

```text
fitness-plan-agent/
│
├── app.py
├── fitness_agent.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── templates/
    └── index.html
```

---

## 🔄 How It Works

```text
User
  │
  ▼
Fitness Web Form
  │
  ▼
Flask Application
  │
  ▼
LangGraph Agent
  │
  ├── Generate Fitness Plan
  │
  ▼
  ├── Evaluate Fitness Plan
  │
  ▼
Personalized Result
```

The application uses **Llama 3.2 3B locally through Ollama**, so user information is processed on the local machine rather than being sent to an external AI API.

---

# 🚀 Installation

## 1. Install Python

Install Python 3.11 or newer.

Verify the installation:

```bash
python --version
```

---

## 2. Install Git

Install Git if you want to clone the repository.

Verify:

```bash
git --version
```

---

## 3. Install Ollama

Install Ollama on your computer.

Verify:

```bash
ollama --version
```

---

## 4. Download the AI Model

The project uses **Llama 3.2 3B**.

Run:

```bash
ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

You should see:

```text
llama3.2:3b
```

> The AI model is not included in this GitHub repository because it is large. Each user should download it through Ollama.

---

# 📥 Clone the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fitness-plan-agent.git
```

Enter the project folder:

```bash
cd fitness-plan-agent
```

---

# 📦 Install Python Dependencies

Run:

```bash
pip install -r requirements.txt
```

The main dependencies are:

```text
Flask
langchain-core
langchain-ollama
langgraph
```

---

# ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🧪 Test the AI Agent

You can also test the fitness agent directly from the terminal:

```bash
python fitness_agent.py
```

Example input:

```text
Age: 22
Height: 165
Weight: 60
Fitness goal: general fitness
Experience level: beginner
Workout days per week: 4
Workout duration: 45
Equipment available: none
Workout preferences: home workout
```

The agent will generate and evaluate a personalized fitness plan.

---

# 🖥️ Application Workflow

The user provides:

* Age
* Height
* Weight
* Fitness goal
* Experience level
* Workout days
* Workout duration
* Available equipment
* Workout preferences

The AI then generates a customized fitness plan based on the provided information.

---

# 🤖 AI Agent Workflow

The project uses **LangGraph** to manage the AI workflow.

### Step 1 — Generate

The Llama 3.2 model generates a personalized fitness plan.

### Step 2 — Evaluate

The AI evaluates the generated plan based on:

* Safety
* Personalization
* Exercise balance
* Workload
* Recovery
* Goal alignment

The plan receives a score from **1–10** along with feedback.

---

# ⚡ Local AI

This project uses:

```text
Ollama
    ↓
Llama 3.2 3B
```

No OpenAI API key or other cloud AI API key is required.

The model runs locally on the user's computer.

---

# ⚠️ Safety Notice

This application provides **general fitness information for educational and planning purposes**.

It is not a replacement for professional medical or fitness advice.

Users with injuries, medical conditions, or other health concerns should consult a qualified healthcare professional before starting a new exercise program.

---

# 🔮 Future Enhancements

Possible future improvements include:

* 👤 User accounts
* 💾 Database integration
* 📈 Workout progress tracking
* 📊 Fitness analytics dashboard
* 🥗 More detailed nutrition planning
* 📱 Mobile-friendly application
* 🎙️ Voice-based fitness assistant
* 🧠 More advanced AI recommendations
* 📄 Downloadable workout plans
* ☁️ Cloud deployment

---

# 👩‍💻 Author

**Jyoshika Irlapati**

B.Tech – Computer Science and Engineering

---

## ⭐ Project Goal

The goal of this project is to demonstrate how **Generative AI, LangGraph, LangChain, Ollama, and Flask** can be combined to create a practical AI-powered fitness assistant.
