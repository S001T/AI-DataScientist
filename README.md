# AI Data Scientist

AI-powered Data Analysis Framework for Python.

## Features

* CSV and Excel loading
* Data Cleaning
* Statistics Analysis
* Correlation Analysis
* Feature Engineering
* AutoML
* Data Visualization
* OpenAI Integration
* Claude Integration
* Chat With Dataset
* SQL Agent
* HTML Reports
* Streamlit Dashboard

## Installation

```bash
pip install aidatascientist
```

## Quick Start

```python
from aidatascientist import DataAgent

agent = DataAgent()

agent.load("data.csv")

agent.clean()

stats = agent.analyze()

print(stats)
```

## AutoML Example

```python
result = agent.train_model(
    target="price"
)

print(result)
```

## AI Chat Example

```python
from aidatascientist.llm.openai_provider import OpenAIProvider

provider = OpenAIProvider(
    api_key="YOUR_API_KEY"
)

agent.connect_llm(provider)

answer = agent.ask(
    "Which features are most important?"
)

print(answer)
```

## Author

Sarkis Tamaryan

## License

MIT
