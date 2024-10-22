from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
import os

# Configure the LLM to use Cerebras
cerebras_llm = LLM(
    model="cerebras/llama3.1-70b",  # Replace with your chosen Cerebras model name i.e. "cerebras/llama3.1-8b"
    api_key=os.environ.get("CEREBRAS_API_KEY"), # Your Cerebras API key
    base_url="https://api.cerebras.ai/v1",
    temperature=0.5,
    # top_p=1,
    # max_completion_tokens=8192, # Max tokens for the response
    # response_format={ "type": "json_object" } # This will ensure the response is in JSON object format
)

# Agent definition
researcher = Agent(
    role='{topic} Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic} for year 2024',
    backstory='Driven by curiosity, you explore and share the latest innovations.',
    tools=[SerperDevTool()],
    llm=cerebras_llm
)

# Define a research task for the Senior Researcher agent
research_task = Task(
    description='Identify the next big trend in {topic} with pros and cons.',
    expected_output='A 3-paragraph report on emerging {topic} technologies.',
    agent=researcher,
)

def main():
    # Forming the crew and kicking off the process
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True
    )
    result = crew.kickoff(inputs={'topic': 'AI Agents'})
    print(result)

if __name__ == "__main__":
    main()