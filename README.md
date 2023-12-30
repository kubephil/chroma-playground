# Description

This is just for me to keep track of my learnings and organize myself when reading through the docs the first time.

## Learnings

- Per Default it seems like you can run chorma in a python process for quick prototyping?
- This is also why the pip package is so "bloated". If you only need the client, you can run `pip install chromadb-client`
- You can also store the files to your local machine with a `PersistentClient(path="/path/to/save/to")`
- You can run it via docker `docker run -p 8000:8000 chromadb/chroma`. Note state not stored and no volume attached
- Chorma is by default ephemeral
- Chroma collections are created with an optional embedding function. If you later use `get_collection` you must use the same embedding function -> If non is supplied Chroma will use sentence transformer as a default
- In addition `create_collection` also takes the optional parameter metadata, which can be used to customize the distance method by setting the value of `hnsw:space`



## Useful links
- [Deployment](https://docs.trychroma.com/deployment) Options
## Open Questions