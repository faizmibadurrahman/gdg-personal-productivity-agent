import os
from google.adk.agents import Agent
from .tools import get_tasks, get_schedule, add_task

# Your turn: rewrite this profile to make the agent yours.
PERSONAL_PROFILE = """
My name is John Pork.
I am a university student studying Computer Science.

My priorities:
- Academic assignments
- Clubs
- Personal wellbeing

My preferences:
- I am most productive in the morning.
- I prefer 45-minute study sessions.
- Give me a 15-minute break between sessions.
- Keep my evenings free after 8 PM.
- Prioritize upcoming deadlines.

Plan my day around my preferences,
existing commitments and unfinished tasks.
"""

root_agent = Agent(
    name="productivity_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    description="A student productivity assistant.",
    instruction="""
    You help university students organize their day.
    Use get_tasks and get_schedule to retrieve information.
    Plan the sample day, 27 November 2026, around fixed commitments and the personal profile.
    Use the profile as preferences, not as evidence of actual deadlines or events.
    Treat all sample data as fictional. Never invent deadlines or events.
    Add tasks only when explicitly requested; ask for missing details.
    Never claim a tool succeeded if it returned an error.
    """ + "\nPersonal profile:\n" + PERSONAL_PROFILE,
    tools=[get_tasks, get_schedule, add_task],
)
