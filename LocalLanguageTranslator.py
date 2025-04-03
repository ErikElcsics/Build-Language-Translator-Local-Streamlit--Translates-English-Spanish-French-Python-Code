import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Model mapping - only available English/Spanish/French combinations
model_mapping = {
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
}

# Available languages
available_languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr"
}


@st.cache_resource
def load_model(src_lang, tgt_lang):
    try:
        model_name = model_mapping[(src_lang, tgt_lang)]
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        return tokenizer, model
    except Exception as e:
        st.error(f"Model loading failed: {str(e)}")
        return None, None


def translate(text, src_lang, tgt_lang):
    tokenizer, model = load_model(src_lang, tgt_lang)
    if tokenizer is None or model is None:
        return "Translation unavailable"

    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        translated = model.generate(**inputs)
        return tokenizer.decode(translated[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error during translation: {str(e)}"


# Streamlit UI
st.title("🌍 Local Language Translator - Translates English, Spanish and French")
st.caption("Local translation using MarianMT models from Helsinki-NLP on Hugging Face")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("From:", list(available_languages.keys()), key="src_lang")
with col2:
    # Only show possible target languages
    src_code = available_languages[src_lang]
    possible_targets = [
        lang for lang in available_languages
        if (src_code, available_languages[lang]) in model_mapping
           and lang != src_lang
    ]
    tgt_lang = st.selectbox("To:", possible_targets, key="tgt_lang")

input_text = st.text_area("Text to translate:", height=150, key="input_text")

if st.button("Translate", key="translate_button"):
    if not input_text.strip():
        st.warning("Please enter some text!")
    else:
        with st.spinner("Translating..."):
            src_code = available_languages[src_lang]
            tgt_code = available_languages[tgt_lang]

            output = translate(input_text, src_code, tgt_code)

            if output.startswith("Error"):
                st.error(output)
            else:
                st.success("Translation:")
                st.write(output)

# Add model information
st.info("""
ℹ️ Translation models provided by Helsinki-NLP:
- English ↔ Spanish
- English ↔ French
""")