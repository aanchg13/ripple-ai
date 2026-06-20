# Ripple

An AI-powered web application designed to eliminate the operational bottleneck of manually analyzing user experience (UX) research data. By leveraging Anthropic's Claude models, this tool automatically ingests raw conversation transcripts and instantly extracts core themes, critical user pain points, and a structured executive summary.

**What used to take a UX Researcher or Product Owner an entire day of manual tagging now takes under 90 seconds.**

---

## 🚀 The Problem & The Solution

- **The Bottleneck:** UX research, stakeholder interviews, and customer feedback calls generate hours of text transcripts. Manually parsing these documents to find actionable trends is incredibly time-consuming and delays product strategy decisions.
- **The AI Solution:** `ripple` automates the heavy lifting of qualitative data synthesis. It acts as an intelligent research partner that reads transcripts instantly, categorizing unstructured conversation data into high-value, organized business insights.

---

## 🛠️ Key Features

- **Automated Thematic Analysis:** Identifies and clusters recurring topics and behavioral patterns across transcripts, complete with supporting quotes, frequency, and severity ratings.
- **Pain Point Extraction:** Surfaces immediate user friction, complaints, and blockers so product teams know exactly what to fix first.
- **User Needs Summary:** Lists out the underlying needs expressed by users across all transcripts.
- **Executive Summarization:** Generates a crisp, high-level overview of the conversation ideal for cross-functional stakeholders, engineering leads, or leadership one-pagers.
- **Multi-format Upload:** Accepts `.txt`, `.pdf`, and `.csv` transcript files.
- **Built-in Demo:** A `/sample` endpoint runs the analysis on bundled example banking-interview transcripts, so you can try the tool without uploading anything.

---

## 💻 Tech Stack

- **Backend API:** Python, FastAPI
- **AI Engine:** Anthropic Claude API (`claude-opus-4-5`)
- **File Parsing:** PyPDF2 (PDF), pandas (CSV)
- **Frontend UI:** Jinja2-rendered HTML (`templates/index.html`), vanilla JavaScript (`static/app.js`), CSS (`static/style.css`)
- **Data Transfer:** Asynchronous HTTP requests via the Fetch API using JSON payloads

---

## ⚙️ Installation & Setup

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/aanchg13/ripple-ai.git
cd ripple-ai
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn anthropic python-dotenv jinja2 python-multipart PyPDF2 pandas
```

### 4. Set Up Your API Key

Create a `.env` file in the root directory and add your Anthropic API key:

```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.

### 6. Try It Out

- Click the **sample** option in the UI to see an instant demo analysis of bundled example transcripts, or
- Upload your own `.txt`, `.pdf`, or `.csv` transcript file(s) for analysis.

---

## 🔮 Future Roadmap / Next Steps

- [ ] **Multi-file batch processing:** Allow users to upload 10+ transcripts at once to extract macro-trends across an entire research study.
- [ ] **Action-Item Generation:** Automatically generate product feature tickets or operational tasks directly from user pain points.
- [ ] **Sentiment Trend Dashboard:** Integrate visual charts showing the emotional trajectory of an interview over time.
- [ ] **requirements.txt:** Add a proper dependency lockfile for easier setup.