from document import Document
class PDFDocument(Document):
    def open_document(self):
        print(f"Opening PDF document: {self.file_name}")
    def read_document(self):
        print(f"Reading PDF document: {self.file_name}")
    def save_document(self):
        print(f"Saving PDF document: {self.file_name}")
