import os

from langchain_openai import AzureChatOpenAI
from langchain.callbacks import get_openai_callback
from dotenv import find_dotenv, load_dotenv
from crewai import Agent, Task, Crew


#Instance Model
load_dotenv(find_dotenv())

# azure_llm = AzureChatOpenAI(
#     azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
#     api_key=os.environ.get("AZURE_OPENAI_KEY"),
#     validate_base_url=True,
# )

azure_llm = AzureChatOpenAI(
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
    deployment_name=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION"),
    openai_api_type="azure"
)

# llm = AzureChatOpenAI(
#     azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
#     api_key=os.environ.get("AZURE_OPENAI_KEY"),
#     openai_api_type="azure",
#     openai_api_version=os.environ.get("OPENAI_API_VERSION"),
# )





with get_openai_callback() as cb:
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")

# with get_openai_callback() as cb:
#     model.invoke([message])
#     print(
#         f"Total Cost (USD): ${format(cb.total_cost, '.6f')}"
#     )  # without specifying the model version, flat-rate 0.002 USD per 1k input and output tokens is used


# Instantiate Tools
#website_search_tool = WebsiteSearchTool()


#Instance Agents 
talent_acquisition_specialist_agent = Agent(
    role='Talent Acquisition Specialist',
    goal='Provide best job descriptions to attract top talent.',
    backstory='A Talent Acquisition Specialist finds, attracts, and recruits the best talent for a company.',
    llm_model=azure_llm,
    tools=[],
    function_calling_llm=azure_llm,  # Optional
    max_iter=15,  # Optional
    max_rpm=None, # Optional
    verbose=True,  # Optional
    allow_delegation=True,  # Optional
    #step_callback=my_intermediate_step_callback,  # Optional
    cache=True  # Optional
)

#Instance Tasks
task = Task(
    description='Write the best job description for a Software Enginnering Manager role.',
    expected_output='A resume with main bullet points',
    agent=talent_acquisition_specialist_agent,
    output_file='job_description.md'  # The final blog post will be saved here
)

#Instance Crew
crew = Crew(
    agents=[talent_acquisition_specialist_agent],
    tasks=[task],
    verbose=2
)

# Execute tasks
crew.kickoff()


