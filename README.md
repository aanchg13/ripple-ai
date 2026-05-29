# Ripple 

An AI-powered web application designed to eliminate the operational bottleneck of manually analyzing user experience (UX) research data. By leveraging Large Language Models (LLMs), this tool automatically ingests raw conversation transcripts and instantly extracts core themes, critical user pain points, and a structured executive summary.

**What used to take a UX Researcher or Product Owner an entire day of manual tagging now takes under 90 seconds.**

---

## 🚀 The Problem & The Solution

* **The Bottleneck:** UX research, stakeholder interviews, and customer feedback calls generate hours of text transcripts. Manually parsing these documents to find actionable trends is incredibly time-consuming and delays product strategy decisions.
* **The AI Solution:** `ripple` automates the heavy lifting of qualitative data synthesis. It acts as an intelligent research partner that reads transcripts instantly, categorizing unstructured conversation data into high-value, organized business insights.

---

## 🛠️ Key Features

* **Automated Thematic Analysis:** Automatically identifies and clusters recurring topics and behavioral patterns across transcripts.
* **Pain Point Extraction:** Surface-levels immediate user friction, complaints, and blockers so product teams know exactly what to fix first.
* **Executive Summarization:** Generates a crisp, high-level overview of the conversation ideal for cross-functional stakeholders, engineering leads, or leadership one-pagers.
* **Lightweight Web Interface:** A decoupled, responsive frontend built for rapid upload and instantaneous processing.

---

## 💻 Tech Stack

* **Backend API:** Python, FastAPI (Asynchronous, high-performance API framework)
* **AI Engine:** OpenAI API / LangChain framework (for prompt chaining and structured data extraction)
* **Frontend UI:** HTML5 (`index.html`), Vanilla JavaScript (`app.js`), CSS3
* **Data Transfer:** Asynchronous HTTP requests via the Fetch API using JSON payloads

---

## ⚙️ Installation & Setup

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone [https://github.com/aanchg13/ripple.git](https://github.com/aanchg13/ripple.git)
cd ripple
```

### 2. Set Up the FastAPI Backend
Make sure you have Python installed, then install the required dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your API credentials:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

### 3. Launch the Frontend
The frontend relies on `app.js` and `index.html`. You can serve it locally using a VS Code extension like **Live Server** (right-click `index.html` -> *Open with Live Server*), or simply open the `index.html` file directly in any modern web browser.

---

## 🔮 Future Roadmap / Next Steps
* [ ] **Multi-file batch processing:** Allow users to upload 10+ transcripts at once to extract macro-trends across an entire research study.
* [ ] **Action-Item Generation:** Automatically generate product feature tickets or operational tasks directly from user pain points.
* [ ] **Sentiment Trend Dashboard:** Integrate visual charts showing the emotional trajectory of an interview over time.