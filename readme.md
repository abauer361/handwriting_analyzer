# Handwriting Analyzer 📝

Ever looked at a note and wondered if it was written by a human, an alien, or maybe your past self at 2am? This quick project uses Anthropic's Claude model to analyze and describe handwriting images—because sometimes, even AI can't tell if that's a shopping list or an ancient prophecy!

**🌐 Live Demo:** [https://handwriting-analyzer.streamlit.app/](https://handwriting-analyzer.streamlit.app/)

## What is This?

A fun, simple Streamlit web app that takes an image of handwriting and asks Claude to describe it. Great for:

- Deciphering mysterious notes
- Analyzing handwriting styles
- Finally figuring out what you meant on that cryptic sticky note from last week
- Confirming that your grocery list isn't actually a lost language
- Proving that your doctor's prescription is, in fact, illegible

## Quick Setup (Local Development)

1. **Clone this repo:**

   ```bash
   git clone <repo-url>
   cd handwriting_analyzer
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   # If you're on Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key:**
   Create a `.streamlit/secrets.toml` file:

   ```toml
   ANTHROPIC_API_KEY = "your_actual_api_key_here"
   ```

5. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```

## Deploy to Streamlit Cloud

Want to share your handwriting analyzer with the world? Deploy it to Streamlit Cloud and let others try to decipher their own mysterious notes!

1. **Push your code to GitHub** (make sure you have these files):

   - `app.py` (your main app)
   - `requirements.txt` (dependencies)
   - `.streamlit/secrets.toml` (your API key - **don't commit this!**)

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your GitHub repo** and configure:

   - **Repository:** `your-username/handwriting_analyzer`
   - **Branch:** `main`
   - **Main file path:** `app.py`

4. **Add your secrets** in the Streamlit Cloud dashboard:

   - Go to your app settings
   - Add this to the "Secrets" section:

   ```toml
   ANTHROPIC_API_KEY = "your_actual_api_key_here"
   ```

5. **Deploy!** Your app will be live at `https://your-app-name.streamlit.app/`

## Project Structure

```
handwriting_analyzer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml      # API keys (local only)
├── readme.md             # This file
└── .gitignore           # Git ignore file
```

## Requirements

- Python 3.8+ (if you don't have this, your computer's handwriting might be as mysterious as your signature)
- Anthropic API key
- Streamlit Cloud account (for deployment)

## Notes

- **Never commit your API keys** to version control (unless you want the whole internet to know your secrets)
- The app accepts JPG, JPEG, and PNG image formats
- Claude will analyze handwriting characteristics like pressure, slant, size, and spacing
- Perfect for deciphering those mysterious notes you find around the house
- If the AI can't read it, it's probably a doctor's note

## Why?

Because sometimes, you just need a second opinion on whether that's a 7, a 1, or a secret message from your cat. 🐾✍️

---

_Remember: If the AI can't read it, it's probably a doctor's note!_
