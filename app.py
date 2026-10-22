import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="AI Code Reviewer & Bug Fixing Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Code Reviewer & Bug Fixing Agent")
st.markdown("Paste your source code below to detect bugs, get explanations, and receive optimized production-ready fixes instantly.")

# Layout: Two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input Code")
    code_input = st.text_area("Paste your Python, JavaScript, or any code snippet here:", height=350, placeholder="def add(a, b):\n    return a + b")
    
    analyze_btn = st.button("🚀 Analyze & Fix Code", type="primary")

with col2:
    st.subheader("🔍 AI Analysis & Recommendations")
    
    if analyze_btn:
        if not code_input.strip():
            st.warning("⚠️ Please enter some code to analyze.")
        else:
            with st.spinner("Analyzing code with Groq LLM agent..."):
                try:
                    # FastAPI backend endpoint connection
                    response = requests.post(
                        "http://127.0.0.1:8000/api/review",
                        json={"code": code_input}
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        
                        # Display Bugs Found
                        st.error("🚨 **Bugs / Issues Detected:**")
                        bugs = result.get("bugs_found", [])
                        if bugs:
                            for bug in bugs:
                                st.markdown(f"- {bug}")
                        else:
                            st.success("No major bugs detected!")
                            
                        # Display Explanation
                        st.info("💡 **Explanation:**")
                        st.write(result.get("explanation", "No explanation provided."))
                        
                        # Display Fixed Code
                        st.subheader("✨ **Optimized & Fixed Code:**")
                        st.code(result.get("fixed_code", "# No code returned"), language="python")
                        
                    else:
                        st.error(f"❌ Server Error: {response.text}")
                        
                except requests.exceptions.ConnectionError:
                    st.error("❌ Could not connect to FastAPI backend. Make sure the backend server is running (`python -m uvicorn backend.main:app --reload`).")