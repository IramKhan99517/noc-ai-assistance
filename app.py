
import streamlit as st

# -------- MOCK AI ENGINE --------
def get_section(section_name):
    with open("SOP_data.txt", "r") as file:
        data = file.read()

    section_tag = f"[{section_name}]"

    if section_tag not in data:
        return "SOP section not found."

    # Split content
    parts = data.split(section_tag)
    content = parts[1]

    # Remove next section
    next_section_index = content.find("[")
    if next_section_index != -1:
        content = content[:next_section_index]

    content = content.strip()

    # ✅ FORMAT HEADER (IMPORTANT)
    clean_title = section_name.replace("_", " ").title()

    return f"{clean_title}\n\n{content}"

def mock_ai_engine(question):
    q = question.lower()

    if "pos" in q:
        return get_section("POS_DOWN")

    if "network" in q or "offline" in q:
        return get_section("Store_Network_Down")

    if "setup" in q or "go-live" in q:
        return get_section("Store_Setup")

    return "No SOP matched. Please escalate to L2 NOC."

    
def generate_ticket_summary(question):
    q = question.lower()

    if "pos" in q:
        return "POS issue reported at store. Possible impact to billing operations. Initial checks recommended."

    elif "network" in q or "offline" in q:
        return "Store network connectivity issue reported. Possible WAN/ISP outage. Immediate troubleshooting required."

    elif "setup" in q:
        return "Store setup activity in progress. Validation steps required before go-live."

    else:
        return "General issue reported. Further analysis required."


# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="NOC AI Assistant",
    page_icon="🧠",
    layout="wide"
)

# -------- SIDEBAR --------
with st.sidebar:
    st.header("Foot Locker NOC AI")

    st.markdown("""
    **Purpose**
    - Assist NOC engineers
    - Standardize troubleshooting
    - Reduce MTTR
    """)

    st.caption(
        "⚠️ Prototype demo only. SOP‑driven logic.\n"
        "Future: Microsoft Copilot / Azure OpenAI integration."
    )

# -------- MAIN PAGE --------
st.title("🧠 NOC AI Assistant")
st.caption("SOP‑Driven Incident Support")

st.markdown("### 🔍 Ask an Incident or Setup Question")

question = st.text_input(
    "Example: POS down at Store 214",
    placeholder="Type store issue (POS / Network / Setup)"
)

# -------- DEMO BUTTONS --------
st.markdown("### 🚀 Quick Demo")

col1, col2, col3 = st.columns(3)

if col1.button("POS Down"):
    question = "POS down at Store 214"

if col2.button("Network Offline"):
    question = "Store network offline"

if col3.button("Store Setup"):
    question = "Checklist before store go-live"

# -------- RESPONSE --------
if question:
    with st.spinner("Analyzing SOPs..."):
        response = mock_ai_engine(question)

    st.success("SOP‑based recommendation generated")

    st.markdown("### 🛠 Troubleshooting Guidance")
    st.code(response, language="text")



if question:
    with st.spinner("Analyzing SOPs..."):
        ticket_summary = generate_ticket_summary(question)

    # ✅ Ticket Summary
    st.markdown("### 📝 Ticket Summary")
    st.info(ticket_summary)

  # -------- FOOTER --------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; font-size:12px; color:gray;'>"
    "Internal Prototype • NOC AI Assistant Curated by Iram M.Khan</p>",
    unsafe_allow_html=True
)
