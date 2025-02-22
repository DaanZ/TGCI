import fitz
import glob
import os

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_openai import OpenAIEmbeddings

from core.util import json_read_file

document_embeddings = OpenAIEmbeddings()


def read_pdf_path(file_path):
    document = fitz.open(file_path, filetype="pdf")
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def read_pdf(file_bytes, max_pages: int = None):
    document = fitz.open(stream=file_bytes, filetype="pdf")
    text = ""
    for page_num in range(document.page_count):
        if max_pages:
            if page_num > max_pages:
                break
        page = document.load_page(page_num)
        text += page.get_text()
    return text


def read_context(folder):
    pages = []
    paths = os.path.join(folder, "*.json")
    print(paths)
    for path in glob.glob(paths):
        data = json_read_file(path)
        for key in data:
            row = data[key]
            row["source"] = key
            pages.append(row)
    return pages


def read_pages(folder):
    pages = []
    paths = os.path.join(folder, "*.txt")
    print(paths)
    for path in glob.glob(paths):
        loader = TextLoader(path, encoding="utf-8")
        pages.extend(loader.load_and_split())
    return pages


def read_code(folder):
    pages = []
    paths = os.path.join(folder, "*.py")
    for path in glob.glob(paths):
        loader = TextLoader(path, encoding="utf-8")
        pager = loader.load_and_split()
        pages.extend(pager)
    return pages


def read_pdfs(folder):
    pages = []
    paths = os.path.join(folder, "*.pdf")
    for path in glob.glob(paths):
        loader = PyPDFLoader(path)
        pages.extend(loader.load_and_split())
    return pages
