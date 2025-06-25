# OmarsAI

OmarsAI is a web-based chatbot powered by OpenAI's GPT-3.5 Turbo via the OpenAI API.

## Setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Set your OpenAI API key:

On Linux/macOS:
```
export OPENAI_API_KEY=your_key_here
```

On Windows:
```
set OPENAI_API_KEY=your_key_here
```

3. Run the app:

```
python app.py
```

## Deploying to Render

- Use `gunicorn app:app` as the start command.
- Add your `OPENAI_API_KEY` under "Environment Variables".