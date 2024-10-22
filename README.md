# CrewAI Cerebras Integration Demo

This project demonstrates the integration of [CrewAI](https://github.com/crewai/crewai) with [Cerebras AI](https://www.cerebras.net/) models for advanced AI research tasks. 
It showcases how to create an AI research crew using the CrewAI framework and leverage Cerebras' fast inference speed and large model sizes for intelligent agent interactions.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview

This demo creates an AI research crew consisting of a Senior Researcher agent. The agent is tasked with identifying emerging trends in a specified topic (default: AI Agents) for the year 2024. 
The project utilizes Cerebras AI models for natural language processing and the CrewAI framework for orchestrating AI agents and tasks.

## Prerequisites

- Python 3.7+
- [Cerebras API key](https://console.cerebras.net/keys)
- [Serper API key](https://serper.ai/) (for web search capabilities)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/tonykipkemboi/crewai-cerebras-integration-demo.git
   cd crewai-cerebras-integration-demo
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install crewai crewai-tools
   ```

## Configuration

1. Create a `.env` file in the project root and add your API keys:

   ```bash
   CEREBRAS_API_KEY=your_cerebras_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

2. Ensure the `.env` file is added to your `.gitignore` to keep your API keys secure.

## Usage

Run the demo script:

```bash
python crewai_cerebras_integration_demo.py
```

The script will execute the research task and print the results.

## Project Structure

- `crewai_cerebras_integration_demo.py`: Main script demonstrating the CrewAI and Cerebras integration.
- `.env`: Contains environment variables for API keys.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file, providing project documentation.

## How It Works

1. The script configures a Cerebras LLM using the specified model and API key.
2. A Senior Researcher agent is created with a defined role, goal, and backstory.
3. A research task is defined for the agent to identify emerging trends in the specified topic.
4. A CrewAI Crew is formed with the agent and task.
5. The crew's process is initiated, and the results are printed.

## Customization

- Modify the Cerebras model by changing the `model` parameter in the `LLM` configuration in `ai_research_crew.py`, i.e. `model="llama3.1-8b"`.
- Adjust the agent's role, goal, and backstory to fit different research scenarios.
- Change the research topic by modifying the `inputs` parameter in the `crew.kickoff()` method in `ai_research_crew.py`, i.e. `inputs="AI in healthcare"`.
- Add more agents or tasks to create more complex research crews.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy coding! 🚀
