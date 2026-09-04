# 🏋️‍♀️ AI Real-Time GYM Coach & Trainer

[![Deploy with Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=KartikKubde/AI-Gym-Trainer2&branch=main&mainModule=app.py)

AI Real-time GYM Coach is a computer vision and LLM powered workout companion built with **Streamlit**, **MediaPipe**, **OpenCV**, **Groq AI (Llama 3)**, and **gTTS**. It tracks your exercise form in real-time through your webcam, counts sets and reps, provides live positional feedback, and speaks personalized coaching audio.

---

## 🚀 Instant Deployment Guide (Streamlit Community Cloud)

You can deploy this project for **FREE** on **Streamlit Community Cloud** in under 2 minutes:

### Option 1: 1-Click Deploy
Click the button below to deploy directly to Streamlit Community Cloud:

[![Deploy with Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=KartikKubde/AI-Gym-Trainer2&branch=main&mainModule=app.py)

---

### Option 2: Manual Deploy Steps

1. **Log in to Streamlit Community Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.

2. **Create New App**:
   - Click **"Create app"** / **"Deploy an app"**.
   - Choose **"I already have an app"**.

3. **Configure Repository Settings**:
   - **Repository:** `KartikKubde/AI-Gym-Trainer2`
   - **Branch:** `main`
   - **Main file path:** `app.py` (or `Main App/main.py`)

4. **Add Secrets (Environment Variables)**:
   - Click **Advanced Settings** -> **Secrets** (or edit Secrets after deployment).
   - Add your Groq API Key:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```
   - *(Get a free key from [console.groq.com](https://console.groq.com/keys))*.

5. **Deploy**:
   - Click **Deploy!** 🚀
   - Streamlit will automatically install dependencies from `requirements.txt` and system packages from `packages.txt`.

---

## 💻 Local Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KartikKubde/AI-Gym-Trainer2.git
   cd AI-Gym-Trainer2
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up `.env` file:**
   Create a `.env` file inside `Main App/`:
   ```env
   GROQ_API_KEY=gsk_your_groq_api_key_here
   ```

5. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

---

## 🌟 Key Features

- 📹 **Real-Time WebRTC Pose Detection:** Smooth camera video streaming via WebRTC.
- 🏋️ **Multiple Exercise Detectors:** Squats, Push-ups, Biceps Curls, Shoulder Press, Lunges.
- 🤖 **Groq LLM AI Voice Coach:** Intelligent feedback and motivation tailored to your set/rep performance.
- 🔊 **Voice Audio Synthesis:** Real-time text-to-speech feedback via gTTS.
- 📊 **Workout History Tracking:** SQLite database persistence for set/rep logging.