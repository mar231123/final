from document import Document
class ExcelDocument(Document):
    def open_document(self):
        print(f"Opening Excel document: {self.file_name}")
    def read_document(self):
        print(f"Reading Excel document: {self.file_name}")
    def save_document(self):
        print(f"Saving Excel document: {self.file_name}")
