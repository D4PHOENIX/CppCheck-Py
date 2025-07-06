"""Streamlit web frontend for the C++-like syntax checker.

Allows users to upload a C/C++ source file or type code manually, and displays syntax checking results
with enhanced, human-friendly output and pretty-printed AST.
"""
import streamlit as st
from backend.src.checker import Checker
from backend.src.errors import ParserError
from backend.src.utils import pretty_print_ast

st.set_page_config(page_title="CppCheck‑Py", page_icon="🧑‍💻")
st.title("🧑‍💻 CppCheck‑Py: C++-like Syntax Checker")

st.markdown(
    """
    Upload a C/C++ source file or type your code below to check its syntax.<br>
    <small>
    <ul>
        <li>Supports a subset of C++ syntax (declarations, assignments, expressions).</li>
        <li>Shows detailed error messages with line/column and hints.</li>
        <li>Displays a readable Abstract Syntax Tree (AST) if syntax is correct.</li>
    </ul>
    </small>
    """,
    unsafe_allow_html=True,
)

mode = st.radio(
    "Choose input method:",
    ("Upload file", "Type code"),
    horizontal=True
)

code = ""
if mode == "Upload file":
    uploaded = st.file_uploader("Upload C/C++ source file", type=["c", "cpp", "h"])
    if uploaded:
        code = uploaded.read().decode("utf-8")
elif mode == "Type code":
    code = st.text_area(
        "Type or paste your C/C++ code here:",
        height=200,
        placeholder="int x;\nx = 10;\nint y;\ny = x + 5;"
    )

if code:
    st.code(code, language="c")
    if st.button("Check Syntax"):
        code = code.replace('\r\n', '\n').replace('\r', '\n')
        with st.spinner("Analyzing..."):
            try:
                program = Checker.check_syntax(code)
                st.success("✅ Syntax is correct!")
                st.markdown("**Abstract Syntax Tree (AST):**")
                st.code(pretty_print_ast(program), language="text")
            except ParserError as e:
                st.error("❌ Syntax Error detected!")
                error_lines = []
                if getattr(e, "line", None) is not None and getattr(e, "column", None) is not None:
                    error_lines.append(f"**Location:** Line {e.line}, Column {e.column}")
                error_lines.append(f"**Message:** {e.message}")
                if getattr(e, "hint", None):
                    error_lines.append(f"💡 **Hint:** {e.hint}")
                st.markdown("<br>".join(error_lines), unsafe_allow_html=True)
                # Show code with error line highlighted
                if getattr(e, "line", None):
                    code_lines = code.splitlines()
                    if 1 <= e.line <= len(code_lines):
                        st.markdown("**Error context:**")
                        st.code(
                            "\n".join(
                                f"{'>>' if i+1 == e.line else '  '} {i+1:3}: {line}"
                                for i, line in enumerate(code_lines)
                            ),
                            language="c"
                        )