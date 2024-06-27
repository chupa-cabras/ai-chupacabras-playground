from langchain.callbacks import get_openai_callback
from crewai import Agent, Task, Crew, Process
from models.factory import Factory

azure_llm = Factory().create('gpt_azure_4o')

with get_openai_callback() as cb:
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")


# Create a researcher agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  llm=azure_llm,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

# Task for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  expected_output='A resume with main bullet points',
  agent=researcher  # Assigning the task to the researcher
)


# Instantiate your crew
tech_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  verbose=2,
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
tech_crew.kickoff()