# AI-Powered Notes Summariser — V4 Multi-Format

[![Python Tests](https://github.com/olohi184/AI-Powered-Notes-Summariser-V4-Multi-Format-Version-/actions/workflows/python-tests.yml/badge.svg)](https://github.com/olohi184/AI-Powered-Notes-Summariser-V4-Multi-Format-Version-/actions/workflows/python-tests.yml)

A Python document summarization project using Hugging Face's `facebook/bart-large-cnn` model. It accepts **TXT, PDF and DOCX** documents, extracts readable text, creates chunked summaries and saves a text report.

## Quick start
Requires **Python 3.10+**, internet access for the initial model download, and sufficient memory/disk space for the BART model and PyTorch. CPU inference may be slow.

```bash
git clone https://github.com/olohi184/AI-Powered-Notes-Summariser-V4-Multi-Format-Version-.git
cd AI-Powered-Notes-Summariser-V4-Multi-Format-Version-
python -m pip install -r requirements.txt
python main.py path/to/notes.pdf -o summary_output.txt
```

Replace the input with a `.txt` or `.docx` file as needed. The model downloads from Hugging Face on first use.

## Project structure
- `main.py`: command-line interface
- `src/notes_summariser/documents.py`: document text extraction
- `src/notes_summariser/summarize.py`: BART inference and chunking
- `tests/`: fast tests without model download
- Original notebook and Colab-exported Python script: retained for learning history

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Limitations
- Scanned or image-only PDFs are not supported without OCR.
- Long documents are summarized chunk by chunk; results may omit context across chunks.
- Summaries can contain errors; verify against the source before relying on them.
- The original exported Colab script is not the main CLI entry point. Use `main.py`.

## Author
Olohimai Juliet Michael · [GitHub](https://github.com/olohi184)
