import streamlit as st


def main():
    st.title("CppCheck‑Py Frontend")
    
    settings = load_settings()
    st.sidebar.header("Settings")
    for key, val in settings.items():
        settings[key] = st.sidebar.text_input(key, value=str(val))
    
    uploaded = st.file_uploader("Upload C/C++ source file", type=["c", "cpp", "h"])
    if uploaded:
        code = uploaded.read().decode("utf-8")
        st.code(code, language='c')
        
        if st.button("Run CppCheck"):
            with st.spinner("Analyzing..."):
                results = run_cppcheck(code, settings)
            st.subheader("Results")
            for issue in results:
                st.markdown(f"- **{issue['severity']}**: {issue['message']} (line {issue['line']})")

if __name__ == "__main__":
    main()
