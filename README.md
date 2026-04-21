# ✈️ AI Travel Idea Generator

A beginner-friendly Flask web app that uses Google Gemini AI to generate personalized travel plans — including destination suggestions, day-by-day itineraries, packing checklists, and image ideas.

---

## 📁 Project Structure

```
travel-planner/
├── app.py                    # Flask backend
├── templates/
│   └── index.html            # Frontend HTML page
├── static/
│   └── style.css             # Styling
├── dataset/
│   └── destinations.csv      # Destination data
├── prompts/
│   └── travel_prompt.txt     # AI prompt template
├── requirements.txt          # Python dependencies
├── .env                      # API key (DO NOT commit)
├── .gitignore
├── vercel.json               # Vercel deployment config
├── README.md
└── GRANDMA.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/travel-planner.git
cd travel-planner
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_actual_api_key_here
```
Get your key from: https://aistudio.google.com/app/apikey

### 5. Run locally
```bash
python app.py
```
Open your browser at: **http://127.0.0.1:5000**

---

## 🚀 Deploy on Vercel

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Login
```bash
vercel login
```

### 3. Deploy
```bash
vercel
```

### 4. Set your environment variable on Vercel
Go to: Vercel Dashboard → Your Project → Settings → Environment Variables  
Add: `GEMINI_API_KEY` = your actual API key

### 5. Redeploy
```bash
vercel --prod
```

---

## 🌐 How It Works

1. User enters budget, travel days, and destination type
2. Flask backend reads `prompts/travel_prompt.txt` and fills in the user's inputs
3. The prompt is sent to Google Gemini API
4. Gemini returns a full travel plan
5. The app displays it in 4 tabs: Suggestion, Itinerary, Packing List, Image Idea

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google AI Studio API key |

---

## 📦 Tech Stack

- **Frontend**: HTML, CSS, vanilla JavaScript
- **Backend**: Python, Flask
- **AI**: Google Gemini 1.5 Flash
- **Deployment**: Vercel
