# Engineering Drawing Analyzer

An AI-powered Python application for analyzing engineering drawings using OpenAI's Vision API (GPT-4 with vision capabilities).

## Features

- **Single or Multiple Drawing Analysis**: Analyze one or multiple engineering drawings simultaneously
- **Interactive CLI**: Command-line interface for easy interaction
- **Flexible Prompts**: Ask any questions about dimensions, materials, specifications, tolerances, etc.
- **Multiple Image Formats**: Supports PNG, JPG, JPEG, and other common image formats

## Prerequisites

- Python 3.8 or higher
- OpenAI API key with access to GPT-4 Vision models

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "Engineering Drawings"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # OR
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Usage

### Interactive Mode

Run without arguments to enter interactive mode:

```bash
python main.py
```

You'll be prompted to:
1. Enter the path(s) to your drawing image(s)
2. Ask questions about the drawings
3. Get AI-powered analysis

### Command Line Mode

Analyze a single drawing:

```bash
python main.py path/to/drawing.png -p "What are the main dimensions of this part?"
```

Analyze multiple drawings:

```bash
python main.py drawing1.png drawing2.jpg -p "Compare these two designs"
```

### Example Prompts

- "What are the overall dimensions of this part?"
- "List all the tolerances specified in this drawing"
- "What material is specified for this component?"
- "Identify all the holes and their diameters"
- "What is the surface finish requirement?"
- "Explain the assembly sequence based on this drawing"
- "Are there any geometric dimensioning and tolerancing (GD&T) symbols?"

## Project Structure

```
Engineering Drawings/
├── .env                      # Environment variables (create from .env.example)
├── .env.example             # Example environment file
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── main.py                  # CLI application entry point
├── drawing_analyzer.py      # Core analysis module
└── .github/
    └── copilot-instructions.md  # Project setup checklist
```

## API Usage and Costs

This application uses OpenAI's GPT-4 Vision API, which incurs costs based on:
- Number of tokens processed
- Number of images analyzed
- Image resolution

Monitor your usage at: https://platform.openai.com/usage

## Troubleshooting

### "API key not found" error
Make sure you've created a `.env` file and added your OpenAI API key.

### "Image file not found" error
Verify the image path is correct and the file exists.

### Module import errors
Ensure you've activated your virtual environment and installed all dependencies:
```bash
pip install -r requirements.txt
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.
