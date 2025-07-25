import os
import fitz  # PyMuPDF
import json
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


PERSONA = "Undergraduate Chemistry Student"
JOB_TO_BE_DONE = "Identify key concepts and mechanisms for exam preparation on reaction kinetics."


def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                text = " ".join(span["text"].strip() for line in block["lines"] for span in line["spans"] if span["text"].strip())
                if not text or len(text.split()) < 5:
                    continue
                sections.append({
                    "document": os.path.basename(pdf_path),
                    "page_number": page_num + 1,
                    "section_title": text[:50].strip(),
                    "content": text.strip()
                })

    return sections


def rank_sections(sections, query):
    documents = [s["content"] for s in sections]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([query] + documents)
    query_vec = tfidf_matrix[0]
    doc_vecs = tfidf_matrix[1:]
    similarity_scores = cosine_similarity(query_vec, doc_vecs).flatten()

    for i, score in enumerate(similarity_scores):
        sections[i]["score"] = float(score)

    ranked = sorted(sections, key=lambda x: x["score"], reverse=True)
    return ranked[:5]


def refine_subsection_text(text):
    sentences = text.split(". ")
    return ". ".join(sentences[:2]) + "." if sentences else text


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    all_sections = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            sections = extract_text_blocks(pdf_path)
            all_sections.extend(sections)

    query = PERSONA + " " + JOB_TO_BE_DONE
    ranked_sections = rank_sections(all_sections, query)

    extracted_sections = []
    subsection_analysis = []

    for idx, section in enumerate(ranked_sections, start=1):
        extracted_sections.append({
            "document": section["document"],
            "page_number": section["page_number"],
            "section_title": section["section_title"],
            "importance_rank": idx
        })

        subsection_analysis.append({
            "document": section["document"],
            "refined_text": refine_subsection_text(section["content"]),
            "page_number": section["page_number"]
        })

    output_json = {
        "metadata": {
            "input_documents": list(set([s["document"] for s in all_sections])),
            "persona": PERSONA,
            "job_to_be_done": JOB_TO_BE_DONE,
            "processing_timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    output_path = os.path.join(output_dir, "challenge1b_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_json, f, indent=4)


if __name__ == "__main__":
    main()
