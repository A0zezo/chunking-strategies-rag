"""Three text chunking strategies commonly used before indexing documents for RAG."""
import re


def fixed_chunks(text, size=200, overlap=40):
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    step = size - overlap
    return [text[i:i + size] for i in range(0, max(len(text) - overlap, 1), step)]


def sentence_chunks(text, max_chars=200):
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    out, cur = [], ""
    for s in sents:
        if cur and len(cur) + 1 + len(s) > max_chars:
            out.append(cur)
            cur = s
        else:
            cur = f"{cur} {s}".strip()
    if cur:
        out.append(cur)
    return out


def paragraph_chunks(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
