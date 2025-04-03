# 🌍 Build Local Language Translator - Translates English, Spanish and French with Streamlit and Python Code.

Build a lightweight, offline-capable translation app for English, Spanish, and French using MarianMT models.

# Features
- Local Translation: No API keys or internet required after setup

# Bilingual Support:
- English ↔ Spanish
- English ↔ French
- Small Models: ~150MB per language pair
- Simple UI: Built with Streamlit for ease of use

# Models & Performance
- Models Used: MarianMT from Helsinki-NLP

- opus-mt-en-es (English ↔ Spanish)
- opus-mt-en-fr (English ↔ French)

- Model Sizes: ~150MB each (total ~300MB for all pairs)

# Performance:
- Best for short/medium sentences
- Moderate accuracy (comparable to mid-tier translators)
- CPU-friendly (no GPU required)

# Installation
Clone the repo:
git clone https://github.com/ErikElcsics/Build-Language-Translator-Local-Streamlit--Translates-English-Spanish-French-Python-Code.git
cd streamlit-translator

# Install dependencies:
pip install streamlit transformers torch sentencepiece

# Run the app:
streamlit run LocalLanguageTranslator.py

# How It Works
- Select Languages: Choose source/target from dropdowns.
- Enter Text: Type/paste text to translate.
- Click Translate: Output appears instantly.

# Basic Technical Information:
- Uses Hugging Face’s transformers to load MarianMT models.
- Tokenizes input → generates translation → decodes output.

# Libraries Used
- streamlit (UI)
- transformers (model loading)
- torch (PyTorch backend)
- sentencepiece (tokenization)

# Notes
First run downloads models (~5-10 minutes depending on internet).
Translations may be slower on CPU (2-5 seconds per sentence).

# License: MIT

English to Spanish

![image](https://github.com/user-attachments/assets/87db213e-48b9-48e2-bc81-669a5cc6fc82)

English to French

![image](https://github.com/user-attachments/assets/036088b5-6527-4c42-a75a-767deaecb340)

French to English

![image](https://github.com/user-attachments/assets/a379a6dd-685f-4042-9cbc-e480b66ac36b)

Spanish to English

![image](https://github.com/user-attachments/assets/1d4a5e1d-996b-4b2b-afc3-17e548f3e6ae)










