import streamlit as st
from google import genai

# ==========================================
# CONFIG
# ==========================================

GEMINI_API_KEY = st.secrets["AIzaSyDpLzBTLME8kjaog1Uy8JZelSpkoP31BWY"]

# ==========================================
# PAGE
# ==========================================

st.set_page_config(
    page_title="Real Estate AI Video Planner",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Real Estate AI Video Planner")

st.write(
    "Paste property information and generate a complete short-form video plan with timeline, script and Veo prompts."
)

# ==========================================
# INPUT
# ==========================================

project_copy = st.text_area(
    "Property Information",
    height=300,
    placeholder="Paste property description here..."
)

# ==========================================
# BUTTON
# ==========================================

if st.button("🚀 Generate Video Plan"):

    if not project_copy.strip():
        st.error("Please enter property information.")
        st.stop()

    try:

        client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        prompt = f"""
You are an expert real estate marketing strategist, copywriter and AI video director.

Your task is to transform the provided property information into a highly engaging short-form real estate advertisement.

==================================================
PRIMARY OBJECTIVE
==================================================

Generate a complete short-form video plan that can be used directly for AI video generation.

The final output must contain:

1. Video Summary
2. Master Script
3. Timeline
4. Scene Breakdown
5. Final Veo Prompts

==================================================
IFORMATION PRIORITY:
==================================================
==================================================
FACT-FIRST SCRIPT RULES
==================================================

The video should be information-dense.

Every scene must communicate at least one specific project detail.

Examples of acceptable information:

- apartment sizes
- number of towers
- land area
- amenities
- clubhouse details
- green spaces
- connectivity
- ceiling heights
- balcony sizes
- elevator ratios
- location advantages
- floor plans
- project density
- special offers
- inventory advantages

Avoid scenes that only contain praise.

Do NOT create scenes that say things like:

- luxury redefined
- world-class lifestyle
- iconic address
- statement of elegance
- premium living at its finest
- visionary development

unless accompanied by specific supporting facts.

Every scene should answer at least one question:

- What does the buyer get?
- Why is this feature useful?
- What makes this project different?
- What problem does this solve?

The script should follow:

20% Hook + Emotion

80% Concrete Information

If forced to choose between marketing language and useful information,
always choose useful information.

By the end of the video the viewer should clearly remember:

- project name
- location
- major amenities
- apartment features
- connectivity benefits
- unique selling points
- call to action

==================================================
VIDEO RULES
==================================================

- Maximum total duration: 60 seconds
- Each scene must be exactly 8 seconds
- Decide scene count automatically
- Create a strong hook
- Remove repetitive information
- Prioritize strongest selling points
- Prioritize strongest lifestyle benefits
- Prioritize strongest connectivity benefits
- End with a strong CTA

==================================================
DIALOGUE RULES
==================================================

- Dialogue must sound natural when spoken aloud
- Avoid corporate jargon
- Avoid long sentences
- One main idea per scene
- Maximum 20 spoken words per scene
- Target 15-20 words per scene
- Never exceed 25 words
If forced to choose between marketing language and useful information, always choose useful information.

==================================================
PRESENTER BEHAVIOR
==================================================

Assume a professional real estate consultant seated behind a modern office desk.

Maintain:

- direct eye contact
- natural blinking
- natural breathing
- relaxed shoulders
- hands resting on desk
- occasional subtle hand gestures
- minimal body movement
- minimal head movement
- slight nods
- slight smiles
- realistic speaking behavior

Avoid:

- influencer behavior
- dramatic acting
- excessive gestures
- theatrical movement

==================================================
CAMERA RULES
==================================================

- Medium shot
- Eye-level camera
- Static camera
- No zoom
- No camera shake
- No dramatic movement
- Natural framing
- Professional composition

==================================================
VISUAL RULES
==================================================

- Ultra realistic
- Shot on iPhone 16 Pro
- Premium corporate office
- Natural daylight through windows
- Modern professional environment
- Realistic facial motion
- Realistic eye movement
- Realistic speaking behavior
- Realistic hand movement
- Realistic lip synchronization

==================================================
OUTPUT FORMAT
==================================================

VIDEO SUMMARY

MASTER SCRIPT

TIMELINE

SCENE BREAKDOWN

For each scene include:

SCENE NUMBER
TIME
DIALOGUE
SCENE PURPOSE

PERFORMANCE DIRECTION

Facial Expression:
Eye Behavior:
Head Movement:
Hand Gestures:
Posture:
Body Movement:
Speaking Style:
Emphasis Points:

==================================================
SCENE PROMPTS
==================================================

Generate one FINAL VEO PROMPT for every scene.

Each prompt must include:

- environment
- camera
- performance
- realism instructions
- exact dialogue

At the end include:

DIALOGUE TO SPEAK:

"exact dialogue"

Speak this exact dialogue naturally.

Synchronize realistic lip movement.

Complete dialogue naturally within the 8-second scene.

Maintain direct eye contact.

Maintain realistic speaking pace.

Maintain subtle realistic gestures.

==================================================
IMPORTANT
==================================================

Do NOT describe:

- gender
- face
- age
- hairstyle
- clothing
- presenter identity

Focus entirely on:

- behavior
- performance
- realism
- dialogue delivery
- camera direction

==================================================
PROPERTY INFORMATION
==================================================

{project_copy}
"""

        with st.spinner("Generating video plan..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            result = response.text

        st.success("Video plan generated successfully!")

        st.text_area(
            "Generated Video Plan",
            value=result,
            height=700
        )

        st.download_button(
            label="📥 Download TXT",
            data=result,
            file_name="video_plan.txt",
            mime="text/plain"
        )

    except Exception as e:

        st.error(f"Error: {e}")