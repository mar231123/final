from factory import DocumentFactory

word_doc = DocumentFactory.create_document("Word", "research.txt", 1024, "This is a Word document .")
word_doc.open_document()
word_doc.read_document()
word_doc.save_document()

pdf_doc = DocumentFactory.create_document("PDF", "presentation.pdf", 2048, "This is a PDF document.")
pdf_doc.open_document()
pdf_doc.read_document()
pdf_doc.save_document()

excel_doc = DocumentFactory.create_document("Excel", "STATS", 4096, "This is an Excel document.")
excel_doc.open_document()
excel_doc.read_document()
excel_doc.save_document()
