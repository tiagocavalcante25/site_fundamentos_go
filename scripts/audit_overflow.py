"""
audit_overflow.py
Analisa index.html e custom.css procurando qualquer elemento que possa causar overflow horizontal ou quebra em telas de 320px a 768px.
"""
import os
import re

site_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
index_path = os.path.join(site_dir, 'index.html')
css_path = os.path.join(site_dir, 'assets', 'css', 'custom.css')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()
lines = html.splitlines()

print("=== AUDIT OF ALL GRID CONTAINERS IN index.html ===")
for i, line in enumerate(lines):
    if 'grid ' in line or 'grid-cols' in line:
        cols = re.findall(r'grid-cols-[^\s\"\']+', line)
        print(f"Line {i+1} [cols: {cols}]: {line.strip()[:100]}")

print("\n=== AUDIT OF ALL BUTTONS IN index.html ===")
for i, line in enumerate(lines):
    if '<button' in line:
        print(f"Line {i+1}: {line.strip()[:100]}")
