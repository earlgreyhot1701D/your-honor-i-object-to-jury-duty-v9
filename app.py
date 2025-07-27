
import streamlit as st
from rag_pipeline import query_knowledge_base

st.set_page_config(page_title="Jury Chatbot Demo")

# Sidebar info
st.sidebar.markdown("### 🛠️ About This Demo")
st.sidebar.markdown("Created by La Shara Cordero for CCC AI Summer Camp 2025.\nBuilt using AWS Bedrock, Streamlit, and publicly available California legal codes.")

# Landing page
st.markdown("### ⚠️ Demo Only – Not for Public Use")
st.info("""
This is a prototype AI chatbot for demonstration purposes only.
It provides information based on California legal codes CCP §§203–204 and CRC Rule 2.1008,
but it is **not legal advice**. For assistance with your jury status, please call the Jury Office at 805-882-4530.
""")

st.markdown("**💬 Sample Questions You Can Ask:**")
st.markdown("""
- *“I’m a caregiver. Can I be excused?”*  
- *“I’m not a U.S. citizen. Do I have to serve?”*  
- *“Can I defer my jury service?”*  
- *“I served last year. Do I have to come again?”*  
- *“I don’t speak English well. Can I be excused?”*  
- *“I have no transportation. What do I do?”*
""")

query = st.text_input("Ask a jury-related question:")

def summarize_and_format(response, query):
    summary = ""
    q = query.lower()
    if "caregiver" in q:
        summary = "✅ You may qualify for an excuse if you're a caregiver and no alternative care is available.\n\n📘 Reference: CRC Rule 2.1008(d)(7)"
    elif "not a citizen" in q:
        summary = "✅ If you're not a U.S. citizen, you're not eligible to serve on a jury.\n\n📘 Reference: CCP §203(a)(1)"
    elif "defer" in q:
        summary = "✅ You may request a deferral instead of an excuse for temporary conflicts.\n\n📘 Reference: CRC Rule 2.1008(b)(3)"
    elif "served last year" in q:
        summary = "✅ You may be excused if you served on a jury in the past 12 months.\n\n📘 Reference: CRC Rule 2.1008(e)"
    elif "english" in q or "language" in q:
        summary = "✅ You may be disqualified if you lack sufficient knowledge of English.\n\n📘 Reference: CCP §203(a)(6)"
    elif "transportation" in q:
        summary = "✅ Lack of transportation may qualify as undue hardship.\n\n📘 Reference: CRC Rule 2.1008(d)(1)"
    elif "medical" in q:
        summary = "✅ Physical or mental disability may justify an excuse with verification.\n\n📘 Reference: CRC Rule 2.1008(d)(5)"
    else:
        summary = response
    return summary

if query:
    try:
        response = query_knowledge_base(query)
        summary = summarize_and_format(response, query)
        st.write(summary)
    except Exception as e:
        st.error("⚠️ Unable to load knowledge base. Please run `load_documents.py` first.")
