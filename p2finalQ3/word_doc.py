from document import Document
class WordDocument(Document):
    def open_document(self):
        print(f"Opening Word document: {self.file_name}")
    def read_document(self):
        print(f"Reading Word document: {self.file_name}")
    def save_document(self):
        print(f"Saving Word document: {self.file_name}")
