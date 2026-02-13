import streamlit as st

st.title("📚 AI Author Architect: Project Brief")
st.write("Complete this form to generate your professional book blueprint.")

# 1. Base Question: Genre
genre = st.selectbox(
    "What is the genre of your book?",
    ["Non-Fiction", "Fiction", "Memoir/Biography", "Business/Self-Help"]
)

# 2. Conditional Questions
if genre == "Non-Fiction" or genre == "Business/Self-Help":
    style = st.selectbox(
        f"What style of writing do you want for your {genre} book?",
        ["Educational & Academic", "Conversational & Friendly", "Direct & Professional", "Story-driven"]
    )
    target_audience = st.text_input("Who is your ideal reader? (e.g., Small business owners, History buffs)")
    key_takeaway = st.text_area("What is the #1 thing the reader should learn?")

else: # For Fiction
    style = st.selectbox(
        f"What style of writing do you want for your {genre} novel?",
        ["Dark & Atmospheric", "Fast-paced & Action-heavy", "Poetic & Descriptive", "Suspenseful"]
    )
    pov = st.radio("Point of View?", ["1st Person (I)", "3rd Person Limited (He/She)", "3rd Person Omniscient"])
    protagonist = st.text_input("Describe your main character's core conflict:")

# 3. Final Step: Generate the Prompt
if st.button("Generate Professional AI Prompt"):
    # This combines the answers into an elite prompt
    final_prompt = f"""
    ACT AS A PROFESSIONAL GHOSTWRITER. 
    Project Genre: {genre}
    Tone/Style: {style}
    Target Audience/Goal: {target_audience if 'target_audience' in locals() else protagonist}
    
    TASK: Based on these details, create a 12-chapter structural outline and a 500-word introduction that hooks the reader.
    """
    
    st.subheader("Your Custom Author Prompt:")
    st.code(final_prompt, language="text")
    st.success("You can now copy this prompt into Gemini or Claude to start your book!")
