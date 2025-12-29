# Engineering Drawing Analyzer

An AI-powered tool to analyze engineering drawings using open-source vision models (Ollama + LLaVA). Load drawings, ask questions, and get detailed analysis - all running locally on your machine!

## Features

- 🎯 Analyze engineering drawings with natural language prompts
- 🖼️ Support for single or multiple drawings
- 🔒 **100% Local & Private** - runs entirely on your machine using open-source models
- 💰 **Free** - no API costs or subscriptions
- 🚀 Multiple vision models supported (LLaVA, BakLLaVA, Moondream)
- 📊 Extract dimensions, specifications, and technical details
- 🔍 Identify components, materials, and design features
- ⚡ Interactive mode for multiple queries

## Prerequisites

### 1. Install Ollama

Ollama is required to run the open-source vision models locally.

**macOS:**
```bash
brew install ollama
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download from [https://ollama.ai](https://ollama.ai)

### 2. Start Ollama Service

```bash
ollama serve
```

### 3. Pull a Vision Model

```bash
# Recommended: LLaVA (best for engineering drawings)
ollama pull llava

# Alternative models:
# ollama pull bakllava    # Good for detailed analysis
# ollama pull moondream   # Lightweight and fast
```

## Installation

1. Clone or download this repository
2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Mode

Analyze a single drawing:
```bash
python main.py path/to/drawing.png -p "What are the main dimensions shown in this drawing?"
```

Analyze multiple drawings:
```bash
python main.py drawing1.png drawing2.png -p "Compare these two designs"
```

Use a different model:
```bash
python main.py drawing.png -p "List all components" -m bakllava
```

### Interactive Mode

```bash
python -c "from main import interactive_mode; interactive_mode()"
```

Then enter your drawing path(s) and ask multiple questions interactively.

### Python API

```python
from drawing_analyzer import DrawingAnalyzer

# Initialize analyzer
analyzer = DrawingAnalyzer(model="llava")

# Analyze a drawing
result = analyzer.analyze_drawing(
    "path/to/drawing.png",
    "What materials are specified in this drawing?"
)
print(result)

# Analyze multiple drawings
result = analyzer.analyze_multiple_drawings(
    ["drawing1.png", "drawing2.png"],
    "What are the differences between these designs?"
)
print(result)
```

## Example Prompts

- "What are the main dimensions in this engineering drawing?"
- "List all the components shown in this assembly"
- "What material specifications are indicated?"
- "Identify any tolerances or technical requirements"
- "What type of engineering drawing is this (orthographic, isometric, etc.)?"
- "Extract the title block information"
- "Are there any welding symbols or surface finish specifications?"

## Supported Image Formats

- PNG
- JPEG/JPG
- BMP
- GIF
- TIFF

## Available Models

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| **llava** | ~4.5GB | Medium | High | General engineering drawings |
| **bakllava** | ~4.5GB | Medium | Very High | Detailed technical analysis |
| **moondream** | ~1.6GB | Fast | Good | Quick reviews, lighter workloads |

## Configuration

You can set environment variables in a `.env` file:

```env
OLLAMA_MODEL=llava
OLLAMA_BASE_URL=http://localhost:11434
```

## Troubleshooting

### "Cannot connect to Ollama"
- Ensure Ollama is running: `ollama serve`
- Check if the service is accessible: `curl http://localhost:11434/api/tags`

### Model not found
- Pull the model first: `ollama pull llava`
- Check available models: `ollama list`

### Slow performance
- Try a smaller model like `moondream`
- Ensure you have adequate RAM (8GB+ recommended)
- Close other resource-intensive applications

## Requirements

- Python 3.8+
- Ollama installed and running
- At least one vision model pulled (llava, bakllava, or moondream)
- 8GB+ RAM recommended

## License

MIT License - feel free to use and modify!

## Privacy & Security

All analysis happens locally on your machine. No data is sent to external servers, ensuring your engineering drawings remain private and secure.
