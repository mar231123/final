from word_doc import WordDocument
from PDF import PDFDocument
from EXCEL import ExcelDocument
class DocumentFactory:
    def create_document(doc_type, file_name, file_size, content):
        if doc_type == "Word":
            return WordDocument(file_name, file_size, content)
        elif doc_type == "PDF":
            return PDFDocument(file_name, file_size, content)
        elif doc_type == "Excel":
            return ExcelDocument(file_name, file_size, content)
        else:
            raise ValueError(f"Invalid document type: {doc_type}")
