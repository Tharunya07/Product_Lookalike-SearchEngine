from jina import Document, DocumentArray, Flow

def index():
docs = DocumentArray.from_files('fashion_products') 
#making a document array

# Createing a Flow to process our Documents
