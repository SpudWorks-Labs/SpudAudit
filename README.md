# SpudAudit
##### A Local-first, RAG-driven legal document auditor.

SpudAudit is designed to help understand legal documentation so that anyone can understand what is legal or not in plain English, and less legal jargon. By using a local LLM, it ensures 100% privacy for sensitive legal documents while providing verifiable citations from local statutes.


### Tech Stack
* Language; Python 3.11
* LLM Engine: Ollama (Running llama3.1:8b)
* Orchestration: LlamaIndex
* Vector DB: ChromaDB (Persistent local storage)
* Frontend: Streamlit
* Parsing: Marker & pypdf


### Quick Start

**1. Prerequisites**
Ensure Ollama is installed and pull the needed model:
```bash
ollama pull llama3.1:8b
```

**2. Installation**
```bash
git clone https://github.com/SpudWorks-Labs/SpudAudit
cd SpudAudit

conda create -n spudaudit python==3.11
conda activate spudaudit

pip install -r requirements.txt
```

**3. Ingestion (DCP Protocol)**
Place your legal PDFs in data/raw/ and run the ingestion file:
```bash
python src/core/ingest.py
```
**Note:** We follow the Data Cleaning Protocol: Clean -> Chunk -> Tag -> Index.

### Roadmap
* Phase 1: Foundation - Environment & PDF Vectorization. (Current)
* Phase 2: Logic - The "Judge" prompt for clause comparison.
* Phase 3: OCR - Handling messy user-uploaded PDFs.
* Phase 4: UI - Streamlit dashboard with "Risk Meter".
* Phase 5: Safety - Citation guardrails and clinic outreach.

### License
This project is licensed under the GNU Affero General public License v3.0 (AGPL-3.0) - see the [LICENSE](LICENSE) file for details. 

This project was made by human developers with the assistance of AI.
