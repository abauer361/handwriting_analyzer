import anthropic
import base64
import httpx
import streamlit as st
from PIL import Image
from io import BytesIO

# Initialize Anthropic client with API key from Streamlit secrets
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
    client = anthropic.Anthropic(api_key=api_key)
except KeyError:
    st.error("❌ ANTHROPIC_API_KEY not found in Streamlit secrets. Please add it to your secrets configuration.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error initializing Anthropic client: {e}")
    st.stop()

def analyze_handwriting(image):
    # Convert the image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Fetches image from URL and encodes it in base64 then decodes it to a UTF-8 string
    # This is required for the image to be sent to the model
    # image_url = "https://www.theparisreview.org/blog/wp-content/uploads/2018/07/matisse.jpg"
    # image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        messages=[
            {  
                "role": "user", "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": img_str
                        }
                    },
                    {
                "type": "text",
                "text": """"
                Please analyze this handwriting or signature.
                Describe the characteristics you observe and what they might indicate about the writer.
                Includes aspects like pressure, slant, size, space, and any other natable features.
                Please try to describe what the writing says.
                """
            }]}
        ]
    )

    return message.content[0].text

st.title("✍ ✍ Handwriting Analyzer ✍ ✍")

uploaded_file = st.file_uploader("Upload a handwriting or signature image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width = True)

    if st.button("Analyze Handwriting"):
        with st.spinner("Analyzing handwriting..."):
            analysis = analyze_handwriting(image)
            st.subheader("Analysis Results:")
            st.write(analysis)