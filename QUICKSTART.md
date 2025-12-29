# Quick Start Guide - Engineering Drawing Analyzer

## 🚀 5-Minute Setup

### Step 1: Install Ollama
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai
```

### Step 2: Start Ollama Service
```bash
ollama serve
```
Keep this terminal running. You can also set it to launch on startup.

### Step 3: Pull the Vision Model (in a new terminal)
```bash
ollama pull llava
```
This downloads the LLaVA model (~4.5 GB). First time only!

### Step 4: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Analyze Your First Drawing!
```bash
python main.py your_drawing.png -p "What are the main dimensions?"
```

---

## 📊 Common Usage Examples

### Get dimensions from a drawing
```bash
python main.py drawing.png -p "What are the overall dimensions of this part?"
```

### Extract specifications
```bash
python main.py drawing.png -p "List all material specifications and tolerances"
```

### Analyze multiple drawings
```bash
python main.py part1.png part2.png -p "Compare these two parts"
```

### Use a different model
```bash
python main.py drawing.png -p "Analyze this" -m moondream  # Faster but less detailed
python main.py drawing.png -p "Analyze this" -m bakllava   # More detailed
```

---

## 🎯 Engineering Drawing Analysis Tips

### Best Prompts for Drawings:
- "What are the main dimensions and tolerances shown?"
- "Identify all holes, slots, and their sizes"
- "What material is specified? Are there any surface finish requirements?"
- "Describe the assembly or manufacturing process"
- "Extract all GD&T (geometric dimensioning & tolerancing) symbols"
- "What are the title block details?"
- "Identify any welding, fastener, or special specifications"

### Tips for Best Results:
- Use high-quality, clear images of drawings
- Ensure proper lighting and contrast
- Try multiple prompts to get comprehensive information
- For complex drawings, analyze specific sections with targeted prompts

---

## 🔧 Troubleshooting

### Ollama won't start
```bash
# Check if port 11434 is in use
lsof -i :11434

# Try different port
# Edit your code to use: base_url="http://localhost:11435"
```

### Model is slow
Try `moondream` instead of `llava` for faster analysis (less detailed but faster)

### Running out of memory
Close other applications or try `moondream` which is smaller

### Model not found error
```bash
# Check what models you have
ollama list

# Pull the model you want
ollama pull llava
ollama pull bakllava
ollama pull moondream
```

---

## 📚 More Information

See [README.md](README.md) for detailed documentation.

---

**Enjoy analyzing your engineering drawings locally and privately!** 🎯
