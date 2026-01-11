"""
Engineering Drawing Analyzer using Ollama with Open-Source Vision Models
"""
import os
import base64
from pathlib import Path
from typing import Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class DrawingAnalyzer:
    """Analyze engineering drawings using open-source AI vision models via Ollama."""
    
    def __init__(self, model: str = "llava", base_url: Optional[str] = None):
        """
        Initialize the DrawingAnalyzer.
        
        Args:
            model: Model name to use (default: llava - LLaVA vision model)
                   Other options: bakllava, llava-phi3, moondream
            base_url: Ollama API base URL (default: http://localhost:11434)
        """
        self.model = model or os.getenv("OLLAMA_MODEL", "llava")
        self.base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        self.api_url = f"{self.base_url}/api/generate"
        
        # Verify Ollama is running
        self._check_ollama_connection()
    
    def _check_ollama_connection(self):
        """Check if Ollama is running and accessible."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.base_url}. "
                f"Please ensure Ollama is installed and running. "
                f"Install: 'brew install ollama' (macOS) or visit https://ollama.ai\n"
                f"Start: 'ollama serve'\n"
                f"Pull model: 'ollama pull {self.model}'\n"
                f"Error: {e}"
            )
    
    def encode_image(self, image_path: str) -> str:
        """
        Encode image to base64 string.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Base64 encoded string of the image
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def analyze_drawing(self, image_path: str, prompt: str) -> str:
        """
        Analyze an engineering drawing with a user prompt.
        
        Args:
            image_path: Path to the engineering drawing image
            prompt: User's question or instruction about the drawing
            
        Returns:
            AI response analyzing the drawing based on the prompt
        """
        # Validate image path
        if not Path(image_path).exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Encode image
        base64_image = self.encode_image(image_path)
        
        # Prepare the payload for Ollama
        payload = {
            "model": self.model,
            "prompt": prompt,
            "images": [base64_image],
            "stream": False
        }
        
        # Call Ollama API
        try:
            # Increase timeout for M1/M2 Macs which take longer for first run
            response = requests.post(self.api_url, json=payload, timeout=300)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "No response from model")
        except requests.exceptions.ReadTimeout as e:
            raise RuntimeError(f"Model took too long to respond (timeout after 300s). Try again - it should be faster on subsequent runs.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error calling Ollama API: {e}")
    
    def analyze_multiple_drawings(self, image_paths: list[str], prompt: str) -> str:
        """
        Analyze multiple engineering drawings with a user prompt.
        
        Args:
            image_paths: List of paths to engineering drawing images
            prompt: User's question or instruction about the drawings
            
        Returns:
            AI response analyzing the drawings based on the prompt
        """
        # Validate image paths
        for image_path in image_paths:
            if not Path(image_path).exists():
                raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Encode all images
        base64_images = [self.encode_image(img_path) for img_path in image_paths]
        
        # Prepare the payload for Ollama with multiple images
        payload = {
            "model": self.model,
            "prompt": f"{prompt}\n\nNote: Analyzing {len(image_paths)} drawings together.",
            "images": base64_images,
            "stream": False
        }
        
        # Call Ollama API
        try:
            response = requests.post(self.api_url, json=payload, timeout=300)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "No response from model")
        except requests.exceptions.ReadTimeout as e:
            raise RuntimeError(f"Model took too long to respond (timeout after 300s). Try again - it should be faster on subsequent runs.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error calling Ollama API: {e}")
