"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Company: SpudWorks
                         Program Name: SpudAudit
       Description: RAG-driven legal auditor for legal documents like leases.
                             File: ingest.py
                            Date: 2026/03/02
                        Version: 0.1.0-2026.03.02

===============================================================================

                     Copyright (C) 2026 SpudWorks Labs.

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as published
        by the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.

        You should have received a copy of the GNU Affero General Public License
        along with this program. If not, see <https://www.gnu.org/licenses/>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings
import chromadb


Settings.llm = Ollama(model="llama3.1:8b", request_timeout=360.0)
Settings.embed_model = OllamaEmbedding(model_name="llama3.1:8b")


def ingest_documents():
    print("Ingesting the documents...")

    reader = SimpleDirectoryReader(input_dir="data/raw")
    documents = reader.load_data()

    db = chromadb.PersistentClient(path="./vector_store")
    chroma_collection = db.get_or_create_collection("legal_knowledge_base")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )

    print("Documents ingested successfully!")


if __name__ == '__main__':
    ingest_documents()
