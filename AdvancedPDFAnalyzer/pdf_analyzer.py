# AdvancedPDFAnalyzer/pdf_analyzer.py

import os
import json
from datetime import datetime
from utils.pdf_utils import extract_text_from_pdf


def extract_sections(text, query):
    """
    Dummy function to simulate relevance matching.
    Replace this with an actual ML/NLP model if needed.
    """
    sections = []
    for idx, para in enumerate(text.split("\n\n")):
        if any(q.lower() in para.lower() for q in query.split()):
            sections.append({
                "page_number": idx + 1,
                "text": para.strip()
            })
    return sections[:5]  # Top 5 matches


def analyze_document(pdf_path, persona, task):
    text = extract_text_from_pdf(pdf_path)
    query = f"{persona} {task}"
    return extract_sections(text, query)


def process_collection(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")
    pdf_dir = os.path.join(collection_path, "PDFs")

    with open(input_path, 'r', encoding='utf-8') as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    task = input_data["job_to_be_done"]["task"]
    documents = input_data["documents"]

    all_sections = []
    all_subsections = []
    input_filenames = []

    for doc in documents:
        filename = doc["filename"]
        pdf_path = os.path.join(pdf_dir, filename)
        input_filenames.append(filename)

        matches = analyze_document(pdf_path, persona, task)
        for rank, match in enumerate(matches, start=1):
            title_line = match["text"].split("\n")[0][:100]
            all_sections.append({
                "document": filename,
                "section_title": title_line,
                "importance_rank": rank,
                "page_number": match["page_number"]
            })
            all_subsections.append({
                "document": filename,
                "refined_text": match["text"],
                "page_number": match["page_number"]
            })

    output_data = {
        "metadata": {
            "input_documents": input_filenames,
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": all_sections,
        "subsection_analysis": all_subsections
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
    print(f"✅ Processed: {collection_path}")


def process_all_collections(base_dir="Challenge_1b"):
    for name in os.listdir(base_dir):
        collection_path = os.path.join(base_dir, name)
        if os.path.isdir(collection_path) and name.startswith("Collection"):
            process_collection(collection_path)


if __name__ == "__main__":
    process_all_collections()