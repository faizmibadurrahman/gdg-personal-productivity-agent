# Build an agent to plan your day

GDG on Campus Universiti Malaya × REC | Let Him Cook

A simple personal productivity agent built with Google ADK and Gemini. The code is ready. Run it, try its tools, and customize how it responds.

## 1. Get started

You need Python 3.11 or 3.12, VS Code, internet access, and your own [Gemini API key](https://aistudio.google.com/app/apikey). Use only fictional task data; prompts and tool results can be sent to Gemini.

Open a terminal:

```bash
git clone https://github.com/faizmibadurrahman/gdg-personal-productivity-agent.git
cd gdg-personal-productivity-agent
```

Alternatively, download the ZIP, extract it, and open the project folder in VS Code. Run the remaining commands from the folder containing `requirements.txt`.

## 2. Set up

**Windows (PowerShell)**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item productivity_agent\.env.example productivity_agent\.env
```

Use `py -3.12` if you have Python 3.12.

**macOS / Linux**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp productivity_agent/.env.example productivity_agent/.env
```

Use Python 3.11 or 3.12 for the virtual environment. Skip the copy command if you already have a `.env` file.

Open `productivity_agent/.env` and replace `YOUR_API_KEY` with your Gemini API key. Keep this file private. Check your API project's access, quota and costs.

## 3. Run the agent

**Windows**

```powershell
.\.venv\Scripts\adk.exe web
```

**macOS / Linux**

```bash
.venv/bin/adk web
```

Open [localhost:8000](http://localhost:8000), select `productivity_agent` and start chatting. Keep the terminal running.

## 4. Try these prompts

1. What tasks do I have?
2. Plan my day on 27 November 2026 around my schedule and deadlines.
3. Add a task called Submit group assignment, due 2026-11-29, priority high.
4. Show my tasks again.

Look at the tool calls in ADK Web. The new task should appear in `productivity_agent/data.json`. The schedule is fictional and fixed to 27 November 2026.

## 5. Explore the code

| File | Purpose |
| --- | --- |
| `agent.py` | Sets the model, instructions and available tools. |
| `tools.py` | Defines `get_tasks()`, `get_schedule()` and `add_task()`. |
| `data.json` | Stores your local tasks and schedule. Created from `sample_data.json` on the first tool call. |

These files are inside `productivity_agent/`.

## 6. Your turn

Open `productivity_agent/agent.py` and find:

```python
PERSONAL_STYLE = "Be friendly and suggest realistic study breaks."
```

Change it. For example:

```python
PERSONAL_STYLE = "Act as a strict study coach. Prioritize urgent deadlines and give me a short checklist."
```

Save the file, stop ADK with `Ctrl+C`, run the same launch command again, and start a new session. Ask it to plan your day again. What changed?

Next, open `productivity_agent/data.json` and change one fictional task. Ask the agent to list your tasks again.

**Done!** You have run an AI agent, used its tools, and customized its behavior.

## Quick fixes

- Agent missing? Run ADK from the project root.
- API error? Check your key, model access and quota.
- Changes not showing? Save, restart ADK, and open a new session.
- Reset sample data: stop ADK and delete only `productivity_agent/data.json`. It will be recreated on the next tool call.

[Google ADK documentation](https://adk.dev/)
