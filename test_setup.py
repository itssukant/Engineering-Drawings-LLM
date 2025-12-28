#!/usr/bin/env python3
"""
Test and Demo Script for Engineering Drawing Analyzer

This script helps you verify that everything is set up correctly
and demonstrates the capabilities of the analyzer.
"""
import sys
from pathlib import Path
from drawing_analyzer import DrawingAnalyzer


def test_connection():
    """Test if Ollama is running and accessible."""
    print("=" * 60)
    print("TEST 1: Checking Ollama Connection")
    print("=" * 60)
    
    try:
        analyzer = DrawingAnalyzer()
        print("✓ Successfully connected to Ollama")
        print(f"  Model: {analyzer.model}")
        print(f"  API URL: {analyzer.api_url}")
        return True
    except ConnectionError as e:
        print(f"✗ Connection failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


def test_sample_image():
    """Test with a sample image if available."""
    print("\n" + "=" * 60)
    print("TEST 2: Analyzing Sample Image")
    print("=" * 60)
    
    # Look for sample images in common locations
    sample_paths = [
        Path("sample_drawings/drawing.png"),
        Path("sample.png"),
        Path("test.jpg"),
    ]
    
    sample_image = None
    for path in sample_paths:
        if path.exists():
            sample_image = path
            break
    
    if not sample_image:
        print("ℹ No sample image found. Add an image to test this feature.")
        print("  Tried paths:", [str(p) for p in sample_paths])
        return True
    
    try:
        analyzer = DrawingAnalyzer()
        print(f"✓ Found sample image: {sample_image}")
        print("  Analyzing...")
        
        result = analyzer.analyze_drawing(
            str(sample_image),
            "Briefly describe what you see in this image."
        )
        
        print(f"✓ Analysis complete!")
        print(f"\nResult:\n{result}")
        return True
    except Exception as e:
        print(f"✗ Analysis failed: {e}")
        return False


def test_models():
    """Test available models."""
    print("\n" + "=" * 60)
    print("TEST 3: Checking Available Models")
    print("=" * 60)
    
    try:
        analyzer = DrawingAnalyzer()
        import requests
        
        response = requests.get(
            f"{analyzer.base_url}/api/tags",
            timeout=5
        )
        response.raise_for_status()
        
        models = response.json().get("models", [])
        
        if not models:
            print("ℹ No models installed yet.")
            print("  Install one with: ollama pull llava")
            return False
        
        print(f"✓ Found {len(models)} model(s):")
        for model in models:
            name = model.get("name", "Unknown")
            size = model.get("size", 0)
            size_gb = size / (1024**3)
            print(f"  - {name} ({size_gb:.1f} GB)")
        
        return True
    except Exception as e:
        print(f"✗ Failed to check models: {e}")
        return False


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " Engineering Drawing Analyzer - Verification ".center(58) + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    results = {
        "Connection": test_connection(),
        "Models": test_models(),
        "Sample Analysis": test_sample_image(),
    }
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    all_passed = all(results.values())
    
    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status:8} - {test_name}")
    
    print()
    
    if all_passed:
        print("✓ All tests passed! You're ready to analyze drawings.")
        print("\nNext steps:")
        print("1. Place your engineering drawing in the same directory")
        print("2. Run: python main.py your_drawing.png -p 'Your question'")
        print("\nExample:")
        print("  python main.py drawing.png -p 'What are the main dimensions?'")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        print("\nCommon fixes:")
        print("1. Start Ollama service: ollama serve")
        print("2. Install a model: ollama pull llava")
        print("3. Check your network connection")
    
    print()
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
