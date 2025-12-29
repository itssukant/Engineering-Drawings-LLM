# Project Overview - Engineering Drawing Analyzer (Open-Source Edition)

## ✨ What's Changed

Your project has been successfully converted from OpenAI-based to an **open-source, locally-running** solution using:
- **Ollama**: Local AI model runtime (free, runs on your machine)
- **LLaVA**: Open-source vision model for analyzing images
- **Python**: For orchestration and CLI

### Key Benefits:
✅ **Free** - No API costs  
✅ **Private** - Everything runs locally  
✅ **Fast** - No network latency  
✅ **Offline** - Works without internet  
✅ **Flexible** - Multiple model options  

---

## 📁 Project Structure

```
Engineering Drawings/
├── .env.example                 # Configuration template
├── .github/
│   └── copilot-instructions.md # Project setup checklist
├── .gitignore                   # Git ignore rules
├── .venv/                       # Python virtual environment
│
├── drawing_analyzer.py          # Core analyzer module (Ollama-based)
├── main.py                      # CLI interface
├── requirements.txt             # Python dependencies
├── setup.sh                     # Automated setup script
│
├── README.md                    # Full documentation
├── QUICKSTART.md               # Quick start guide (READ THIS FIRST!)
├── PROJECT_OVERVIEW.md         # This file
│
└── sample_drawings/            # (Optional) Add your engineering drawings here
    ├── drawing1.png
    ├── drawing2.jpg
    └── ...
```

---

## 🔄 How It Works

### Architecture:
```
Your Prompt
    ↓
main.py (CLI)
    ↓
drawing_analyzer.py (Analysis Module)
    ↓
Local Ollama Server (http://localhost:11434)
    ↓
LLaVA Vision Model (LLM)
    ↓
Image Analysis Result
```

### Flow:
1. User provides image path + prompt
2. CLI loads and encodes the image
3. Image + prompt sent to Ollama API
4. LLaVA model analyzes the image
5. Response returned and displayed

---

## 📦 File Descriptions

| File | Purpose |
|------|---------|
| `drawing_analyzer.py` | Core analyzer class using Ollama API |
| `main.py` | Command-line interface for running analyses |
| `requirements.txt` | Python package dependencies |
| `setup.sh` | Automated setup script for Ollama + models |
| `.env.example` | Configuration template |
| `README.md` | Comprehensive documentation |
| `QUICKSTART.md` | 5-minute setup guide |

---

## 🚀 Getting Started

### Quickest Way:
1. **Read [QUICKSTART.md](QUICKSTART.md)** - 5-minute guide
2. **Run setup script**:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
3. **Analyze your first drawing**:
   ```bash
   python main.py your_drawing.png -p "What are the dimensions?"
   ```

---

## 🎯 Available Models

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| **llava** | 4.5 GB | ⭐⭐⭐ | ⭐⭐⭐ | Recommended default |
| **bakllava** | 4.5 GB | ⭐⭐⭐ | ⭐⭐⭐⭐ | Maximum quality |
| **moondream** | 1.6 GB | ⭐⭐⭐⭐ | ⭐⭐ | Fast, lightweight |

### Install Additional Models:
```bash
ollama pull bakllava      # High-quality alternative
ollama pull moondream     # Fast alternative
ollama list              # See all installed models
```

---

## 💻 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|------------|
| Python | 3.8+ | 3.9+ |
| RAM | 6 GB | 16 GB |
| Disk | 5 GB | 10 GB |
| GPU | Optional | Nvidia/AMD (faster) |

---

## 🔧 Configuration

Create a `.env` file (copy from `.env.example`):
```env
OLLAMA_MODEL=llava
OLLAMA_BASE_URL=http://localhost:11434
```

---

## 📝 Usage Examples

### Analyze Single Drawing:
```bash
python main.py drawing.png -p "List all dimensions and tolerances"
```

### Analyze Multiple Drawings:
```bash
python main.py part1.png part2.png -p "Compare these designs"
```

### Use Different Model:
```bash
python main.py drawing.png -p "Quick analysis" -m moondream
```

### Python API:
```python
from drawing_analyzer import DrawingAnalyzer

analyzer = DrawingAnalyzer(model="llava")
result = analyzer.analyze_drawing(
    "drawing.png",
    "What materials are specified?"
)
print(result)
```

---

## 🐛 Troubleshooting

### Ollama not running?
```bash
ollama serve              # Start in one terminal
python main.py ...       # Use in another terminal
```

### Model download stuck?
```bash
ollama pull llava --verbose
```

### Slow performance?
- Try `moondream` (faster, less detailed)
- Ensure 8+ GB RAM available
- Close other applications
- Consider GPU acceleration (check Ollama docs)

---

## 🎓 Engineering Drawing Analysis Tips

### Good Prompts:
- "Extract all dimensions from this drawing"
- "What material specifications are shown?"
- "Identify all holes, slots, and features"
- "List any surface finish or tolerance requirements"
- "Describe the assembly or manufacturing sequence"

### Image Tips:
- Use clear, high-contrast images
- Ensure proper lighting
- Square-on photographs (minimize perspective distortion)
- Include title block if available

---

## 📚 Next Steps

1. **Try it out**: Run `python main.py sample.png -p "Analyze this drawing"`
2. **Experiment**: Test different models and prompts
3. **Integrate**: Use the `DrawingAnalyzer` class in your own scripts
4. **Optimize**: Fine-tune prompts for your specific use cases

---

## 🤝 Support

- See [README.md](README.md) for detailed documentation
- Check [QUICKSTART.md](QUICKSTART.md) for setup help
- Read code comments in `drawing_analyzer.py` and `main.py`
- Visit https://ollama.ai for Ollama documentation

---

**Welcome to local, private, free engineering drawing analysis!** 🎉
