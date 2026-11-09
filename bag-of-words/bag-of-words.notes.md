**Bag of Words (BoW) **

Represents a document as a fixed-length vector of word counts, ignoring grammar and word order. First, build a vocabulary of unique words from the training corpus and assign each word a fixed position; then count each vocabulary word in each document, recording zero when absent. For example, tokens `["i", "love", "ml", "love"]` with vocabulary `["i", "love", "hate", "ml"]` produce `[1, 2, 0, 1]`. 



Stacking these vectors creates a document-term matrix, where rows represent documents, columns represent vocabulary terms, and cells contain counts; this matrix is usually sparse because most documents contain only a small subset of the vocabulary. Preprocessing may include lowercasing, tokenization, and optional stopword removal, stemming, lemmatization, or filtering rare and common terms, depending on the task. BoW can use binary presence, raw counts, or normalized term frequency (count divided by document length), and document similarity can be measured using cosine similarity. I



t is simple, efficient, and useful for classification tasks such as spam detection, but it cannot capture word order, semantic relationships, or context, and a fixed vocabulary cannot represent unseen words unless explicitly handled. N-grams capture local word sequences, TF-IDF adjusts term importance, and embeddings or contextual models provide richer representations.