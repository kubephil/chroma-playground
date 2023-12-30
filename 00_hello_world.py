import chromadb 


if __name__ == '__main__':
    chroma_client = chromadb.Client()

    collection = chroma_client.create_collection(name='fancy')
    collection.add(documents=["This is a document", "This is another document"],
                    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
                    ids=["id1", "id2"])
    results = collection.query(query_texts=["This is a query document"], n_results=2)
    print(results)

    # Now let's do the same with the persistent client. It will create files in the data folder
    persistent_chroma_client = chromadb.PersistentClient("./data")
    collection = persistent_chroma_client.create_collection(name='fancy')
    collection.add(documents=["This is a document", "This is another document"],
                    metadatas=[{"source": "my_source"}, {"source": "my_source"}],
                    ids=["id1", "id2"])
    results = collection.query(query_texts=["This is a query document"], n_results=2)
    print(results)
    

    