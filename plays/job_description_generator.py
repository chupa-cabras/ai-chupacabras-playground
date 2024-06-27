import os
from langchain.callbacks import get_openai_callback
from crewai import Agent, Task, Crew
from models.factory import Factory


azure_llm = Factory().create('gpt_azure_4o')

with get_openai_callback() as cb:
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")


# Create a researcher agent
talent_acquisition_specialist_agent = Agent(
  role='Talent Acquisition Specialist',
  goal='Provide best job descriptions to attract top talent.',
  backstory='A Talent Acquisition Specialist finds, attracts, and recruits the best talent for a company.',
  verbose=True,
  llm=azure_llm,
  function_calling_llm=azure_llm
)

# #Instance Tasks
task = Task(
    description='Write the best job description for a Software Enginnering Manager role.',
    expected_output='A resume with main bullet points',
    agent=talent_acquisition_specialist_agent
)

# #Instance Crew
crew = Crew(
    agents=[talent_acquisition_specialist_agent],
    tasks=[task],
    verbose=2
)

# # Execute tasks
crew.kickoff()
