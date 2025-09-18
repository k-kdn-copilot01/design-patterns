from document import Document
from client import Client

if __name__ == "__main__":
    prototype_doc = Document("Template", "Base content")
    client = Client(prototype_doc)

    doc1 = client.make_copy()
    doc1.title = "Contract A"
    doc1.content = "Custom content A"

    doc2 = client.make_copy()
    doc2.title = "Contract B"
    doc2.content = "Custom content B"

    print("Prototype:", prototype_doc)
    print("Doc1:", doc1)
    print("Doc2:", doc2)
