import nbformat
import os

# Load notebook
notebook_path = 'worksheet_audio.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Clear all outputs
for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.outputs = []
        cell.execution_count = None

# Save cleaned notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

file_size = os.path.getsize(notebook_path) / (1024*1024)
print(f"✅ Notebook outputs cleared successfully!")
print(f"📊 New file size: {file_size:.2f} MB")
