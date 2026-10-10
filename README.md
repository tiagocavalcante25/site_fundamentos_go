# Portal Fundamentos em Ginecologia e Obstetrícia 🩺
### Treinamento Clínico Interativo para Internato, Residência Médica, FEBRASGO & USMLE Step 2 CK

Plataforma estática, moderna e responsiva construída em conformidade com as diretrizes do **Ministério da Saúde do Brasil (PCDT / SUS)**, **FEBRASGO**, **ACOG** e **USMLE Step 2 CK**.

---

## 🚀 Como Fazer o Deploy no GitHub Pages

Este repositório foi otimizado para deploy imediato no **GitHub Pages** como site estático, sem necessidade de build (`npm build`) ou servidores adicionais:

### Passo a Passo:

1. **Inicializar o Repositório Git (se ainda não o fez):**
   ```bash
   cd "c:\Users\Admin\Downloads\INTERNATO GO\site_fundamentos_go"
   git init
   git add .
   git commit -m "feat: Portal Fundamentos em GO otimizado para GitHub Pages"
   ```

2. **Criar um repositório no GitHub e conectar:**
   ```bash
   git branch -M main
   git remote add origin https://github.com/<SEU_USUARIO>/<NOME_DO_REPOSITORIO>.git
   git push -u origin main
   ```

3. **Ativar o GitHub Pages no Repositório:**
   - Acesse o repositório no GitHub: `https://github.com/<SEU_USUARIO>/<NOME_DO_REPOSITORIO>`
   - Vá na aba **Settings** (Configurações)
   - Na barra lateral esquerda, clique em **Pages**
   - Na seção **Build and deployment**:
     - **Source**: Selecione `Deploy from a branch`
     - **Branch**: Selecione `main` e a pasta `/(root)`
     - Clique em **Save** (Salvar)
   - Em 1 a 2 minutos, seu site estará no ar na URL:  
     `https://<SEU_USUARIO>.github.io/<NOME_DO_REPOSITORIO>/`

> **Nota Técnica:** O arquivo `.nojekyll` já está incluído na raiz do projeto para instruir o GitHub Pages a publicar todos os arquivos e diretórios estáticos diretamente, sem passar pela engine Jekyll.

---

## 📱 Otimizações para Celulares (iOS / Android) e Tablets

- **Fonte Ampliada e Confortável:** Tipografia base reescalada (`16.5px` no mobile, `17px` em tablets e `17.5px` no desktop), com classes utilitárias de texto pequeno ajustadas para evitar fadiga visual durante plantões.
- **Controle Dinâmico de Fonte (A / A+ / A++):** Seletor rápido na barra superior e no menu gaveta mobile para alternar entre tamanho *Padrão*, *Grande (+15%)* e *Máximo (+30%)*, com persistência em `localStorage`.
- **Prevenção de Auto-Zoom no iOS Safari:** Inputs, selects e áreas de formulário calibrados com `font-size: 16px` em dispositivos móveis, impedindo saltos indesejados de zoom na tela ao focar campos.
- **Suporte a Safe Area Insets (iPhone & Android):** Ajuste automático para notch, Dynamic Island e barras de gestos (`env(safe-area-inset-top)` e `env(safe-area-inset-bottom)`).
- **Tabelas Médicas Deslizáveis:** Tabelas densas protegidas com largura mínima e indicadores visuais de deslizamento lateral, preservando a leitura comparativa (ex: Bethesda e DPP vs Placenta Prévia).
- **Botão Flutuante Voltar ao Topo (FAB):** Botão ergonômico no canto inferior direito que surge suavemente ao rolar a página, respeitando a margem inferior do aparelho.

---

## 📚 Conteúdo Clínico Integrado (100% dos Módulos 21 ao 28)

1. **Módulo 21: Semiologia Gineco-Obstétrica**
   - Anamnese estruturada (ID, QP, HMA, Antecedentes, Mnemônico BLOOD CLAMP).
   - Exame Especular e Toque Vaginal Bimanual (com infográfico HD e zoom interativo).
   - Rastreio de Câncer de Colo Uterino e Classificação de Bethesda completa.
   - Calculadora Interativa do **Índice de Bishop** com conduta clínica automatizada.

2. **Módulo 22: Raciocínio Clínico em GO**
   - Diagnósticos diferenciais de emergência da 2ª metade da gestação (DPP vs Placenta Prévia).
   - Tabela comparativa e critérios de Couvelaire / acretismo.
   - Vulvovaginites e vaginoses (Candidíase, Vaginose Bacteriana com critérios de Amsel, Tricomoníase).

3. **Módulo 23: Medicina Baseada em Evidências (MBE)**
   - Calculadora 2x2 de Testes Diagnósticos (Sensibilidade, Especificidade, VPP, VPN, RVP+, RVP- e Acurácia).
   - Aplicação em pré-eclâmpsia e rastreios obstétricos.

4. **Módulo 24: Segurança do Paciente & Erro Médico**
   - Modelo do Queijo Suíço de James Reason.
   - Checklist Cirúrgico Interativo da OMS (Sign-In, Time-Out, Sign-Out) com barra de progresso em tempo real.

5. **Módulo 25: Comunicação Clínica & Habilidades Interpessoais**
   - Protocolo SPIKES para comunicação de más notícias (óbitos fetais, anomalias, malignidades).
   - Gerador Interativo de Passagem de Plantão no protocolo **SBAR** (Situação, Background, Avaliação, Recomendação) com botão de cópia rápida.

6. **Módulo 26: Bioética Médica & Aspectos Legais**
   - Quatro princípios bioéticos fundamentais (Autonomia, Beneficência, Não-maleficência, Justiça).
   - Sigilo profissional médico vs Excludentes de quebra (dever legal, justa causa, consentimento).
   - Abortamento Legal no Brasil (estupro, risco de vida materna, anencefalia fetal).

7. **Módulo 27: Direitos Sexuais, Reprodutivos & Violência Sexual**
   - Protocolo de Profilaxia Pós-Exposição (PEP de HIV, Hepatite B, anticoncepção de emergência).
   - Calculadora de conduta pós-violência sexual conforme tempo decorrido (<72h, 72-120h, >120h).
   - Anticoncepção reversível de longa duração (LARCs: DIU de Cobre, DIU de Levonorgestrel, Implante Subdérmico).

8. **Módulo 28: Cuidados Paliativos em Ginecologia e Obstetrícia**
   - Princípios da ortotanásia, diretivas antecipadas de vontade e luto perinatal.
   - Escada Analgésica Interativa da OMS com slider EVA (0 a 10) e prescrições completas com laxativos profiláticos e resgates.

9. **Hubs de Treinamento e Fixação:**
   - **Top 20 High-Yield:** Pérolas clínicas e pegadinhas clássicas de prova.
   - **Flashcards Interativos:** Modo 3D com virada tátil, filtros por tema e embaralhamento.
   - **Simulado de Casos Clínicos:** Questões comentadas no padrão USMLE Step 2 / Enare / FEBRASGO.

---

## 🛠️ Tecnologias Utilizadas

- **HTML5 Semântico**
- **Tailwind CSS (via CDN)**
- **CSS Customizado (`assets/css/custom.css`)**
- **JavaScript Vanilla Modular (`assets/js/app.js`)**
- **Lucide Icons**
- **Imagens Clínicas em Alta Definição com Lightbox HD e Zoom**
