"""Streamlit web frontend for the C++-like syntax checker.

Allows users to upload a C/C++ source file and displays syntax checking results.
"""
#TODO: Improve the streamlit app, according to the new changes in ast printing and error generating.

import streamlit as st
from backend.src.checker import Checker
from backend.src.errors import ParserError

st.title("CppCheck‑Py Minimal Frontend")

uploaded = st.file_uploader("Upload C/C++ source file", type=["c", "cpp", "h"])
if uploaded:
    code = uploaded.read().decode("utf-8")
    st.code(code, language="c")
    if st.button("Check Syntax"):
        try:
            program = Checker.check_syntax(code)
            st.success("Syntax OK! Parsed AST:")
            st.write(program)
        except ParserError as e:
            st.error(f"Syntax Error: {e}")
