# 🥗 Diet Generator — Streamlit + LangChain (Ollama)

A small Streamlit web app that generates personalized diet recommendations using a local LLM (via Ollama + LangChain). This README is tailored to the files you shared (`app.py` and `generate_diet.py`).

---

## Overview

`app.py` is the Streamlit front-end that collects user inputs (age, gender, body composition, activity level) and calls `generate_diet()` from `generate_diet.py`.
`generate_diet.py` builds a prompt and queries a local LLM via `langchain_core` + `langchain_ollama`, returning the LLM response object (whose text is available at `.content`).

This README explains how to install, configure, run, and (optionally) adapt the code.

---

## Project structure

```
.
├── app.py                 # Streamlit UI (you provided)
├── generate_diet.py       # LLM prompt + wrapper (you provided)
├── requirements.txt       # Dependencies (below sample)
├── README.md
└── .env (optional)        # Optional environment/config
```

---

## Requirements

### Python

* Python 3.9+ recommended

### Key Python packages

* streamlit
* langchain-core
* langchain-ollama
* ollama (local runtime — see note)
* (optional) python-dotenv

Example `requirements.txt` (use this or adapt to your environment):

```
streamlit>=1.24
langchain-core
langchain-ollama
python-dotenv
```

> **Important:** `langchain_ollama` expects you to have an Ollama runtime (the Ollama daemon) running locally with the model name you reference (`llama3.2` in your code). See the “Ollama / model” note below.

---

## Quick setup & run

1. Clone the repo and create a venv

```bash
git clone https://github.com/<you>/<repo>.git
cd <repo>
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

2. Install Python dependencies

```bash
pip install -r requirements.txt
```

3. Ensure Ollama & model are available (local LLM)

* Install and run Ollama on your machine (follow Ollama's official install steps).
* Pull or host the model you want and ensure its name matches `model="llama3.2"` inside `generate_diet.py`. If you use a different model name, update `generate_diet.py`.

4. Run the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL Streamlit prints (usually `http://localhost:8501`).

---

## How it works (short)

1. `app.py` collects user inputs and calls:

   ```python
   diet = generate_diet(age=age, body_comp=body_comp, activity_level=activity, gender=gender)
   st.write(diet.content)
   ```
2. `generate_diet()` builds a prompt using `PromptTemplate` and sends it to the LLM via `ChatOllama`.
3. The function returns the LLM result object `res`. The text is in `res.content`, which `app.py` displays.

---

## Notes, tips & best practices

### 1) `.content` vs plain string

* Your current `generate_diet()` returns `res` (an LLM response object). `app.py` uses `st.write(diet.content)`. That matches and will work.
* Alternative: if you prefer `generate_diet()` to return a plain string, change the last line to:

  ```python
  return res.content
  ```

  and update `app.py` to `st.write(diet)` (no `.content`).

### 2) Model name & Ollama

* `ChatOllama(model="llama3.2")` must match a model available on your local Ollama server. If you run a different model name, change this string accordingly.
* If Ollama uses a different host/port or needs environment variables, configure that per Ollama docs or via `langchain_ollama` settings.

### 3) Prompt engineering

* The `template` in `generate_diet.py` is already focused and concise. If you want more specific outputs (JSON, bullet list, calories numbers), update the template to request a strict output format (e.g., JSON or a fixed list) — that makes parsing/display easier.

### 4) Input validation & UI polishing

* Consider verifying inputs (e.g., numeric age bounds) and showing a friendly error message if something is missing.
* You can use `st.spinner(...)` around the LLM call to show progress.

### 5) Privacy & safety

* Avoid sending personally identifying or sensitive health information to any LLM you don't fully control. For production/clinical use, validate with professionals and consider privacy-compliant solutions.

---

## Example changes (optional)

### Return plain string from `generate_diet.py`

Replace:

```python
return res
```

with:

```python
return res.content
```

Then in `app.py`:

```python
diet = generate_diet(...)
st.write(diet)   # diet is a string
```

### Use a stricter JSON output

Change the template to ask the model for JSON with keys:

```
Output only valid JSON with fields:
{"calories": 2300, "macros": {"protein_g": ..., "carbs_g": ..., "fat_g": ...}, "meals": [...], "notes": "..."}
```

Then `generate_diet()` can `json.loads(res.content)` to parse and return a structured dict.

---

## Troubleshooting

* **`ModuleNotFoundError: langchain_ollama`** — confirm package installed and that your Python env is active.
* **Connection errors to Ollama** — ensure Ollama daemon is running and accessible locally.
* **Model not found** — check model name (matches `ChatOllama(model="...")`).
* **Streamlit prints but UI blank** — check the terminal for exceptions or logs; add debug prints inside `generate_diet()`.

---

## Example usage & sample output

After clicking **Generate** in Streamlit you might get a concise output like:

```
• Estimated daily calories: ~2200 kcal (maintain)
• Macros: Protein 120g, Carbs 250g, Fat 70g
• Meal timing: 3 main meals + 2 snacks; protein within 30–60 min post-exercise
• Prioritize: lean protein, whole grains, vegetables, healthy fats
• Avoid: sugary drinks, refined carbs (frequent overeating)
• Supplements: Vitamin D if deficient; Omega-3 if dietary intake is low
• Notes: Adjust calories by ±200 based on weekly weight trend
```

---

## Security & licensing

* Add a LICENSE file (e.g., MIT) if you want to open-source.
* Don’t include private API keys or PHI in the repo. Use `.env` or secrets managers for sensitive data.

---
