import re
import streamlit as st

# Define Bloom's taxonomy categories with keywords for classification
category_keywords = {
    "Remember": ["what", "who", "when", "where", "identify", "list", "define", "recite", "name", "state", "recall", "select", "match"],
    "Understand": ["how", "prove", "why", "explain", "summarize", "describe", "outline", "elaborate", "illustrate", "predict", "interpret", "infer"],
    "Analyze": ["compare", "contrast", "analyze", "examine", "classify", "deconstruct", "diagram", "scrutinize"],
    "Apply": ["solve", "calculate", "create", "apply", "show", "demonstrate", "use", "implement", "execute"],
    "Create": ["create", "design", "invent", "compose", "propose", "develop", "construct", "synthesize", "assemble"],
    "Evaluate": ["evaluate", "assess", "judge", "justify", "critique", "validate", "prioritize", "reflect", "appraise"]
}

def preprocess(text):
    """Convert text to lowercase and remove any non-alphabetic characters."""
    return re.sub(r'[^a-z\s]', '', text.lower())

def classify_question(question, category_keywords):
    """Classify question based on Bloom's taxonomy levels using keyword matching."""
    preprocessed_question = preprocess(question)
    
    # Check each category for keywords
    for category, keywords in category_keywords.items():
        if any(keyword in preprocessed_question for keyword in keywords):
            return category  # Return the matched category
    
    return "No match found"  # Return this if no category matches

# Streamlit app
st.title("Question Classifier")
st.subheader("Bloom's Classifier")

# Input text area for question
question = st.text_area("Enter a question:", "")

# Classify button
if st.button("Classify",type="primary"):
    if question.strip():
        blooms_level = classify_question(question, category_keywords)
        st.write(f"**Predicted Bloom's Level**: {blooms_level}")
    else:
        st.write("Please enter a question to classify.")
st.subheader("Question paper generator")
st.selectbox("Select any subject",("Operating System","DSA","Java"),)
st.number_input("Number of question papers to generate",value=1)
if st.button("Generate QP",type="primary"):
    st.write("Work in progress!!")