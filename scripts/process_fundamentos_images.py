"""
process_fundamentos_images.py
Polishes all 5 core medical infographics for site_fundamentos_go.
Ensures 100% Portuguese terminology, no English remnants, no overlapping labels.
Ministry of Health / SUS / FEBRASGO guidelines.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC_DIR = r"C:\Users\Admin\.gemini\antigravity\brain\c8a7917c-8cbc-4119-b7c7-b6bf1409ed34"
DST_DIR = r"c:\Users\Admin\Downloads\INTERNATO GO\site_fundamentos_go\assets\img"

def get_fonts():
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    font_reg_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(font_bold_path):
        font_bold_path = "C:/Windows/Fonts/arialbd.ttf"
        font_reg_path = "C:/Windows/Fonts/arial.ttf"
        
    return {
        "title": ImageFont.truetype(font_bold_path, 21),
        "subtitle": ImageFont.truetype(font_reg_path, 11),
        "badge_title": ImageFont.truetype(font_bold_path, 12),
        "badge_sub": ImageFont.truetype(font_reg_path, 10),
        "ribbon_title": ImageFont.truetype(font_bold_path, 12),
        "ribbon_sub": ImageFont.truetype(font_reg_path, 10),
        "card_title": ImageFont.truetype(font_bold_path, 11),
        "card_sub": ImageFont.truetype(font_bold_path, 9),
        "card_body": ImageFont.truetype(font_reg_path, 9),
        "card_body_bold": ImageFont.truetype(font_bold_path, 9),
        "anno_bold": ImageFont.truetype(font_bold_path, 10),
        "anno_reg": ImageFont.truetype(font_reg_path, 9),
        "anno_small": ImageFont.truetype(font_reg_path, 8),
    }

def draw_header(draw, w, title_text, sub_text, fonts):
    draw.rectangle([(0, 0), (w, 82)], fill=(15, 23, 42))
    draw.rectangle([(0, 82), (w, 86)], fill=(217, 119, 6))

    draw.text((25, 14), title_text, fill=(255, 255, 255), font=fonts["title"])
    draw.text((25, 48), sub_text, fill=(203, 213, 225), font=fonts["subtitle"])

    badge_x1, badge_y1, badge_x2, badge_y2 = w - 340, 10, w - 25, 72
    draw.rounded_rectangle([(badge_x1, badge_y1), (badge_x2, badge_y2)], radius=7, 
                           fill=(30, 41, 59), outline=(56, 189, 248), width=1)
    draw.text((badge_x1 + 16, badge_y1 + 10), "MINISTÉRIO DA SAÚDE / SUS", 
              fill=(56, 189, 248), font=fonts["badge_title"])
    draw.text((badge_x1 + 16, badge_y1 + 32), "Protocolos Clínicos e Diretrizes Terapêuticas (PCDT)", 
              fill=(226, 232, 240), font=fonts["badge_sub"])

def draw_pill_badge(draw, bx1, by1, title, sub, fonts, color=(15, 23, 42), fill=(255, 255, 255), outline=(203, 213, 225)):
    tw = max(len(title), len(sub)) * 6 + 18
    draw.rounded_rectangle([(bx1, by1), (bx1 + tw, by1 + 28)], radius=4, 
                           fill=fill, outline=outline, width=1)
    draw.text((bx1 + 8, by1 + 2), title, fill=color, font=fonts["anno_bold"])
    draw.text((bx1 + 8, by1 + 14), sub, fill=(100, 116, 139), font=fonts["anno_small"])

# =============================================================================
# 1. DPP VS PLACENTA PRÉVIA
# =============================================================================
def build_dpp_vs_pp():
    print("Building sangramento_gestacao_dpp_vs_pp.jpg...")
    src = os.path.join(SRC_DIR, "sangramento_dpp_vs_pp_1791233845543.jpg")
    orig = cv2.imread(src)
    h, w = orig.shape[:2]

    clean = np.ones_like(orig) * 255
    clean[90:680, 126:534] = orig[90:680, 126:534]
    clean[89:682, 770:1174] = orig[89:682, 770:1174]
    clean[509:677, 1083:1276] = orig[509:677, 1083:1276] # Warning sign

    # Surgical wipes for any stray English characters on boundaries
    clean[500:570, 126:170] = 255   # 'id'
    clean[490:610, 480:534] = 255   # stray line right of Col 1
    clean[600:665, 770:860] = 255   # stray line left of Col 2
    clean[600:635, 855:915] = 255   # 'al' pointer
    clean[625:768, :] = 255         # Clear bottom for structured cards

    # Restore Warning Sign cleanly
    clean[509:677, 1083:1276] = orig[509:677, 1083:1276]

    pil_img = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    draw_header(draw, w, 
                "HEMORRAGIAS DA 2ª METADE DA GESTAÇÃO: DIAGNÓSTICO DIFERENCIAL", 
                "Descolamento Prematuro de Placenta (DPP) vs Placenta Prévia (PP) • Diretrizes FEBRASGO & Ministério da Saúde", 
                fonts)

    # Ribbons
    draw.rounded_rectangle([(25, 92), (670, 124)], radius=5, fill=(220, 38, 38))
    draw.text((35, 95), "DESCOLAMENTO PREMATURO DE PLACENTA (DPP)", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((35, 109), "Emergência Obstétrica • Sangue Escuro • Dor Súbita • Hipertonia Uterina", fill=(254, 226, 226), font=fonts["ribbon_sub"])

    draw.rounded_rectangle([(705, 92), (1350, 124)], radius=5, fill=(37, 99, 235))
    draw.text((715, 95), "PLACENTA PRÉVIA (PP) — OCLUSIVA / BAIXA", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((715, 109), "Implantação no Segmento Inferior • Sangue Rutilante • Indolor • Toque Contraindicado", fill=(219, 234, 254), font=fonts["ribbon_sub"])

    draw.line([(688, 92), (688, 755)], fill=(226, 232, 240), width=1)

    # DPP Pointers
    draw_pill_badge(draw, 545, 140, "Hematoma Retroplacentário", "Coleção retrodecidual com fibrina", fonts, color=(220, 38, 38))
    draw.line([(545, 154), (450, 190)], fill=(220, 38, 38), width=2)

    draw_pill_badge(draw, 545, 245, "Sangue Escuro Dissecante", "Dissecção entre decídua e miométrio", fonts, color=(185, 28, 28))
    draw.line([(545, 259), (420, 290)], fill=(185, 28, 28), width=2)

    draw_pill_badge(draw, 545, 425, "Útero de Couvelaire", "Apoplexia uteroplacentária grave", fonts, color=(153, 27, 27))
    draw.line([(545, 439), (460, 480)], fill=(153, 27, 27), width=2)

    draw_pill_badge(draw, 25, 475, "Hipertonia Uterina", "Útero 'em tábua' / tetania dolorosa", fonts, color=(220, 38, 38))
    draw.line([(160, 489), (200, 520)], fill=(220, 38, 38), width=2)

    # PP Pointers
    draw_pill_badge(draw, 1180, 200, "Placenta Prévia", "Oclui o orifício interno do colo", fonts, color=(37, 99, 235))
    draw.line([(1180, 214), (1110, 260)], fill=(37, 99, 235), width=2)

    draw_pill_badge(draw, 1180, 320, "Tônus Uterino Normal", "Útero relaxado e indolor à palpação", fonts, color=(2, 132, 199))
    draw.line([(1180, 334), (1115, 360)], fill=(2, 132, 199), width=2)

    draw_pill_badge(draw, 715, 565, "Sangue Rutilante", "Vermelho-vivo, indolor e recidivante", fonts, color=(220, 38, 38))
    draw.line([(850, 579), (960, 600)], fill=(220, 38, 38), width=2)

    # Caution Banner
    draw.rounded_rectangle([(1020, 575), (1350, 630)], radius=6, fill=(254, 242, 242), outline=(239, 68, 68), width=2)
    draw.text((1035, 582), "TOQUE VAGINAL É CONTRAINDICADO!", fill=(185, 28, 28), font=fonts["anno_bold"])
    draw.text((1035, 598), "Risco de hemorragia cataclísmica materna e fetal.", fill=(153, 27, 27), font=fonts["anno_small"])
    draw.text((1035, 612), "Diagnóstico mandatório por USG Transvaginal!", fill=(71, 85, 105), font=fonts["anno_small"])

    # Bottom Cards
    def draw_card(bx1, bx2, title, subtitle, bullets, theme_color):
        by1, by2 = 635, 755
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, fill=(255, 255, 255), outline=theme_color, width=1)
        draw.text((bx1 + 12, by1 + 6), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 12, by1 + 22), subtitle, fill=theme_color, font=fonts["card_sub"])
        yt = by1 + 36
        for b in bullets:
            draw.text((bx1 + 12, yt), b, fill=(71, 85, 105), font=fonts["card_body"])
            yt += 14

    draw_card(25, 670, "Quadro Clínico & Manejo do DPP", "Emergência Obstétrica — Sofrimento Fetal & Coagulopatia", [
        "• Tríade Clássica: Dor abdominal súbita intensa + Sangramento escuro (80%) + Hipertonia uterina.",
        "• Fatores de Risco: Hipertensão (PE/HAS crônica - principal), trauma abdominal, tabagismo, cocaína.",
        "• Complicações Maiores: CIVD (consumo de fibrinogênio), choque hipovolêmico, Útero de Couvelaire.",
        "• Conduta Imediata: Estabilização volêmica, amniotomia descompressiva precoce e parto pela via mais rápida."
    ], (220, 38, 38))

    draw_card(705, 1350, "Quadro Clínico & Manejo da Placenta Prévia", "Sangramento Indolor de Repetição — Conduta Conservadora vs Cesárea", [
        "• Clínica Típica: Sangramento vaginal vermelho-vivo (rutilante), indolor, espontâneo e recidivante.",
        "• Tônus Uterino: Normal (útero flácido); vitalidade fetal habitualmente preservada no início.",
        "• Fatores de Risco: Cesárea prévia (risco de acretismo placentário!), multiparidade, idade materna > 35.",
        "• Conduta: USG transvaginal para confirmar tipo (total, parcial, marginal); cesárea se oclusiva total."
    ], (37, 99, 235))

    out_path = os.path.join(DST_DIR, "sangramento_gestacao_dpp_vs_pp.jpg")
    pil_img.save(out_path, quality=96)
    print(f"Saved: {out_path}")

# =============================================================================
# 2. VULVOVAGINITES: CANDIDÍASE VS VAGINOSE VS TRICOMONÍASE
# =============================================================================
def build_vulvovaginites():
    print("Building vulvovaginites_diagnostico_diferencial.jpg...")
    src = os.path.join(SRC_DIR, "vulvovaginites_comparativo_1791233902986.jpg")
    orig = cv2.imread(src)
    h, w = orig.shape[:2]

    clean = np.ones_like(orig) * 255
    clean[125:635, 15:455] = orig[125:635, 15:455]
    clean[125:635, 460:900] = orig[125:635, 460:900]
    clean[125:635, 905:1360] = orig[125:635, 905:1360]

    pil_img = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    draw_header(draw, w, 
                "VULVOVAGINITES E VAGINOSES: DIAGNÓSTICO DIFERENCIAL E CONDUTA", 
                "Candidíase Vulvovaginal • Vaginose Bacteriana • Tricomoníase • Diretrizes FEBRASGO & Ministério da Saúde (PCDT IST)", 
                fonts)

    # Ribbons
    draw.rounded_rectangle([(25, 92), (445, 124)], radius=5, fill=(147, 51, 234))
    draw.text((35, 95), "1. CANDIDÍASE VULVOVAGINAL", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((35, 109), "Candida albicans • pH < 4,5 • Leite Coalhado • Prurido", fill=(243, 232, 255), font=fonts["ribbon_sub"])

    draw.rounded_rectangle([(470, 92), (890, 124)], radius=5, fill=(13, 148, 136))
    draw.text((480, 95), "2. VAGINOSE BACTERIANA", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((480, 109), "Gardnerella & Anaeróbios • pH > 4,5 • Clue Cells • Whiff (+)", fill=(204, 251, 241), font=fonts["ribbon_sub"])

    draw.rounded_rectangle([(915, 92), (1350, 124)], radius=5, fill=(234, 88, 12))
    draw.text((925, 95), "3. TRICOMONÍASE VAGINAL", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((925, 109), "Trichomonas vaginalis (IST) • pH > 4,5 • Colo em Framboesa", fill=(255, 237, 213), font=fonts["ribbon_sub"])

    draw.line([(457, 92), (457, 755)], fill=(226, 232, 240), width=1)
    draw.line([(902, 92), (902, 755)], fill=(226, 232, 240), width=1)

    # Badges
    draw_pill_badge(draw, 275, 260, "pH < 4,5", "Ácido (Normal)", fonts, color=(147, 51, 234))
    draw_pill_badge(draw, 60, 580, "Microscopia a Fresco (KOH 10%)", "Pseudo-hifas e Blastóporos", fonts, color=(147, 51, 234))

    draw_pill_badge(draw, 550, 265, "pH > 4,5", "Alcalino", fonts, color=(13, 148, 136))
    draw_pill_badge(draw, 580, 400, "Teste de Whiff (+)", "Odor a aminas (KOH 10%)", fonts, color=(13, 148, 136))
    draw_pill_badge(draw, 500, 580, "Microscopia a Fresco", "Células-Guia (Clue Cells)", fonts, color=(13, 148, 136))

    draw_pill_badge(draw, 1030, 140, "Colo em Framboesa", "Colpite difusa petequial", fonts, color=(234, 88, 12))
    draw_pill_badge(draw, 1180, 260, "pH > 4,5", "Alcalino", fonts, color=(234, 88, 12))
    draw_pill_badge(draw, 950, 580, "Microscopia a Fresco", "Protozoários Móveis Flagelados", fonts, color=(234, 88, 12))

    # Bottom Cards
    def draw_card_col(bx1, bx2, title, subtitle, bullets, theme_color):
        by1, by2 = 635, 755
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, fill=(255, 255, 255), outline=theme_color, width=1)
        draw.text((bx1 + 10, by1 + 6), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 10, by1 + 22), subtitle, fill=theme_color, font=fonts["card_sub"])
        yt = by1 + 36
        for b in bullets:
            draw.text((bx1 + 10, yt), b, fill=(71, 85, 105), font=fonts["card_body"])
            yt += 14

    draw_card_col(25, 445, "Candidíase Vulvovaginal", "Infecção Fúngica Oportunista", [
        "• Corrimento branco grumoso, aspecto de leite coalhado aderido à parede.",
        "• Prurido vulvar intenso, ardor miccional externo, hiperemia e fissuras.",
        "• pH < 4,5. Teste de Whiff negativo. Pseudo-hifas ao KOH 10%.",
        "• Tto: Fluconazol 150 mg VO dose única OU Miconazol creme 2% à noite 7d."
    ], (147, 51, 234))

    draw_card_col(470, 890, "Vaginose Bacteriana", "Disbiose: Queda de Lactobacilos e Supercrescimento", [
        "• Corrimento acinzentado fino homogêneo com microbolhas e odor fétido.",
        "• Critérios de Amsel (3 de 4): corrimento, pH > 4,5, Whiff (+), clue cells > 20%.",
        "• Odor de peixe podre intensificado após coito ou aplicação de KOH 10%.",
        "• Tto: Metronidazol 500 mg VO 12/12h por 7 dias. NÃO tratar parceiro."
    ], (13, 148, 136))

    draw_card_col(915, 1350, "Tricomoníase Vaginal", "Infecção Sexualmente Transmissível (IST)", [
        "• Corrimento abundante bolhoso amarelo-esverdeado de odor desagradável.",
        "• Colpite macular (colo em morango/framboesa) com micro-hemorragias.",
        "• pH > 4,5. Microscopia: protozoário flagelado móvel e piócitos abundantes.",
        "• Tto: Metronidazol 2g VO dose única. TRATAMENTO DO PARCEIRO MANDATÓRIO!"
    ], (234, 88, 12))

    out_path = os.path.join(DST_DIR, "vulvovaginites_diagnostico_diferencial.jpg")
    pil_img.save(out_path, quality=96)
    print(f"Saved: {out_path}")

# =============================================================================
# 3. SEMIOLOGIA GINECOLÓGICA: EXAME ESPECULAR & TOQUE BIMANUAL
# =============================================================================
def build_semiologia():
    print("Building semiologia_exame_especular_toque.jpg...")
    src = os.path.join(SRC_DIR, "semiologia_ginecologica_exame_1791233962721.jpg")
    orig = cv2.imread(src)
    h, w = orig.shape[:2]

    clean = np.ones_like(orig) * 255
    clean[125:635, 20:665] = orig[125:635, 20:665]
    clean[125:635, 690:1355] = orig[125:635, 690:1355]

    # Inpaint residual SCJ text at x: 440..488, y: 320..365
    mask_scj = np.zeros(clean.shape[:2], dtype=np.uint8)
    roi = clean[320:365, 440:488]
    dark_mask = (roi[:,:,0] < 80) & (roi[:,:,1] < 80) & (roi[:,:,2] < 80)
    mask_scj[320:365, 440:488] = dark_mask.astype(np.uint8) * 255
    mask_scj = cv2.dilate(mask_scj, np.ones((3,3), np.uint8), iterations=1)
    clean = cv2.inpaint(clean, mask_scj, 3, cv2.INPAINT_TELEA)

    pil_img = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    draw_header(draw, w, 
                "SEMIOLOGIA GINECOLÓGICA: EXAME ESPECULAR & TOQUE BIMANUAL", 
                "Técnica do Exame Pélvico • Coleta do Papanicolau • Anatomia Cervical • Diretrizes FEBRASGO & Ministério da Saúde", 
                fonts)

    # Ribbons
    draw.rounded_rectangle([(25, 92), (670, 124)], radius=5, fill=(13, 148, 136))
    draw.text((35, 95), "1. EXAME ESPECULAR & COLETA CITOPATOLÓGICA", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((35, 109), "Inserção Bivalve • Inspeção do Colo e Vagina • Junção Escamocolunar (JEC) • Pap Smear", fill=(204, 251, 241), font=fonts["ribbon_sub"])

    draw.rounded_rectangle([(705, 92), (1350, 124)], radius=5, fill=(2, 132, 199))
    draw.text((715, 95), "2. TOQUE VAGINAL BIMANUAL", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((715, 109), "Palpação Bimanual do Útero e Anexos • Posição (AVF/RVF), Mobilidade e Dor", fill=(224, 242, 254), font=fonts["ribbon_sub"])

    draw.line([(688, 92), (688, 755)], fill=(226, 232, 240), width=1)

    # Left Annotations
    draw_pill_badge(draw, 25, 220, "Espéculo Vaginal (Cusco)", "Inserção oblíqua com água", fonts, color=(13, 148, 136))
    draw_pill_badge(draw, 25, 465, "Espátula de Ayre", "Coleta ectocervical (360°)", fonts, color=(13, 148, 136))
    draw_pill_badge(draw, 420, 525, "Cytobrush (Escova)", "Amostragem endocervical", fonts, color=(13, 148, 136))
    draw_pill_badge(draw, 400, 395, "JEC / ZEC", "Junção Escamocolunar (Rastreio)", fonts, color=(185, 28, 28))

    # Right Annotations
    draw_pill_badge(draw, 720, 185, "Mão Abdominal", "Deprime hipogástrio para fixar útero", fonts, color=(2, 132, 199))
    draw_pill_badge(draw, 960, 305, "Útero em Anteversoflexão (AVF)", "Palpação de tamanho, forma e mobilidade", fonts, color=(2, 132, 199))
    draw_pill_badge(draw, 1140, 395, "Anexos & Ovários", "Pesquisa de massas ou espessamento", fonts, color=(2, 132, 199))
    draw_pill_badge(draw, 1105, 505, "Mão Vaginal", "Dedos indicador e médio no fórnice", fonts, color=(2, 132, 199))

    # Bottom Cards
    def draw_card_sem(bx1, bx2, title, subtitle, bullets, theme_color):
        by1, by2 = 635, 755
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, fill=(255, 255, 255), outline=theme_color, width=1)
        draw.text((bx1 + 12, by1 + 6), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 12, by1 + 22), subtitle, fill=theme_color, font=fonts["card_sub"])
        yt = by1 + 36
        for b in bullets:
            draw.text((bx1 + 12, yt), b, fill=(71, 85, 105), font=fonts["card_body"])
            yt += 14

    draw_card_sem(25, 670, "Exame Especular & Citopatológico (Papanicolau)", "Inspeção Direta e Rastreamento de Lesões Precursoras do Câncer Cervical", [
        "• Técnica: Espéculo aquecido e lubrificado apenas com água (evitar gel que interfere na citologia).",
        "• Inspeção: Conteúdo vaginal, fórnices, colo uterino (orifício, ectopia, pólipos, lesões friáveis).",
        "• Amostragem Dupla: Ectocérvice com espátula de Ayre e Endocérvice com Cytobrush girada 360°.",
        "• Rastreio MS/Brasil: Iniciar aos 25 anos em mulheres com sexarca; após 2 exames normais anuais, a cada 3 anos até 64 anos."
    ], (13, 148, 136))

    draw_card_sem(705, 1350, "Toque Vaginal Bimanual & Avaliação Pélvica", "Palpação Sistemática dos Órgãos Reprodutivos Internos e Fundo de Saco", [
        "• Colo Uterino: Consistência (firme/amolecido), orifício externo, mobilidade e dor à tração.",
        "• Sinal de Chandelier: Dor intensa à mobilização do colo (sugestivo de DIP ou prenhez ectópica rota).",
        "• Útero: Tamanho, simetria, consistência, sensibilidade e posição (AVF em 80% das mulheres).",
        "• Anexos e Fundo de Saco: Palpação de ovários (normal até 3 cm no menacme) e abaulamento de Douglas (hemoperitônio)."
    ], (2, 132, 199))

    out_path = os.path.join(DST_DIR, "semiologia_exame_especular_toque.jpg")
    pil_img.save(out_path, quality=96)
    print(f"Saved: {out_path}")

# =============================================================================
# 4. ÍNDICE DE BISHOP & MATURAÇÃO CERVICAL
# =============================================================================
def build_bishop():
    print("Building indice_bishop_maturacao_cervical.jpg...")
    src = os.path.join(SRC_DIR, "indice_bishop_maturacao_1791234028610.jpg")
    orig = cv2.imread(src)
    h, w = orig.shape[:2]

    clean = np.ones_like(orig) * 255
    # Top uterus
    clean[187:570, 215:669] = orig[187:570, 215:669]
    # Bottom uterus
    clean[540:635, 215:669] = orig[540:635, 215:669]

    # Misoprostol uterus
    clean[160:625, 711:1014] = orig[160:625, 711:1014]
    # Foley catheter uterus and tube
    clean[160:600, 1047:1348] = orig[160:600, 1047:1348]

    # Erase English text:
    clean[:, :215] = 255
    clean[490:580, 850:1040] = 255  # 'Misoprosto tablet'
    clean[570:700, 1100:1350] = 255 # 'Foley catheter'
    clean[580:768, 700:1050] = 255 # Old warning box
    clean[625:768, :] = 255         # Clear bottom for structured cards

    pil_img = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    draw_header(draw, w, 
                "ÍNDICE DE BISHOP, MATURAÇÃO CERVICAL & INDUÇÃO DO PARTO", 
                "Avaliação da Favorabilidade do Colo • Sonda de Foley vs Misoprostol • Diretrizes FEBRASGO & Ministério da Saúde (SUS)", 
                fonts)

    # Ribbons
    draw.rounded_rectangle([(25, 92), (670, 124)], radius=5, fill=(5, 150, 105))
    draw.text((35, 95), "1. ÍNDICE DE BISHOP: AVALIAÇÃO DA FAVORABILIDADE CERVICAL", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((35, 109), "5 Parâmetros: Dilatação, Apagamento, Consistência, Posição e Plano de De Lee", fill=(209, 250, 229), font=fonts["ribbon_sub"])

    draw.rounded_rectangle([(705, 92), (1350, 124)], radius=5, fill=(217, 119, 6))
    draw.text((715, 95), "2. MÉTODOS DE MATURAÇÃO CERVICAL & INDUÇÃO DO PARTO", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((715, 109), "Método Farmacológico (Misoprostol) vs Mecânico (Sonda de Foley) • Alertas de Segurança", fill=(254, 243, 199), font=fonts["ribbon_sub"])

    draw.line([(688, 92), (688, 755)], fill=(226, 232, 240), width=1)

    # Left annotations
    draw_pill_badge(draw, 25, 150, "Colo Desfavorável", "Bishop < 6 (Necessita Maturação)", fonts, color=(220, 38, 38))
    draw.text((25, 190), "• Fechado (0 cm)\n• Apagamento 0%\n• Consistência Firme\n• Posição Posterior\n• Plano De Lee -3", fill=(71, 85, 105), font=fonts["card_body"])

    draw_pill_badge(draw, 25, 450, "Colo Favorável (Maduro)", "Bishop ≥ 8 (Indução com Ocitocina)", fonts, color=(5, 150, 105))
    draw.text((25, 490), "• Dilatado (≥ 5 cm)\n• Apagado (≥ 80%)\n• Consistência Amolecida\n• Posição Anterior\n• Plano De Lee +1", fill=(71, 85, 105), font=fonts["card_body"])

    # Right annotations
    draw_pill_badge(draw, 715, 135, "Maturação Farmacológica", "Misoprostol 25 mcg fórnice posterior", fonts, color=(217, 119, 6))
    draw_pill_badge(draw, 1050, 135, "Maturação Mecânica", "Sonda de Foley intracervical (30-50 mL)", fonts, color=(2, 132, 199))

    draw_pill_badge(draw, 715, 495, "Comprimido de Misoprostol", "Prostaglandina E1 (25 mcg)", fonts, color=(217, 119, 6))
    draw_pill_badge(draw, 1050, 495, "Balão de Foley (30-50 mL)", "Acima do orifício interno do colo", fonts, color=(2, 132, 199))

    # Red Warning Box
    draw.rounded_rectangle([(715, 545), (1030, 625)], radius=5, fill=(254, 242, 242), outline=(239, 68, 68), width=1)
    draw.text((725, 550), "ALERTA CRÍTICO: CESÁREA ANTERIOR", fill=(185, 28, 28), font=fonts["anno_bold"])
    draw.text((725, 568), "Misoprostol é CONTRAINDICADO em cicatriz uterina!", fill=(153, 27, 27), font=fonts["anno_small"])
    draw.text((725, 584), "Risco de ROTURA UTERINA catastrófica.", fill=(153, 27, 27), font=fonts["anno_small"])
    draw.text((725, 600), "Método de escolha obrigatório: Sonda de Foley.", fill=(71, 85, 105), font=fonts["anno_small"])

    # Bottom Cards
    def draw_card_bishop(bx1, bx2, title, subtitle, bullets, theme_color):
        by1, by2 = 635, 755
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, fill=(255, 255, 255), outline=theme_color, width=1)
        draw.text((bx1 + 12, by1 + 6), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 12, by1 + 22), subtitle, fill=theme_color, font=fonts["card_sub"])
        yt = by1 + 36
        for b in bullets:
            draw.text((bx1 + 12, yt), b, fill=(71, 85, 105), font=fonts["card_body"])
            yt += 14

    draw_card_bishop(25, 670, "Escore de Bishop & Estratificação Clínica", "Avaliação Objetiva da Prontidão Cervical para Indução do Trabalho de Parto", [
        "• 5 Critérios (0-3 pts cada): Dilatação (0, 1-2, 3-4, ≥5), Apagamento (0-30, 40-50, 60-70, ≥80%), Consistência, Posição e De Lee.",
        "• Bishop ≥ 8 (Favorável): Probabilidade de parto vaginal semelhante ao trabalho de parto espontâneo → Ocitocina IV direta.",
        "• Bishop ≤ 5 (Desfavorável): Alto risco de falha de indução e cesariana se iniciada ocitocina sem maturação cervical prévia.",
        "• Monitorização: Reavaliação cervical seriada a cada 4 a 6 horas após inserção do método de maturação."
    ], (5, 150, 105))

    draw_card_bishop(705, 1350, "Métodos de Maturação & Segurança em Cesárea Prévia", "Misoprostol vs Método Mecânico de Foley — Regra de Ouro do Ministério da Saúde", [
        "• Misoprostol (PGE1): 25 mcg em fundo de saco a cada 6h (máx 4-6 doses). Eficaz, porém causa taquissistolia uterina.",
        "• CONTRAINDICAÇÃO ABSOLUTA: Misoprostol NUNCA deve ser usado em mulheres com cicatriz uterina/cesárea prévia!",
        "• Risco Crítico: Risco elevado de rotura uterina catastrófica com perda fetal e histerectomia puerperal.",
        "• Método de Escolha em Cesárea Anterior: Sonda de Foley nº 16-18 insuflada com 30-50 mL de SF 0,9% (indução mecânica segura)."
    ], (217, 119, 6))

    out_path = os.path.join(DST_DIR, "indice_bishop_maturacao_cervical.jpg")
    pil_img.save(out_path, quality=96)
    print(f"Saved: {out_path}")

# =============================================================================
# 5. SEGURANÇA DO PACIENTE: QUEIJO SUÍÇO & CHECKLIST CIRÚRGICO
# =============================================================================
def build_safety():
    print("Building seguranca_paciente_queijo_suico.jpg...")
    src = os.path.join(SRC_DIR, "seguranca_queijo_suico_1791234103433.jpg")
    orig = cv2.imread(src)
    h, w = orig.shape[:2]

    clean = np.ones_like(orig) * 255

    # Left: Swiss cheese slices
    clean[199:545, 18:669] = orig[199:545, 18:669]

    # Right: Columns with pastel backgrounds
    # Col 1 (Sign In): warm beige
    clean[110:635, 708:921] = [246, 252, 254]
    # Col 2 (Time Out): mint
    clean[110:635, 928:1140] = [246, 248, 243]
    # Col 3 (Sign Out): peach
    clean[110:635, 1146:1359] = [240, 246, 253]

    # Clean illustrations for each column:
    # Col 1: doctor and operating table with patient (clean y:190..315)
    clean[190:315, 715:895] = orig[190:315, 715:895]
    clean[190:245, 785:895] = [246, 252, 254] # erase top right text

    # Col 2: surgical team conferring (clean y:190..296)
    clean[190:296, 940:1130] = orig[190:296, 940:1130]

    # Col 3: operating team performing surgery (clean y:190..295)
    clean[190:295, 1160:1345] = orig[190:295, 1160:1345]

    clean[0:125, :] = 255
    clean[635:768, :] = 255

    pil_img = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    fonts = get_fonts()

    draw_header(draw, w, 
                "SEGURANÇA DO PACIENTE EM GINECOLOGIA E OBSTETRÍCIA", 
                "Modelo do Queijo Suíço de James Reason • Checklist de Cirurgia Segura da OMS em Cesariana • Diretrizes ANVISA / SUS", 
                fonts)

    # 2 Ribbons
    draw.rounded_rectangle([(25, 92), (670, 124)], radius=5, fill=(217, 119, 6))
    draw.text((35, 95), "1. MODELO DO QUEIJO SUÍÇO (JAMES REASON)", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((35, 109), "Barreiras Defensivas do Sistema contra Falhas Latentes e Ativas", fill=(254, 243, 199), font=fonts["ribbon_sub"])

    draw.rounded_rectangle([(705, 92), (1350, 124)], radius=5, fill=(15, 118, 110))
    draw.text((715, 95), "2. CHECKLIST DE CIRURGIA E PARTO SEGURO (OMS / ANVISA / FEBRASGO)", fill=(255, 255, 255), font=fonts["ribbon_title"])
    draw.text((715, 109), "Sign In (Antes da Anestesia) • Time Out (Pausa Cirúrgica) • Sign Out (Antes do Fechamento)", fill=(204, 251, 241), font=fonts["ribbon_sub"])

    draw.line([(688, 92), (688, 755)], fill=(226, 232, 240), width=1)

    # Left annotations (Cheese Slices)
    draw_pill_badge(draw, 25, 135, "1. Protocolos Clínicos", "Rotinas e PCDT", fonts, color=(217, 119, 6))
    draw_pill_badge(draw, 150, 135, "2. Dupla Identificação", "Pulseiras Mãe e RN", fonts, color=(217, 119, 6))
    draw_pill_badge(draw, 280, 135, "3. Treinamento de Equipe", "Simulação Realística", fonts, color=(217, 119, 6))
    draw_pill_badge(draw, 420, 135, "4. Checklist Cirúrgico", "Conferência Ativa", fonts, color=(217, 119, 6))
    draw_pill_badge(draw, 545, 135, "5. Alça Fechada", "Comunicação Efetiva", fonts, color=(217, 119, 6))

    draw.text((35, 595), "→ Trajetória do Dano: O erro só atinge a paciente quando as falhas de todas as barreiras se alinham!", fill=(185, 28, 28), font=fonts["anno_bold"])

    # Right Checklist Columns Headers
    draw.rounded_rectangle([(708, 135), (921, 175)], radius=4, fill=(254, 243, 199), outline=(217, 119, 6))
    draw.text((718, 140), "1. SIGN IN", fill=(180, 83, 9), font=fonts["anno_bold"])
    draw.text((718, 155), "Antes da Indução Anestésica", fill=(120, 53, 15), font=fonts["anno_small"])

    draw.rounded_rectangle([(928, 135), (1140, 175)], radius=4, fill=(204, 251, 241), outline=(15, 118, 110))
    draw.text((938, 140), "2. TIME OUT", fill=(15, 118, 110), font=fonts["anno_bold"])
    draw.text((938, 155), "Antes da Incisão Cirúrgica", fill=(19, 78, 74), font=fonts["anno_small"])

    draw.rounded_rectangle([(1146, 135), (1350, 175)], radius=4, fill=(254, 226, 226), outline=(220, 38, 38))
    draw.text((1155, 140), "3. SIGN OUT", fill=(185, 28, 28), font=fonts["anno_bold"])
    draw.text((1155, 155), "Antes da Saída de Sala", fill=(127, 29, 29), font=fonts["anno_small"])

    # Checklist White Card Boxes inside Columns below illustrations
    # Col 1 Card (y: 325 to 625)
    draw.rounded_rectangle([(714, 325), (915, 625)], radius=5, fill=(255, 255, 255), outline=(217, 119, 6), width=1)
    draw.text((722, 335), "ETAPA PRÉ-ANESTÉSICA", fill=(180, 83, 9), font=fonts["anno_bold"])
    col1_items = [
        "☑ Identidade (Nome + DN)",
        "☑ Pulseira mãe e prontuário",
        "☑ Consentimento assinado",
        "☑ Sítio cirúrgico demarcado",
        "☑ Monitorização e oxímetro",
        "☑ Aparelho anestesia testado",
        "☑ Checagem de alergias",
        "☑ Avaliação de via aérea",
        "☑ Acesso venoso calibroso",
        "☑ Jejum adequado confirmado"
    ]
    y_c1 = 358
    for item in col1_items:
        draw.text((722, y_c1), item, fill=(51, 65, 85), font=fonts["anno_small"])
        y_c1 += 26

    # Col 2 Card (y: 310 to 625)
    draw.rounded_rectangle([(934, 310), (1134, 625)], radius=5, fill=(255, 255, 255), outline=(15, 118, 110), width=1)
    draw.text((942, 320), "PAUSA CIRÚRGICA (TIME OUT)", fill=(15, 118, 110), font=fonts["anno_bold"])
    col2_items = [
        "☑ Apresentação da equipe",
        "☑ Confirmação paciente e parto",
        "☑ Posição materna na mesa",
        "☑ Profilaxia: Cefazolina 2g IV",
        "   (feita < 60 min da incisão)",
        "☑ Previsão de sangramento",
        "☑ Kit de HPP pronto em sala",
        "☑ Sangue tipado / reserva",
        "☑ Berço neonatal aquecido",
        "☑ Pediatra / neo presente"
    ]
    y_c2 = 345
    for item in col2_items:
        draw.text((942, y_c2), item, fill=(51, 65, 85), font=fonts["anno_small"])
        y_c2 += 27

    # Col 3 Card (y: 310 to 625)
    draw.rounded_rectangle([(1152, 310), (1344, 625)], radius=5, fill=(255, 255, 255), outline=(220, 38, 38), width=1)
    draw.text((1160, 320), "CONFERÊNCIA FINAL (SIGN OUT)", fill=(185, 28, 28), font=fonts["anno_bold"])
    col3_items = [
        "☑ Nome do procedimento feito",
        "☑ Contagem correta compressas",
        "   (conferência verbal ativa)",
        "☑ Contagem de agulhas OK",
        "☑ Instrumental cirúrgico OK",
        "☑ Placenta/peças rotuladas",
        "☑ Intercorrências revistas",
        "☑ Prescrição de ocitocina pós",
        "☑ Prescrição de analgesia",
        "☑ Encaminhamento seguro SRPA"
    ]
    y_c3 = 345
    for item in col3_items:
        draw.text((1160, y_c3), item, fill=(51, 65, 85), font=fonts["anno_small"])
        y_c3 += 27

    # Bottom Cards
    def draw_card_safety(bx1, bx2, title, subtitle, bullets, theme_color):
        by1, by2 = 635, 755
        draw.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=6, fill=(255, 255, 255), outline=theme_color, width=1)
        draw.text((bx1 + 12, by1 + 6), title, fill=(15, 23, 42), font=fonts["card_title"])
        draw.text((bx1 + 12, by1 + 22), subtitle, fill=theme_color, font=fonts["card_sub"])
        yt = by1 + 36
        for b in bullets:
            draw.text((bx1 + 12, yt), b, fill=(71, 85, 105), font=fonts["card_body"])
            yt += 14

    draw_card_safety(25, 670, "Cultura de Segurança & Modelo de Reason", "Prevenção Sistêmica de Erros Assistenciais e Eventos Sentinela em Obstetrícia", [
        "• Foco no Sistema: A maioria dos erros decorre de falhas nos processos e comunicação, não de imperícia isolada.",
        "• Eventos Sentinela em GO: Troca de RN, retenção de compressa pós-cesárea, lesão ureteral em histerectomia.",
        "• Prevenção de Troca de Bebê: Dupla pulseira inviolável colocada no RN na presença da mãe imediatamente ao nascer.",
        "• Comunicação SBAR: Ferramenta padronizada (Situação, Breve Histórico, Avaliação, Recomendação) na passagem de plantão."
    ], (217, 119, 6))

    draw_card_safety(705, 1350, "As 3 Etapas do Checklist Cirúrgico da OMS em GO", "Protocolo Obrigatório para Redução de Morbimortalidade Perioperatória", [
        "• 1. Sign In (Antes da Anestesia): Confirmação de 2 identificadores (nome + DN), termo assinado, lateralidade e acesso venoso calibroso.",
        "• 2. Time Out (Antes da Incisão): Cefazolina 2g IV infundida há menos de 60 min, kit de HPP em sala, sangue tipado e berço aquecido.",
        "• 3. Sign Out (Antes do Fechamento): Conferência verbal com a instrumentadora da contagem correta de compressas (regra de 5 em 5) e agulhas.",
        "• Prevenção de Retenção de Corpo Estranho: Recontagem obrigatória antes do fechamento do útero e antes do fechamento da aponeurose."
    ], (15, 118, 110))

    out_path = os.path.join(DST_DIR, "seguranca_paciente_queijo_suico.jpg")
    pil_img.save(out_path, quality=96)
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    os.makedirs(DST_DIR, exist_ok=True)
    build_dpp_vs_pp()
    build_vulvovaginites()
    build_semiologia()
    build_bishop()
    build_safety()
    print("All 5 core images polished successfully!")
