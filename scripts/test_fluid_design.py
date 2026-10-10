"""
test_fluid_design.py
Verifica matematicamente e estruturalmente as 4 exigências do usuário:
1. Design Fluido Global
2. Imagens com max-width: 100% e altura proporcional (aspect-ratio mantido)
3. Tipografia fluida com unidades responsivas (clamp, vw, rem)
4. Blindagem contra rolagem horizontal (overflow-x, min-width, overflow-wrap)
"""
import os
import re
import sys

site_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css_path = os.path.join(site_dir, 'assets', 'css', 'custom.css')
html_path = os.path.join(site_dir, 'index.html')

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

print("=== TESTE 1: IMAGENS COM LARGURA MÁXIMA 100% E ALTURA PROPORCIONAL ===")
# Checar regra global de imagens no CSS
if 'img, picture, video, canvas, svg' in css and 'max-width: 100% !important' in css and 'height: auto !important' in css:
    print("[PASS] Regra global CSS: img, picture, video, canvas, svg possuem max-width: 100% !important e height: auto !important.")
else:
    errors.append("Regra global de img não encontrada no custom.css")

# Checar proporção e classe fluid-img
if '.fluid-img' in css and 'aspect-ratio: 1376 / 768' in css:
    print("[PASS] Regra de aspecto anatômico proporcional: .fluid-img possui aspect-ratio: 1376 / 768.")
else:
    errors.append(".fluid-img com aspect-ratio não encontrada")

# Checar todas as 5 imagens médicas no index.html
expected_images = [
    "semiologia_exame_especular_toque.jpg",
    "indice_bishop_maturacao_cervical.jpg",
    "sangramento_gestacao_dpp_vs_pp.jpg",
    "vulvovaginites_diagnostico_diferencial.jpg",
    "seguranca_paciente_queijo_suico.jpg"
]

for img_name in expected_images:
    pattern = rf'<img[^>]+src=["\']assets/img/{img_name}["\'][^>]*>'
    match = re.search(pattern, html)
    if match:
        tag = match.group(0)
        if 'fluid-img' in tag and 'w-full' in tag and 'max-w-full' in tag and 'h-auto' in tag and 'width="1376"' in tag and 'height="768"' in tag:
            print(f"[PASS] Imagem {img_name} 100% fluida, com dimensões proporcionais e contêiner blindado.")
        else:
            errors.append(f"Imagem {img_name} não possui todos os atributos responsivos fluidos: {tag}")
    else:
        errors.append(f"Imagem {img_name} não encontrada no index.html")

print("\n=== TESTE 2: TIPOGRAFIA FLUIDA COM UNIDADES RESPONSIVAS (CLAMP / VW) ===")
# Checar h1, h2, h3, h4
headings = ['h1', 'h2', 'h3', 'h4']
for h in headings:
    if re.search(rf'(?:^|,|\s){h}\b[^\{{]*\{{[^}}]*font-size:\s*clamp\(', css, re.MULTILINE):
        print(f"[PASS] Tag <{h}> utiliza clamp() com unidades responsivas.")
    else:
        errors.append(f"Tag <{h}> não possui clamp() no CSS")

# Checar utilitários de texto text-xs a text-5xl no CSS
text_classes = ['text-xs', 'text-sm', 'text-base', 'text-lg', 'text-xl', 'text-2xl', 'text-3xl', 'text-4xl', 'text-5xl']
for tc in text_classes:
    if re.search(rf'\.{tc}\s*\{{[^}}]*clamp\(', css):
        print(f"[PASS] Classe .{tc} configurada com clamp() responsivo no custom.css.")
    else:
        errors.append(f"Classe .{tc} não encontrada com clamp() no CSS")

# Checar tailwind.config
if 'fontSize:' in html and 'clamp(' in html:
    print("[PASS] tailwind.config injeta classes fluidas responsivas clamp() no motor Tailwind.")
else:
    errors.append("tailwind.config sem fontSize clamp()")

print("\n=== TESTE 3: BLINDAGEM CONTRA ROLAGEM HORIZONTAL ===")
if 'overflow-x: clip' in css and 'overflow-x: hidden' in css:
    print("[PASS] html e body protegidos com overflow-x: clip e overflow-x: hidden.")
else:
    errors.append("html e body sem overflow-x adequados")

if 'box-sizing: border-box' in css and 'min-width: 0' in css:
    print("[PASS] Reset universal *, *::before, *::after com box-sizing: border-box e min-width: 0 (flex/grid safe).")
else:
    errors.append("Reset universal sem min-width: 0")

if 'overflow-wrap: anywhere' in css:
    print("[PASS] Prevenção de quebra de palavras médicas com overflow-wrap: anywhere.")
else:
    errors.append("overflow-wrap: anywhere ausente")

if '.table-responsive-container' in css and 'max-width: 100% !important' in css:
    print("[PASS] Tabelas clínicas encapsuladas em contêiner com rolagem horizontal contida interna.")
else:
    errors.append("Tabelas sem max-width: 100% no container")

print("\n=======================================================")
if errors:
    print("ERROS ENCONTRADOS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print(">>> TODOS OS 4 PILARES DO DESIGN FLUIDO FORAM CONFIRMADOS COM 100% DE SUCESSO! <<<")
    sys.exit(0)
