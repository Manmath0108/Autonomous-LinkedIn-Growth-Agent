import streamlit as st
from run.generate_week import generate_week

st.set_page_config(
    page_title="Autonomous LinkedIn Growth Agent",
    layout="centered"
)

st.title("🚀 Autonomous LinkedIn Growth Agent")
st.caption("Generate a week of LinkedIn content using AI")

st.markdown("### 🔧 Input Details")

# ---- User Inputs ----
profile_description = st.text_area(
    "🧑‍💼 Profile Description",
    placeholder="Describe your background, role, and current position",
    height=120
)

expertise = st.text_input(
    "🧠 Expertise",
    placeholder="e.g. Generative AI, NLP, Backend Engineering"
)

target_audience = st.text_input(
    "🎯 Target Audience",
    placeholder="e.g. Recruiters, Founders, AI Engineers, Students"
)

topic = st.text_area(
    "📝 Topic",
    placeholder="What should the LinkedIn content be about?",
    height=120
)

# ---- Action ----
if st.button("Generate Weekly Content"):
    if not all([
        profile_description.strip(),
        expertise.strip(),
        target_audience.strip(),
        topic.strip()
    ]):
        st.warning("Please fill in **all fields** before generating.")
    else:
        with st.spinner("Running your AI agent..."):

            user_profile = {
                "profile_description": profile_description,
                "expertise": expertise,
                "target_audience": target_audience
            }

            result = generate_week(
                user_profile=user_profile,
                topic=topic
            )

        st.success("Weekly content generated successfully!")
        st.markdown("### 📅 Generated LinkedIn Posts")
        if isinstance(result, list):
            for idx, post_obj in enumerate(result, start=1):
                st.markdown(f"## POST {idx}")

                if isinstance(post_obj, dict):
                    # Try common keys safely
                    content = (
                        post_obj.get("content")
                        or post_obj.get("post")
                        or post_obj.get("text")
                        or str(post_obj)
                    )
                    st.markdown(content)
                else:
                    st.markdown(str(post_obj))

                st.markdown("---")

        else:
            # Fallback (string or unexpected type)
            st.text_area(
                label="Output",
                value=str(result),
                height=450
            )



