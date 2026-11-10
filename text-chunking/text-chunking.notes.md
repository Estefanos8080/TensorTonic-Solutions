Text chunking in NLP and data processing is the process of dividing a long text or sequence of tokens into smaller segments that can be processed individually. The chunk size determines how many tokens each segment contains, while overlap specifies how many tokens consecutive chunks share to help preserve context across boundaries. 



For example, a chunk size of 3 with an overlap of 1 divides `["a", "b", "c", "d", "e"]` into `[["a", "b", "c"], ["c", "d", "e"]]`. Chunking is used to fit documents within a model’s input limit, retrieve relevant passages in search and retrieval-augmented generation (RAG), summarize long documents, and process large datasets in manageable portions. 



Chunks can follow fixed token counts or natural boundaries such as sentences and paragraphs; the choice affects how well meaning is preserved, while greater overlap increases repeated processing and storage.