"""Reference Modal GPU job for future embedding/entity-resolution workloads."""

import modal

app = modal.App("sapphire-org-platform-gpu")
image = modal.Image.debian_slim().pip_install("sentence-transformers", "torch")


@app.function(image=image, gpu="T4", timeout=900)
def embed_batch(texts: list[str]) -> list[list[float]]:
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return model.encode(texts, normalize_embeddings=True).tolist()

