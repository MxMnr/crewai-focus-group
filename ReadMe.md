
# AI Focus Group Simulator

This application simulates a virtual focus group to gather feedback and insights on product concepts. It uses CrewAI to orchestrate AI agents that mimic different consumer personas, providing diverse perspectives on a product.

## Overview

The AI Focus Group Simulator creates a structured focus group discussion around a product concept (currently a smart water bottle). The discussion is managed by a moderator and recorded by a dedicated agent, with various consumer personas participating in the feedback process.

## Features

- **Multiple Consumer Personas**: Includes diverse perspectives such as tech-savvy millennials, budget-conscious parents, active seniors, and more
- **Structured Discussion Flow**: Follows a typical focus group format with initial reactions, feature exploration, and final reporting
- **Customizable Product Concepts**: Easily modify the product being evaluated
- **Comprehensive Reporting**: Generates detailed feedback reports with actionable insights

## Quick Start

1. Ensure you have Python 3.11+ installed
2. Clone this repository
3. Run the following command to install dependencies:

```
pip install -r requirements.txt
```

4. Run the focus group:

```
python main.py
```

## Configuration

The application uses YAML configuration files for easy customization:

- `config/agents.yaml`: Defines the personas and their characteristics
- `config/tasks.yaml`: Outlines the structure of the focus group discussion

## Customizing the Product

To evaluate a different product, modify the `PRODUCT_CONCEPT` variable in `crew.py`:

```python
PRODUCT_CONCEPT = """
Your product description here
"""
```

## Project Structure

- `main.py`: Entry point for running the focus group
- `crew.py`: Core logic for setting up the CrewAI agents and tasks
- `config/`: Contains configuration files
  - `agents.yaml`: Agent/persona definitions
  - `tasks.yaml`: Task definitions for the focus group
- `tools/`: Optional custom tools for extending agent capabilities

## Requirements

- Python 3.11+
- CrewAI 0.102.0+
- PyYAML 6.0.2+

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch for your feature
3. Add your changes
4. Submit a pull request

## License

MIT
