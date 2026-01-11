#!/usr/bin/env python3
"""Quick test of the analyzer with a simple image"""
import sys
sys.path.insert(0, '/Users/sukantjha/Documents/Engineering Drawings')

from drawing_analyzer import DrawingAnalyzer
from PIL import Image
import io

print("Testing DrawingAnalyzer...")

try:
    # Test connection
    print("\n1. Testing Ollama connection...")
    analyzer = DrawingAnalyzer(model='llava:latest')
    print("✓ Connected to Ollama successfully")
    
    # Create a simple test image
    print("\n2. Creating test image...")
    img = Image.new('RGB', (200, 200), color='red')
    test_image_path = '/tmp/test_drawing.png'
    img.save(test_image_path)
    print(f"✓ Test image created at {test_image_path}")
    
    # Test analysis
    print("\n3. Testing analysis...")
    result = analyzer.analyze_drawing(
        test_image_path,
        "What do you see in this image?"
    )
    print(f"✓ Analysis result:\n{result[:200]}...")
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
