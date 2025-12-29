// State
let selectedFiles = [];

// DOM Elements
const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('fileInput');
const fileChips = document.getElementById('fileChips');
const promptInput = document.getElementById('prompt');
const analyzeBtn = document.getElementById('analyzeBtn');
const clearBtn = document.getElementById('clearBtn');
const btnText = document.getElementById('btnText');
const btnLoader = document.getElementById('btnLoader');
const emptyState = document.getElementById('emptyState');
const resultsContainer = document.getElementById('resultsContainer');
const statusDot = document.getElementById('statusDot');
const statusText = document.getElementById('statusText');
const modelSelect = document.getElementById('model');

// Initialize
checkOllamaStatus();
setInterval(checkOllamaStatus, 10000); // Check every 10 seconds

// Check Ollama status
async function checkOllamaStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        if (data.status === 'ready') {
            statusDot.className = 'status-dot ready';
            statusText.textContent = 'Ready';
        } else {
            statusDot.className = 'status-dot error';
            statusText.textContent = 'Disconnected';
        }
    } catch (error) {
        statusDot.className = 'status-dot error';
        statusText.textContent = 'Error';
    }
}

// Drag and drop
dropzone.addEventListener('click', () => fileInput.click());
dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.classList.add('drag-over');
});
dropzone.addEventListener('dragleave', () => {
    dropzone.classList.remove('drag-over');
});
dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.classList.remove('drag-over');
    handleFiles(e.dataTransfer.files);
});

// File input change
fileInput.addEventListener('change', (e) => {
    handleFiles(e.target.files);
});

// Handle files
function handleFiles(files) {
    selectedFiles = Array.from(files);
    updateFileChips();
    updateAnalyzeButton();
}

// Update file chips
function updateFileChips() {
    fileChips.innerHTML = '';
    selectedFiles.forEach((file, index) => {
        const chip = document.createElement('div');
        chip.className = 'file-chip';
        chip.innerHTML = `
            <span>${file.name}</span>
            <button class="remove-chip" data-index="${index}">×</button>
        `;
        fileChips.appendChild(chip);
    });
    
    // Add remove listeners
    document.querySelectorAll('.remove-chip').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const index = parseInt(e.target.dataset.index);
            selectedFiles.splice(index, 1);
            updateFileChips();
            updateAnalyzeButton();
        });
    });
}

// Update analyze button state
function updateAnalyzeButton() {
    const hasFiles = selectedFiles.length > 0;
    const hasPrompt = promptInput.value.trim().length > 0;
    analyzeBtn.disabled = !(hasFiles && hasPrompt);
}

// Prompt input change
promptInput.addEventListener('input', updateAnalyzeButton);

// Quick prompt pills
document.querySelectorAll('.pill-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        promptInput.value = btn.dataset.prompt;
        updateAnalyzeButton();
    });
});

// Clear button
clearBtn.addEventListener('click', () => {
    selectedFiles = [];
    promptInput.value = '';
    fileInput.value = '';
    updateFileChips();
    updateAnalyzeButton();
});

// Analyze button
analyzeBtn.addEventListener('click', async () => {
    if (selectedFiles.length === 0 || !promptInput.value.trim()) return;
    
    // Show loading state
    btnText.hidden = true;
    btnLoader.hidden = false;
    analyzeBtn.disabled = true;
    
    try {
        // Prepare form data
        const formData = new FormData();
        selectedFiles.forEach(file => {
            formData.append('images', file);
        });
        formData.append('prompt', promptInput.value.trim());
        formData.append('model', modelSelect.value);
        
        // Send request
        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Analysis failed');
        }
        
        // Show results
        displayResults(data);
        
    } catch (error) {
        alert(`Error: ${error.message}\n\nMake sure Ollama is running: ollama serve`);
    } finally {
        // Reset loading state
        btnText.hidden = false;
        btnLoader.hidden = true;
        updateAnalyzeButton();
    }
});

// Display results
function displayResults(data) {
    emptyState.hidden = true;
    resultsContainer.hidden = false;
    
    // Images preview
    const imagesPreview = document.getElementById('imagesPreview');
    imagesPreview.innerHTML = data.images.map(img => 
        `<img src="${img.data}" class="preview-thumb" alt="${img.name}" title="${img.name}">`
    ).join('');
    
    // Model badge
    document.getElementById('modelBadge').textContent = data.model;
    
    // Timestamp
    const now = new Date();
    document.getElementById('timestamp').textContent = now.toLocaleTimeString();
    
    // Answer
    document.getElementById('answerContent').textContent = data.result;
    
    // Scroll to results
    resultsContainer.scrollIntoView({ behavior: 'smooth' });
}

// Copy to clipboard
document.getElementById('copyBtn').addEventListener('click', () => {
    const content = document.getElementById('answerContent').textContent;
    navigator.clipboard.writeText(content).then(() => {
        const btn = document.getElementById('copyBtn');
        const originalHTML = btn.innerHTML;
        btn.innerHTML = '<span style="color: var(--accent)">✓</span>';
        setTimeout(() => {
            btn.innerHTML = originalHTML;
        }, 2000);
    });
});
