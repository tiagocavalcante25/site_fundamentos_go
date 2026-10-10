"""
verify_site.py
Verifica a integridade completa do site_fundamentos_go para deploy no GitHub Pages e Netlify.
Testa:
1. Existência e integridade de arquivos críticos e imagens HD.
2. Compatibilidade com GitHub Pages (.nojekyll, links relativos para subdiretórios de repositório).
3. Meta tags de responsividade mobile (iOS/Android/Tablets).
4. Sincronia de scripts e folhas de estilo CSS.
"""

import os
import re
import sys

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check_file(rel_path):
    full = os.path.join(SITE_DIR, rel_path)
    exists = os.path.exists(full)
    size = os.path.getsize(full) if exists else 0
    print(f"[{'PASS' if exists and size > 0 else 'FAIL'}] {rel_path} (Tamanho: {size:,} bytes)")
    return exists and size > 0

def main():
    print(f"=== VERIFICAÇÃO DE INTEGRIDADE: FUNDAMENTOS EM GO ===")
    print(f"Diretório Raiz: {SITE_DIR}\n")
    all_ok = True

    print("=== 1. ARQUIVOS PRINCIPAIS & ATIVOS ESTÁTICOS ===")
    critical_files = [
        "index.html",
        ".nojekyll",
        "netlify.toml",
        "assets/css/custom.css",
        "assets/js/app.js",
        "assets/img/sangramento_gestacao_dpp_vs_pp.jpg",
        "assets/img/vulvovaginites_diagnostico_diferencial.jpg",
        "assets/img/semiologia_exame_especular_toque.jpg",
        "assets/img/indice_bishop_maturacao_cervical.jpg",
        "assets/img/seguranca_paciente_queijo_suico.jpg"
    ]
    
    for f in critical_files:
        if not check_file(f):
            all_ok = False

    print("\n=== 2. COMPATIBILIDADE COM GITHUB PAGES (URLS RELATIVAS) ===")
    index_path = os.path.join(SITE_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Checar se há links absolutos incorretos para a raiz (ex: /assets/ em vez de assets/)
    bad_absolute_paths = re.findall(r'(?:href|src)=["\']/(assets/[^"\']+)["\']', html)
    if bad_absolute_paths:
        print(f"[ERRO] Encontrados caminhos absolutos que quebram no GitHub Pages: {bad_absolute_paths}")
        all_ok = False
    else:
        print("[PASS] Todos os caminhos de assets utilizam links relativos (compatíveis com subpastas do GitHub Pages).")

    # Checar presença do .nojekyll
    nojekyll_path = os.path.join(SITE_DIR, ".nojekyll")
    if os.path.exists(nojekyll_path):
        print("[PASS] Arquivo .nojekyll presente (Jekyll desativado para preservação total de pastas).")
    else:
        print("[ERRO] Arquivo .nojekyll não encontrado.")
        all_ok = False

    print("\n=== 3. AUDITORIA DE ASSETS EM index.html ===")
    srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
    lightboxes = re.findall(r'data-lightbox=["\']([^"\']+)["\']', html)
    links_css = re.findall(r'href=["\']([^"\']+\.css)["\']', html)

    for asset in set(srcs + lightboxes + links_css):
        if asset.startswith("http") or asset.startswith("//"):
            continue
        asset_clean = asset.split("?")[0].split("#")[0]
        full = os.path.join(SITE_DIR, asset_clean)
        if os.path.exists(full) and os.path.getsize(full) > 0:
            print(f"[PASS] Asset verificado: {asset} ({os.path.getsize(full):,} bytes)")
        else:
            print(f"[FAIL] Asset não encontrado: {asset}")
            all_ok = False

    print("\n=== 4. AUDITORIA DE RESPONSIVIDADE MOBILE & IOS ===")
    if 'viewport-fit=cover' in html:
        print("[PASS] Meta viewport configurado com 'viewport-fit=cover' para suporte a notch/Dynamic Island do iPhone.")
    else:
        print("[AVISO] 'viewport-fit=cover' ausente na meta tag viewport.")

    if 'apple-mobile-web-app-capable' in html:
        print("[PASS] Meta tags para Web App iOS (Safari PWA) configuradas.")
    else:
        print("[AVISO] Meta tags para iOS Safari PWA ausentes.")

    if 'id="fab-back-to-top"' in html:
        print("[PASS] Botão Flutuante (FAB) Voltar ao Topo presente.")
    else:
        print("[AVISO] Botão FAB Voltar ao Topo não encontrado.")

    if 'data-font-size-set' in html:
        print("[PASS] Controles dinâmicos de tamanho de fonte (A / A+ / A++) presentes no DOM.")
    else:
        print("[AVISO] Controles de tamanho de fonte não encontrados.")

    print("\n=======================================================")
    if all_ok:
        print(">>> SUCESSO TOTAL: O Portal Fundamentos em GO está 100% pronto para deploy no GITHUB PAGES! <<<")
        return 0
    else:
        print(">>> ATENÇÃO: Foram encontradas pendências a corrigir. <<<")
        return 1

if __name__ == "__main__":
    sys.exit(main())
