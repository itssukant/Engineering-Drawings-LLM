#!/bin/bash

# Engineering Drawing Analyzer Setup Script
echo "=========================================="
echo "Engineering Drawing Analyzer Setup"
echo "=========================================="
echo ""

# Check if Ollama is installed
echo "Checking for Ollama..."
if command -v ollama >/dev/null 2>&1; then
    echo "✓ Ollama is installed: $(which ollama)"
    ollama --version
else
    echo "✗ Ollama is NOT installed"
    echo ""
    echo "Please install Ollama:"
    echo "  macOS:   brew install ollama"
    echo "  Linux:   curl -fsSL https://ollama.ai/install.sh | sh"
    echo "  Windows: Download from https://ollama.ai"
    echo ""
    exit 1
fi

echo ""
echo "Checking if Ollama service is running..."
if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
    echo "✓ Ollama service is running"
else
    echo "⚠ Ollama service is NOT running"
    echo "Starting Ollama service..."
    ollama serve &
    sleep 3
    if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
        echo "✓ Ollama service started successfully"
    else
        echo "✗ Failed to start Ollama service"
        echo "Please run manually: ollama serve"
        exit 1
    fi
fi

echo ""
echo "Checking for LLaVA vision model..."
if ollama list | grep -q "llava"; then
    echo "✓ LLaVA model is already installed"
else
    echo "⚠ LLaVA model not found"
    echo "Downloading LLaVA model (this may take a few minutes)..."
    ollama pull llava
    if [ $? -eq 0 ]; then
        echo "✓ LLaVA model installed successfully"
    else
        echo "✗ Failed to install LLaVA model"
        exit 1
    fi
fi

echo ""
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "✓ Setup Complete!"
echo "=========================================="
echo ""
echo "You're ready to analyze engineering drawings!"
echo ""
echo "Quick start:"
echo "  python main.py your_drawing.png -p 'What are the dimensions?'"
echo ""
echo "For more information, see README.md"
echo ""
