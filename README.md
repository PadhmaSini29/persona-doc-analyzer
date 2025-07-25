# 📘 Adobe India Hackathon 2025 – Round 1B Submission  
## 🧠 Challenge: **Connecting the Dots Through Docs**  
### 👥 Team: Catalyst

---

## 🚀 Project Title:  
### **PERSONA-DRIVEN DOCUMENT INTELLIGENCE**

---

## 🧠 Problem Statement

Modern professionals — from researchers to analysts — are often overwhelmed with massive PDFs and limited time. This project solves the problem of **extracting and prioritizing relevant sections** from a **collection of documents**, based on a **specific user persona** and their **goal/task**.

---

## 🎯 Objective

Build an offline system that:

- Accepts a persona and their job-to-be-done
- Processes 3–10 related PDFs
- Extracts and ranks the most relevant document sections
- Outputs a structured, hackathon-compliant JSON
- Runs on CPU only with no internet access

---

## 🚀 Features

- 🔍 Persona-driven keyword matching
- 📄 PyMuPDF-based paragraph-level text extraction
- 🧠 Context-aware section ranking
- 📝 JSON output with metadata, extracted sections & full text
- 🧩 Modular, extensible design
- 🐳 Docker-ready, fully offline, CPU-friendly

---

## 🛠 Tech Stack

| Component           | Tool/Library             |
|---------------------|--------------------------|
| Language            | Python 3.10              |
| PDF Parsing         | PyMuPDF (fitz)           |
| Output Format       | JSON                     |
| Containerization    | Docker (amd64 CPU only)  |

---

## 📁 Project Structure

```
AdvancedPDFAnalyzer/
├── pdf_analyzer.py             # Main script to run analysis
├── utils/
│   └── pdf_utils.py            # PDF text extraction helper
├── Challenge_1b/
│   ├── Collection 1/
│   │   ├── PDFs/               # Input PDFs
│   │   ├── challenge1b_input.json     # Persona, job, document list
│   │   └── challenge1b_output.json    # Output JSON (auto-generated)
│   └── Collection 2/
└── requirements.txt
```

---

## 🧪 Sample Input (challenge1b_input.json)

```json
{
  "persona": {
    "role": "PhD Researcher in Computational Biology"
  },
  "job_to_be_done": {
    "task": "Prepare a literature review on GNN methods for drug discovery"
  },
  "documents": [
    { "filename": "paper1.pdf" },
    { "filename": "paper2.pdf" }
  ]
}
```

---

## 📤 Sample Output (challenge1b_output.json)

```json
{
  "metadata": {
    "input_documents": ["paper1.pdf", "paper2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare a literature review on GNN methods for drug discovery",
    "processing_timestamp": "2025-07-24T12:45:30"
  },
  "extracted_sections": [
    {
      "document": "paper1.pdf",
      "section_title": "Graph-based drug prediction models",
      "importance_rank": 1,
      "page_number": 2
    }
  ],
  "subsection_analysis": [
    {
      "document": "paper1.pdf",
      "refined_text": "Graph-based drug prediction models are widely adopted...",
      "page_number": 2
    }
  ]
}
```

---

## 📦 How to Run

1. Place PDFs inside: `Challenge_1b/CollectionX/PDFs/`  
2. Edit your `challenge1b_input.json`  
3. Run the script:

```bash
python pdf_analyzer.py
```

> 💡 This will process all collections inside the `Challenge_1b/` folder and create corresponding outputs.

---

## 🧠 Methodology

1. **Extract PDF Text**  
   - Uses PyMuPDF to extract page-wise text  
   - Splits into paragraphs using `

` as a delimiter

2. **Construct Persona Query**  
   - Combines role + job-to-be-done into a keyword query

3. **Keyword-Based Matching**  
   - Paragraphs are scanned for overlap with query tokens  
   - Top 5 matches per document are selected

4. **Ranking & Structuring**  
   - Matches are sorted by appearance  
   - Output includes section title, rank, and full content

---

## ✅ Constraints Followed

- Runs ≤ 60 seconds for 3–5 PDFs  
- Fully offline (no API calls or web access)  
- CPU-only with <1GB memory footprint  
- No hardcoded logic or format assumptions  

---

## 🔍 Testing

- ✅ Academic research papers  
- ✅ Business reports  
- ✅ Educational textbooks  
- ✅ Edge cases (broken metadata, line splits, multilingual)  

---

## 📈 Possible Improvements

- Add semantic similarity via sentence embeddings  
- Use transformer models (e.g., Longformer) for better matching  
- Support multilingual document handling  
- Add GUI or Adobe Embed API-based viewer


## 🔒 Repository Status

This repository is private until the competition ends, in accordance with Adobe India Hackathon 2025 rules.

---
