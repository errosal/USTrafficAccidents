import nbconvert

# Convert the notebook to HTML
notebook_file = "US_Traffic_Accidents_Analysis_General_Statistics.ipynb"
output_format = 'html'

# Initialize the nbconvert exporter
html_exporter = nbconvert.HTMLExporter()

# Read the notebook file
with open(notebook_file, 'r', encoding='utf-8') as f:
    notebook_content = f.read()

# Convert the notebook content
(body, resources) = html_exporter.from_notebook_node(nbconvert.reads(notebook_content, as_version=4))

# Save the HTML output
output_file = notebook_file.replace('.ipynb', f'.{output_format}')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(body)

print(f"Notebook converted to {output_format}: {output_file}")