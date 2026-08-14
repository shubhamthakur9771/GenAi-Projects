import streamlit as st
import os
from dotenv import load_dotenv
import requests
from PIL import Image
import io

# Load env
load_dotenv()
API_KEY = os.getenv("STABILITY_API_KEY")

if not API_KEY:
    st.error("API Key not found in .env")
    st.stop()

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 Stability AI Image Generator")
st.write("Generate images using Stable Diffusion (SDXL)")

# Input
prompt = st.text_area(
    "Enter prompt:",
    "Futuristic hospital dashboard UI, dark theme, AI analytics"
)

# Generate button
if st.button("Generate Image"):

    if not prompt.strip():
        st.warning("Please enter a prompt")
        st.stop()

    url = "https://api.stability.ai/v2beta/stable-image/generate/sdxl/text-to-image"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "image/png",
        "Content-Type": "application/json"
    }

    payload = {
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            }
        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30
    }

    try:
        with st.spinner("Generating image..."):
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code != 200:
                st.error(f"Error: {response.status_code}")
                st.write(response.text)
                st.stop()

            image = Image.open(io.BytesIO(response.content))

            st.image(image, caption="Generated Image", use_container_width=True)

            # Download button
            buf = io.BytesIO()
            image.save(buf, format="PNG")

            st.download_button(
                "Download Image",
                data=buf.getvalue(),
                file_name="generated.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Error: {str(e)}")