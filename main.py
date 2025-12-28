#!/usr/bin/env python3
"""
Engineering Drawing Analyzer - Command Line Interface

This script allows users to analyze engineering drawings by:
1. Loading drawing images from a directory or specific files
2. Asking questions about the drawings
3. Getting AI-powered analysis using open-source models (Ollama + LLaVA)
"""
import sys
import argparse
from pathlib import Path
from drawing_analyzer import DrawingAnalyzer


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Analyze engineering drawings using open-source AI vision models (Ollama)"
    )
    parser.add_argument(
        "image",
        nargs="+",
        help="Path to engineering drawing image(s)"
    )
    parser.add_argument(
        "-p", "--prompt",
        required=True,
        help="Question or instruction about the drawing(s)"
    )
    parser.add_argument(
        "-m", "--model",
        default="llava",
        help="Ollama vision model to use (default: llava). Options: llava, bakllava, moondream"
    )
    
    args = parser.parse_args()
    
    try:
        # Initialize analyzer
        print("Initializing Drawing Analyzer...")
        analyzer = DrawingAnalyzer(model=args.model)
        
        # Validate image paths
        image_paths = [str(Path(img).resolve()) for img in args.image]
        
        # Analyze drawings
        print(f"\nAnalyzing {len(image_paths)} drawing(s)...\n")
        
        if len(image_paths) == 1:
            result = analyzer.analyze_drawing(image_paths[0], args.prompt)
        else:
            result = analyzer.analyze_multiple_drawings(image_paths, args.prompt)
        
        # Display result
        print("=" * 80)
        print("ANALYSIS RESULT")
        print("=" * 80)
        print(result)
        print("=" * 80)
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def interactive_mode():
    """Run in interactive mode for multiple queries."""
    print("Engineering Drawing Analyzer - Interactive Mode")
    print("=" * 80)
    
    # Get image path(s)
    image_input = input("Enter path(s) to drawing image(s) (comma-separated for multiple): ")
    image_paths = [path.strip() for path in image_input.split(",")]
    
    # Initialize analyzer
    try:
        analyzer = DrawingAnalyzer()
        print(f"\nLoaded {len(image_paths)} drawing(s)")
        print("\nEnter your questions (type 'quit' or 'exit' to stop):\n")
        
        while True:
            prompt = input("Your question: ").strip()
            
            if prompt.lower() in ['quit', 'exit', 'q']:
                print("Exiting...")
                break
            
            if not prompt:
                continue
            
            print("\nAnalyzing...\n")
            
            try:
                if len(image_paths) == 1:
                    result = analyzer.analyze_drawing(image_paths[0], prompt)
                else:
                    result = analyzer.analyze_multiple_drawings(image_paths, prompt)
                
                print("-" * 80)
                print(result)
                print("-" * 80)
                print()
                
            except Exception as e:
                print(f"Error: {e}\n")
    
    except Exception as e:
        print(f"Error initializing analyzer: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments provided, run interactive mode
        interactive_mode()
    else:
        # Run with command line arguments
        main()
