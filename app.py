#!/usr/bin/env python3
"""
Flask Web UI for Engineering Drawing Analyzer
"""
import os
import base64
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from drawing_analyzer import DrawingAnalyzer

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads directory if it doesn't exist
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'tif'}


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Render the main UI."""
    return render_template('index.html')


@app.route('/api/status')
def status():
    """Check Ollama connection status."""
    try:
        analyzer = DrawingAnalyzer()
        return jsonify({
            'status': 'ready',
            'model': analyzer.model,
            'base_url': analyzer.base_url
        })
    except ConnectionError as e:
        return jsonify({
            'status': 'disconnected',
            'error': str(e)
        }), 503
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500


@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Analyze uploaded drawings with a prompt."""
    try:
        # Get files
        if 'images' not in request.files:
            return jsonify({'error': 'No images uploaded'}), 400
        
        files = request.files.getlist('images')
        if not files or files[0].filename == '':
            return jsonify({'error': 'No images selected'}), 400
        
        # Get prompt
        prompt = request.form.get('prompt', '').strip()
        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        # Get model (optional)
        model = request.form.get('model', 'llava')
        # Normalize model name - Ollama uses "llava:latest" format
        if model == 'llava' or model == 'llava:latest':
            model = 'llava:latest'
        elif model == 'bakllava':
            model = 'bakllava:latest'
        elif model == 'moondream':
            model = 'moondream:latest'
        
        # Save uploaded files
        image_paths = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                image_paths.append(filepath)
        
        if not image_paths:
            return jsonify({'error': 'No valid images uploaded'}), 400
        
        # Initialize analyzer
        analyzer = DrawingAnalyzer(model=model)
        
        # Analyze
        if len(image_paths) == 1:
            result = analyzer.analyze_drawing(image_paths[0], prompt)
        else:
            result = analyzer.analyze_multiple_drawings(image_paths, prompt)
        
        # Encode images as base64 for display
        images_data = []
        for path in image_paths:
            with open(path, 'rb') as f:
                img_data = base64.b64encode(f.read()).decode('utf-8')
                ext = Path(path).suffix[1:].lower()
                images_data.append({
                    'name': Path(path).name,
                    'data': f'data:image/{ext};base64,{img_data}'
                })
        
        return jsonify({
            'success': True,
            'result': result,
            'images': images_data,
            'model': model,
            'prompt': prompt
        })
    
    except ConnectionError as e:
        print(f"[ERROR] Connection Error: {e}")
        return jsonify({
            'error': 'Cannot connect to Ollama. Please ensure Ollama is running (ollama serve)',
            'details': str(e)
        }), 503
    except Exception as e:
        print(f"[ERROR] Analysis Exception: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': 'Analysis failed',
            'details': str(e)
        }), 500


@app.route('/api/models')
def list_models():
    """List available Ollama models."""
    try:
        import requests
        response = requests.get('http://localhost:11434/api/tags', timeout=5)
        response.raise_for_status()
        models = response.json().get('models', [])
        
        # Filter for vision models
        vision_models = [m for m in models if any(
            vm in m.get('name', '').lower() 
            for vm in ['llava', 'bakllava', 'moondream']
        )]
        
        return jsonify({
            'models': [m.get('name') for m in vision_models] if vision_models else []
        })
    except Exception as e:
        return jsonify({'models': ['llava', 'bakllava', 'moondream']}), 200


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🎯 Engineering Drawing Analyzer - Web UI")
    print("=" * 70)
    print("\n📍 Opening in browser: http://localhost:5001")
    print("\n⚠️  Make sure Ollama is running: ollama serve")
    print("\n Press Ctrl+C to stop the server\n")
    print("=" * 70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)
