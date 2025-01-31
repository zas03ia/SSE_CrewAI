import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Use the loaded environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
embedder = {
    "provider": "google",
    "config": {
        "api_key": GEMINI_API_KEY,
        "model": "models/embedding-001",
    },
}

# HR Support Agent Setup
hr_support = Agent(
    role="Answering Agent",
    goal="Be a professional HR representative that answers candidate queries to support the hiring process.",
    backstory=(
        "Your name is HRcomrade. You are a Harvard Graduate in Business and Social Sciences "
        "and now work at W3 Engineers as an HR manager. You are exceptional at communicating with candidates "
        "in a smooth, efficient, and supportive manner. Your job is to ensure precise answers to candidates' queries."
    ),
    allow_delegation=False,
    verbose=True,
    llm="gemini/gemini-1.5-flash",
)



# Crew Setup
class CustomCrew:
    def __init__(self, callback):
        self.callback = callback

    def create_crew(self):
        hr_conversation_task = self.create_conversational_task(hr_support, "HR representative")
        return Crew(
            agents=[hr_support],
            tasks=hr_conversation_task,
            verbose=True,
            process=Process.sequential,
            memory=False,
            embedder=embedder,
        )
    
    def create_conversational_task(self, agent, role):
        return [Task(
            name="Task1",
            description=f"You are on a call with {{candidate}}. {{candidate}} just said {{inquiry}}. Respond as a {role}.",
            expected_output="Simulate a real phone conversation, acknowledging {{inquiry}} and naturally leading to the next turn.",
            tools=[],
            agent=agent,
            callback=self.callback,
        ),
        Task(
            name="Task2",
            description=f"Say Task2",
            expected_output="Simulate a real phone conversation, acknowledging {{inquiry}} and naturally leading to the next turn.",
            tools=[],
            agent=agent,
            callback=self.callback,
        )
        ,Task(
            name="Task3",
            description=f"Say Task3.",
            expected_output="Simulate a real phone conversation, acknowledging {{inquiry}} and naturally leading to the next turn.",
            tools=[],
            agent=agent,
            callback=self.callback,
        )
        ]