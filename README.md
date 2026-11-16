# Let Him Cook: Build an agent to plan your day

GDG on Campus Universiti Malaya × Robotics Engineering Club · 27 November 2026

**Hands-on lab.** The code is already written. Your job is to get it running, follow the tool calls, then make the agent your own. You do not need to write a new app from scratch.

## 0. Before the workshop

- Python **3.11 or 3.12**, VS Code (or your editor), an internet connection.
- Git is optional if you download a ZIP.
- Your own Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey). Check model access, quota and any costs on your project. Do not share the key. Use fictional data only: Gemini receives prompts and relevant tool results.

## 1. Get the project

In a terminal, run:

```bash
git clone https://github.com/faizmibadurrahman/gdg-personal-productivity-agent.git
cd gdg-personal-productivity-agent
```

Alternatively, download the ZIP from the presentation or GitHub (**Code → Download ZIP**), extract it, and open the extracted project folder. Its name may include `-main` or `-starter`. Open that folder in VS Code (**File → Open Folder**) and open **Terminal → New Terminal**. You should see `requirements.txt` and the `productivity_agent` folder at the root. All commands below are run from there.

## 2. Install dependencies

### Windows (PowerShell)

If you installed Python 3.12 instead, replace `-3.11` with `-3.12`.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item productivity_agent\.env.example productivity_agent\.env
```

### macOS / Linux

Check that `python3 --version` shows 3.11 or 3.12 first. If another version is the default, use `python3.11` or `python3.12` instead of `python3`.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp productivity_agent/.env.example productivity_agent/.env
```

No activation is necessary with these commands. If you already created `.env`, skip the copy to avoid overwriting your key.

## 3. Add your key and start the agent

Open **`productivity_agent/.env`** in VS Code and replace `YOUR_API_KEY` with your own key. Leave the other settings unchanged unless the facilitator tells you otherwise.

```dotenv
GOOGLE_GENAI_USE_ENTERPRISE=FALSE
GOOGLE_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-3.5-flash
```

Save. Start ADK from the repository root:

**Windows**
```powershell
.\.venv\Scripts\adk.exe web
```

**macOS / Linux**
```bash
.venv/bin/adk web
```

Open [http://localhost:8000](http://localhost:8000) in your browser. Select `productivity_agent` and create a session if needed. Keep the terminal running. ADK Web is a local development interface, not a public deployment.

## 4. Try it (follow the speaker)

Copy these prompts **one at a time** into ADK Web.

| Prompt | What to look for |
| --- | --- |
| What tasks do I have? | `get_tasks` retrieves three sample tasks. |
| Plan my day on 27 November 2026 around my schedule and deadlines. | The plan includes the 09:00 lecture and 14:00 REC meeting, without overlap. It uses task and schedule data. |
| Add a task called Test robot battery, due 2026-11-29, priority high. | `add_task` returns success the first time. |
| Show my tasks again. | The added task appears, and `productivity_agent/data.json` contains it. |

Inspect tool calls/results in the ADK Web event or trace view. The wording and order of model calls may vary. The dates are deliberately fixed sample dates, not live calendar information.

## 5. Understand the code (guided walkthrough)

Only three files matter right now:

| File | What it does |
| --- | --- |
| `productivity_agent/agent.py` | Model, instructions, registered tools; edit `PERSONAL_STYLE` here. |
| `productivity_agent/tools.py` | Python functions that retrieve tasks/schedule and save new tasks. |
| `productivity_agent/data.json` | Your local fictional tasks and schedule; created on the first tool call from `sample_data.json`. |

In `agent.py`, the `tools=[...]` list exposes Python functions to the model. The model requests a tool; ADK executes the function and returns its result. A tool's docstring explains what it does.

## 6. Make it yours (required)

In `agent.py`, find:

```python
PERSONAL_STYLE = "Be friendly and suggest realistic study breaks."
```

Replace the sentence with your own, or try:

```python
PERSONAL_STYLE = "Act as an REC project assistant. Prioritize robotics milestones alongside urgent academic deadlines. Return a short checklist."
```

Save. Press **Ctrl+C** in the running terminal and restart ADK using the same command from step 3. Refresh the browser, start a **new session**, and ask the day-planning prompt again. Compare the style and priorities; factual schedule entries should remain the same.

Next, in `data.json`, change one fictional task title, priority or deadline. Save and ask `What tasks do I have?` again. This time, compare the tool result as well as the answer. Do not put personal information in the shared repo.

**Done when:** your agent runs, successfully calls at least one tool, and responds using your changed instructions or data.

### Optional stretch task (if you finish early)

Add a new function to the bottom of `tools.py`:

```python
def get_high_priority_tasks() -> dict:
    """Return unfinished high-priority tasks."""
    tasks = get_tasks()["tasks"]
    return {"tasks": [t for t in tasks
                      if t["priority"] == "high" and not t["completed"]]}
```

Import it on the `.tools` import line in `agent.py` and append it to the `tools=[...]` list. Restart ADK, create a new session, and ask `Which tasks are high priority?` Check whether the new tool is called. No extra feature is required for the core lab.

## 7. What else could ADK do? (REC)

The same model + instructions + tools pattern can work with a read-only tool that retrieves ESP32 serial logs. For example a `read_serial_logs()` function can fetch a log buffer and let the model suggest troubleshooting checks. A real integration would need a serial reader (e.g. PySerial), correct port and baud rate, bounded reads and testing. Do not give a model direct control of safety-critical hardware. The workshop's log example is simulated; no hardware setup is required.

## Stuck? Quick fixes

| Problem | Try this |
| --- | --- |
| `git` not found | Download/extract the ZIP instead. |
| `py` or `python3` not found | Install Python 3.11/3.12; reopen VS Code. |
| `adk` not found | Use the explicit `.venv` executable in step 3; check installation. |
| Agent missing from dropdown | Run from the project root containing `productivity_agent`. |
| API error 401/403 | Check your own API key and project/model permissions. |
| API error 429 | Check quota or rate limits; ask a facilitator, do not borrow a key. |
| Port 8000 already in use | Append `--port 8001` to your ADK command and open `localhost:8001`. |
| JSON decode error | Check commas/quotes in `data.json`; restore from the sample if needed. |
| Your edits seem ignored | Save; restart for Python edits; open a new session and try again. |

To reset fictional data, stop ADK and delete `productivity_agent/data.json` (only your local demo copy). The next tool call recreates it from `sample_data.json`. If API setup is blocked, pair with another participant and examine local tools with the tests below.

## Organizers / developers

- Offline test: `python -m unittest discover -s tests -v` (use the virtual environment's Python executable where needed). This checks tools with no API key.
- `google-adk==2.14.0` is pinned for consistent workshop setup; model ID is configurable via `.env`. Confirm access and dependency installation on Windows/macOS in a dry run before the event.
- Never commit `.env`, `data.json` or keys. Both local files are ignored by Git.
- Full repo only: the web slides live at `docs/index.html`. GitHub Pages: Settings → Pages → Deploy from a branch → `main` → `/docs`. The slides also contain a ZIP fallback for the starter code. Repository: [GitHub](https://github.com/faizmibadurrahman/gdg-personal-productivity-agent).
- [ADK Python quickstart](https://adk.dev/get-started/python/) · [ADK source](https://github.com/google/adk-python)

Offline tools are tested; live Gemini calls and the full ADK installation must be smoke-tested with an authorized key and network access.
