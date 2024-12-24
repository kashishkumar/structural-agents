# Structural Agent

An AI-powered structural engineering assistant that helps analyze and design structural components.

## Overview

This project implements an intelligent agent specifically designed to assist with structural engineering tasks, currently focusing on beam design calculations.

## Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Setup and Run

1. **Clone and Install**
   ```bash
   git clone <repository-url>
   cd structural-agent
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Run the Agent**
   ```bash
   python structural-agents.py
   ```

## Configuration

The agent is configured through `config.yaml`:

```

## Features

- 🏗️ Beam design calculations
- 📐 Support for LaTeX mathematical expressions
- ⚙️ Configurable agent parameters
- 📝 Markdown output support

## Dependencies

- `phi-agent`: Core agent functionality
- `python-markdown`: Markdown processing
- `python-markdown-math`: LaTeX math support
- `pyyaml`: YAML configuration
- `python-dotenv`: Environment management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Troubleshooting

- **API Key Issues**: Ensure your OpenAI API key is correctly set in the `.env` file
- **Dependencies**: Run `pip install -r requirements.txt` to ensure all packages are installed
- **Configuration**: Verify `config.yaml` syntax is correct



