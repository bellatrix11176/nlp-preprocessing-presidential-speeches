# NLP Preprocessing — Presidential Speeches Token Frequency

This project performs basic **NLP preprocessing** on a presidential speeches text corpus, then exports a token frequency “word list” and supporting outputs to an `output/` evidence locker.

The preprocessing matches the assignment requirements:
- Tokenize text into words
- Convert all text to lowercase
- Remove English stopwords (default list)
- Ignore tokens shorter than 3 characters

---

## Folder Structure

```text
NLP Preprocessing/
├─ data/
│  └─ presidential_speeches_corpus.txt
├─ src/
│  └─ presidential_speeches_token_analysis.py
├─ output/
│  └─ (generated files)
└─ README.md
```
How to Run
From the project root folder (NLP Preprocessing/), run:

python src/presidential_speeches_token_analysis.py

Outputs (Evidence Locker)
All files are written to output/.

Token frequency outputs
- wordlist_counts.csv      (full token frequency table: word + count)
- top20_tokens.csv         (top 20 tokens by count)
- key_token_counts.csv     (counts for specific tokens used for quick lookup)

Notes
- Stopwords are removed using the default English stopword list.
- Tokens shorter than 3 characters are excluded by the vectorizer token pattern.
- The full word list is saved so results are transparent and easy to verify.
- key_token_counts.csv is a convenience file: it does not “answer” questions by itself, but it makes it easy to reference exact counts in a write-up.
