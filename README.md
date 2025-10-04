# 🌐 AFFECTA

AFFECTA is an AI-powered **mental health teletherapy assistant** that analyzes both **facial expressions** (FER) and **voice emotions** (VER) from recorded therapy sessions.  
It helps therapists gain deeper insights into patients’ emotions by combining **video + audio analysis**.

---

## ✨ Features
- 🎥 **Upload therapy sessions** (video files)
- 🤖 **Facial Emotion Recognition (FER)** using AI models
- 🎤 **Voice Emotion Recognition (VER)** for vocal analysis
- 📊 **Interactive graphs** to visualize emotional trends
- 👨‍⚕️ **Therapist login & registration**
- ☁️ **Google Drive integration** for session storage

---

## 📂 Project Structure
AFFECTA/
│── backend/ FastAPI backend (Python + PostgreSQL)
│ ├── app/
│ │ ├── api/ Upload & analysis endpoints
│ │ ├── models/ Database models
│ │ ├── utils/ Cloud storage + ML models
│ │ └── main.py App entry point
│── frontend/ React + Tailwind frontend
│ ├── src/
│ │ ├── components Upload form, analysis UI, login, etc.
│ │ └── App.jsx
│── README.md


---

## ⚙️ Tech Stack
- **Backend:** FastAPI (Python), SQLAlchemy, PostgreSQL
- **Frontend:** React.js, Tailwind CSS, Recharts
- **Storage:** Google Drive (via PyDrive)
- **ML Models:** FER (CNN), VER (audio feature extraction)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/AFFECTA.git
cd AFFECTA
cd backend
# (Create virtual environment)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn app.main:app --reload
cd frontend
npm install
npm run dev
🧪 Usage

Register / Login as a therapist.

Upload a therapy session (video).

Analyze a session → view FER + VER results.

View results in charts & summaries.

📊 Example Output

FER: Frame-by-frame emotional breakdown (happy, sad, neutral, angry…)

VER: Dominant voice emotion (neutral, stressed, happy…)
