# Handwriting Analyzer 📝

Ever looked at a note and wondered if it was written by a human, an alien, or maybe your past self at 2am? This quick project uses Anthropic's Claude model to analyze and describe handwriting images—because sometimes, even AI can't tell if that's a shopping list or an ancient prophecy!

## What is This?

A fun, simple Python project that takes an image of handwriting and asks Claude to describe it. Great for:

- Deciphering mysterious notes
- Analyzing handwriting styles
- Finally figuring out what you meant on that cryptic sticky note from last week
- Confirming that your grocery list isn't actually a lost language

## Setup Instructions

1. **Clone this repo** (if you haven't already):

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
   pip install anthropic httpx
   ```

4. **Set your Anthropic API key:**

   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   # (Replace 'your_api_key_here' with your actual key)
   ```

5. **Run the app:**
   ```bash
   python3 app.py
   ```

## Notes

- Make sure you have Python 3.8+ installed. If you don't, your computer's handwriting might be as mysterious as your signature.
- The app fetches a sample handwriting image and asks Claude to describe it. You can swap in your own images for more fun (or confusion).

## Why?

Because sometimes, you just need a second opinion on whether that's a 7, a 1, or a secret message from your cat. 🐾✍️

---

_Remember: If the AI can't read it, it's probably a doctor's note._
