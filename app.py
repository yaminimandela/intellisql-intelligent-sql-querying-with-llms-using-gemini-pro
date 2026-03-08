import streamlit as st
import sqlite3
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Convert English to SQL
def get_sql_query(question):
    prompt = f"""
    Convert the following natural language question into SQL query.
    The database has one table named students with columns:
    id, name, age, marks.
    Only return SQL query.

    Question: {question}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return response.text.strip()

# Run SQL
def run_query(query):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Streamlit UI
st.title("IntelliSQL - Intelligent SQL Querying")

question = st.text_input("Ask your question:")

if st.button("Generate & Execute"):
    sql_query = get_sql_query(question)
    st.subheader("Generated SQL Query:")
    st.code(sql_query)

    try:
        results = run_query(sql_query)
        st.subheader("Results:")
        st.write(results)
    except Exception as e:
        st.error(f"Error: {e}")
