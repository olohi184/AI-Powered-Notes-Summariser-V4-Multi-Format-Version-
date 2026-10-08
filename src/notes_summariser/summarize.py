"""BART summarization with word-aware chunks and lazy model loading."""


def chunk_text(text: str, max_words: int = 350) -> list[str]:
    if max_words < 1:
        raise ValueError("max_words must be positive")
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


def summarize_text(text: str, model_name: str = "facebook/bart-large-cnn") -> str:
    if not text.strip():
        raise ValueError("Cannot summarize empty text")
    from transformers import pipeline
    summarizer = pipeline("summarization", model=model_name)
    summaries = []
    for chunk in chunk_text(text):
        # Short inputs need smaller output limits than long inputs.
        word_count = len(chunk.split())
        max_length = min(150, max(20, int(word_count * 1.3)))
        min_length = min(40, max_length - 1)
        result = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False, truncation=True)
        summaries.append(result[0]["summary_text"])
    return "\n\n".join(summaries)
