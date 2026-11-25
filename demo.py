from chunking import *

text = open("sample.txt").read()
for name, chunks in [("fixed(size=150, overlap=30)", fixed_chunks(text, 150, 30)),
                     ("sentence(max_chars=150)", sentence_chunks(text, 150)),
                     ("paragraph", paragraph_chunks(text))]:
    lens = [len(c) for c in chunks]
    print(f"{name}: {len(chunks)} chunks, lengths {lens}")
