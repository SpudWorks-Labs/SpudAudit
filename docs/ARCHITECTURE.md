# SpudAudit

SpudAudit is a local-first, RAG-driven legal auditor designed to identify
illegal clauses and legal loopholes within residential leases - and more in
future versions.

---

### Program Model
- ***The RAG Pipeline:***
    * The program takes a library of PDFs and other sources of information
      for the knowledge and a user provided query with an optional legal
      document upload.
    * The Local LLM acts as a legal auditor and provides helpful information
      and required steps to the user.
    * Finally, the user receives a report on the information.
- ***Tech Stack:***
    * **Language:** Python 3.11+
    * **LLM Engine:** Ollama (inference)
    * **Orchestration:** LlamaIndex (data framework)
    * **Vector DB:** ChromaDB (persistent local storage)
    * **Frontend:** Streamlit (rapid UI prototyping)
    * **PDF Parsing:** pypdf and Marker (for clean OCR)

---

### File Structure
```plaintext
SpudAudit/
├── data/
│   ├── raw/                # Original PDFs/Bylaws
│   └── chunked_law/        # Cleaned/Chunked markdown of the law
├── src/
│   ├── core/
│   │   ├── ingest.py       # Vectorizes the PDF/ByLaw data
│   │   └── auditor.py      # Main RAG logic & Prompt Engineering
│   ├── web/
│   │   └── app.py          # Streamlit Interface
│   └── utils/
│       └── pdf_tools.py    # Conversion and OCR logic
├── vector_store/           # Persistent ChromaDB indices
├── tests/                  # Integration tests for "Hallucination Checks"
├── docs/
│   ├── ARCHITECTURE.md     # Defining the architecture for the program.
│   └── DEV_LOG.md          # Entire log of development.
├── .env                    # Local environment variables
├── README.md               # Information pertaining to the project.
└── requirements.txt
```

---

### Phase Roadmap
**Phase 1: Foundation & Data Ingestion**
* **Goal:** Environment setup and PDF/ByLaw Vectorization.
* **Deliverble:** A script that can answer the users legal queries using
                  local PDFs.
* **Success Metric:** 100% Citation Reliability on basic legal retrieval
                      queries.

**Phase 2: The Logic Layer & Prompt Engineering**
* **Goal:** Create the "Comparison" prompt.
* **Deliverable:** A CLI tool where you paste a clause, and it returns
                  "Valid" or "Illegal" with a citation.
* **Reality:** Can it detect an illegal "No Pets" clause for RTA 10/10 times?

**Phase 3: Document Parsing & OCR**
* **Goal:** Handle messy user inputs.
* **Deliverable:** Integration of pypdf to allow users to upload PDF leases
                   instead of copy-pasting text.
* **Success Metric:** Successful text extraction from a legal document
                      template.

**Phase 4: The SpudAudit UI**
* **Goal:** Move from Terminal to the Browser.
* **Deliverable:** A Streamlit dashboard with a "Risk Meter" and a
                   "Download Audit Report" (PDF) button.
* **Revenue Focus:** This is the version that can be shown to potential
                     partners.

**Phase 5: Hallucination Guardrails & Lead Gen**
* **Goal:** Stability and Outreach.
* **Deliverable:** Implementation of a "Citation Check" so the AI cannot
                   output a claim without a matching Section Index.
* **Action:** Send a demo video to one Legal Aid clinic or Housing NGO.

---

### Installation
```bash
git clone https://github.com/SpudWorks-Labs/SpudAudit
cd SpudAudit

python -m venv ./venv
source ./venv/bin/activate

pip install -r requirements.txt

python app.py
```
