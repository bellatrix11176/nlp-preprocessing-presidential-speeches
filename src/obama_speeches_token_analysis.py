from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


# =============================================================================
# Presidential Speeches — Token Frequency (NLP Preprocessing Evidence Locker)
# =============================================================================
# Required preprocessing:
#   - tokenize
#   - lowercase
#   - remove English stopwords (default list)
#   - ignore tokens shorter than 3 characters
#
# Outputs (written to output/):
#   - wordlist_counts.csv      (full token frequency table)
#   - top20_tokens.csv         (top 20 tokens)
#   - key_token_counts.csv     (handy lookup counts for specific tokens)
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]  # .../NLP Preprocessing
DATA_DIR = PROJECT_ROOT / "data"
OUT_DIR = PROJECT_ROOT / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DATA_PATH = DATA_DIR / "presidential_speeches_corpus.txt"  # keep filename stable


def load_corpus_txt(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(
            f"File not found: {path}\n"
            "Expected: <project_root>/data/presidential_speeches_corpus.txt"
        )
    return path.read_text(encoding="utf-8", errors="ignore")


def build_wordlist(corpus: str) -> pd.DataFrame:
    vectorizer = CountVectorizer(
        lowercase=True,
        stop_words="english",
        token_pattern=r"(?u)\b\w{3,}\b",  # 3+ chars only
    )
    X = vectorizer.fit_transform([corpus])
    words = vectorizer.get_feature_names_out()
    counts = X.toarray().ravel()

    df = pd.DataFrame({"word": words, "count": counts})
    return df.sort_values("count", ascending=False).reset_index(drop=True)


def get_count(wordlist: pd.DataFrame, word: str) -> int:
    w = word.lower().strip()
    row = wordlist.loc[wordlist["word"] == w, "count"]
    return int(row.iloc[0]) if not row.empty else 0


def main() -> None:
    corpus = load_corpus_txt(DATA_PATH)
    wordlist = build_wordlist(corpus)

    # OUTPUT 1: Full word list (RapidMiner-like WordList output)
    wordlist.to_csv(OUT_DIR / "wordlist_counts.csv", index=False)

    # OUTPUT 2: Top 20 tokens
    top20 = wordlist.head(20).copy()
    top20.to_csv(OUT_DIR / "top20_tokens.csv", index=False)

    # OUTPUT 3: Key lookup counts (generic; not tied to question numbers)
    top_word = str(wordlist.iloc[0]["word"])
    top_count = int(wordlist.iloc[0]["count"])

    tokens_to_check = [
        "education",
        "afghanistan",
        "applause",
        "policy",
        "year",
        "country",
        "cancer",
        "addiction",
        "diabetes",
        "aids",
    ]

    rows = [{"item": "most_prevalent_word", "value": top_word, "count": top_count}]
    for t in tokens_to_check:
        rows.append({"item": f"token_{t}", "value": t, "count": get_count(wordlist, t)})

    key_counts = pd.DataFrame(rows)
    key_counts.to_csv(OUT_DIR / "key_token_counts.csv", index=False)

    # Console summary (sanity check)
    print("=== NLP Preprocessing — Token Frequency Summary ===")
    print(f"Corpus file: {DATA_PATH.name}")
    print(f"Most prevalent token: {top_word} ({top_count})")
    print("\nFiles written to output/:")
    print(" - wordlist_counts.csv")
    print(" - top20_tokens.csv")
    print(" - key_token_counts.csv")


if __name__ == "__main__":
    main()
