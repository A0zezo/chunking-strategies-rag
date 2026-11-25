# chunking-strategies-rag

Three text chunking strategies used before indexing for RAG: fixed size with overlap, sentence-packed, and paragraph.

## Run

```bash
pip install -r requirements.txt
python demo.py
pytest
```

## Output (reproduced)

```
$ python3 demo.py
fixed(size=150, overlap=30): 3 chunks, lengths [150, 150, 124]
sentence(max_chars=150): 3 chunks, lengths [129, 135, 95]
paragraph: 3 chunks, lengths [129, 135, 95]

$ pytest -q
5 passed in 0.01s
```

## Limits

- Sizes are in characters, not tokens. The demo only compares chunk counts and lengths on a short sample text; it does not measure retrieval quality.
