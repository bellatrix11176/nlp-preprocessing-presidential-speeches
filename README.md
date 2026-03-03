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
---

## How to Run
From the project root folder (NLP Preprocessing/), run:

python src/presidential_speeches_token_analysis.py

Outputs (Evidence Locker)
All files are written to output/.

Token frequency outputs
- wordlist_counts.csv      (full token frequency table: word + count)
- top20_tokens.csv         (top 20 tokens by count)
- key_token_counts.csv     (counts for specific tokens used for quick lookup)
---

## Notes
- Stopwords are removed using the default English stopword list.
- Tokens shorter than 3 characters are excluded by the vectorizer token pattern.
- The full word list is saved so results are transparent and easy to verify.
- key_token_counts.csv is a convenience file: it does not “answer” questions by itself, but it makes it easy to reference exact counts in a write-up.

MIT License

Copyright (c) 2026 Gina Aulabaugh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

🌐 **PixelKraze Analytics (Portfolio):** https://pixelkraze.com/?utm_source=github&utm_medium=readme&utm_campaign=portfolio&utm_content=homepage
