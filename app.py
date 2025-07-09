import anthropic
import base64
import httpx

client = anthropic.Anthropic()

# Fetches image from URL and encodes it in base64 then decodes it to a UTF-8 string
# This is required for the image to be sent to the model
image_url = "https://www.theparisreview.org/blog/wp-content/uploads/2018/07/matisse.jpg"
image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")

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
                        "media_type": "image/jpeg",
                        "data": image_data
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

print(message.content)