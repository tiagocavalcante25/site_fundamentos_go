/**
 * app.js - Lógica Interativa do Portal Fundamentos em Ginecologia & Obstetrícia
 * Baseado no Guia Obstetrícia e Ginecologia Parte 3 (USMLE Step 2 CK / FEBRASGO / SUS)
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initFontSize();
  initFabBackToTop();
  initReadingProgressBar();
  initMobileNav();
  initSearch();
  initBishopCalculator();
  initMBECalculator();
  initSafeSurgeryChecklist();
  initSBARGenerator();
  initPainLadder();
  initSexualViolenceProtocol();
  initFlashcards();
  initQuiz();
  initLightbox();
});

/* ==========================================================================
   1. GERENCIAMENTO DE TEMA (DARK / LIGHT)
   ========================================================================== */
function initTheme() {
  const themeToggles = document.querySelectorAll('.theme-toggle-btn, #theme-toggle, #mobile-theme-toggle');
  const html = document.documentElement;

  // Garantir sincronia de acessibilidade e títulos
  function updateThemeUI() {
    const isDark = html.classList.contains('dark');
    themeToggles.forEach(btn => {
      btn.setAttribute('aria-label', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
      btn.setAttribute('title', isDark ? 'Ativar modo claro' : 'Ativar modo escuro');
    });
  }

  function toggleTheme() {
    const isDark = html.classList.contains('dark');
    if (isDark) {
      html.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    } else {
      html.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    }
    updateThemeUI();
  }

  themeToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleTheme();
    });
  });

  updateThemeUI();
}

/* ==========================================================================
   1.2 CONTROLE DINÂMICO DE TAMANHO DE FONTE (A- / A / A+)
   ========================================================================== */
function initFontSize() {
  const html = document.documentElement;
  const savedSize = localStorage.getItem('fontSizePreference') || 'normal';
  setFontSize(savedSize);

  const fontButtons = document.querySelectorAll('[data-font-size-set]');
  fontButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetSize = btn.getAttribute('data-font-size-set');
      setFontSize(targetSize);
      localStorage.setItem('fontSizePreference', targetSize);
    });
  });

  function setFontSize(size) {
    if (['normal', 'large', 'xlarge'].includes(size)) {
      html.setAttribute('data-font-size', size);
    } else {
      html.setAttribute('data-font-size', 'normal');
    }
    // Atualiza estado ativo dos botões
    document.querySelectorAll('[data-font-size-set]').forEach(btn => {
      const btnSize = btn.getAttribute('data-font-size-set');
      if (btnSize === size) {
        btn.classList.add('bg-sky-600', 'text-white', 'shadow-sm', 'active');
        btn.classList.remove('text-slate-600', 'dark:text-slate-400', 'hover:bg-slate-200', 'dark:hover:bg-slate-800');
      } else {
        btn.classList.remove('bg-sky-600', 'text-white', 'shadow-sm', 'active');
        btn.classList.add('text-slate-600', 'dark:text-slate-400');
      }
    });
  }
}

/* ==========================================================================
   1.3 BOTÃO FLUTUANTE VOLTAR AO TOPO (FAB)
   ========================================================================== */
function initFabBackToTop() {
  const fab = document.getElementById('fab-back-to-top');
  if (!fab) return;

  function toggleFab() {
    if (window.scrollY > 350) {
      fab.classList.remove('fab-hidden');
      fab.classList.add('fab-visible');
    } else {
      fab.classList.remove('fab-visible');
      fab.classList.add('fab-hidden');
    }
  }

  window.addEventListener('scroll', toggleFab, { passive: true });
  fab.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  toggleFab();
}

/* ==========================================================================
   1.3.1 BARRA DE PROGRESSO DE LEITURA
   ========================================================================== */
function initReadingProgressBar() {
  const bar = document.getElementById('reading-progress');
  if (!bar) return;

  function updateProgress() {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (totalHeight > 0) {
      const progress = (window.scrollY / totalHeight) * 100;
      bar.style.width = Math.min(100, Math.max(0, progress)) + '%';
    }
  }

  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress, { passive: true });
  updateProgress();
}

/* ==========================================================================
   1.4 NAVEGAÇÃO SUPERIOR FIXA (ACESSO DIRETO AOS MÓDULOS SEM GAVETA REDUNDANTE)
   ========================================================================== */
function initMobileNav() {
  // A navegação foi unificada na barra superior fixa de 2 níveis (position: fixed).
  // Todos os módulos e calculadoras têm acesso direto por toque sem drawer lateral.
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-menu-drawer');
  if (!toggleBtn || !drawer) return;
}

/* ==========================================================================
   2. SISTEMA DE BUSCA E FILTRO RÁPIDO
   ========================================================================== */
function initSearch() {
  const searchInputs = [
    document.getElementById('global-search'),
    document.getElementById('mobile-search')
  ].filter(Boolean);

  if (searchInputs.length === 0) return;

  function handleSearch(query) {
    const q = query.toLowerCase().trim();
    const modules = document.querySelectorAll('.module-card');
    
    // Sincronizar inputs
    searchInputs.forEach(input => {
      if (input.value !== query) input.value = query;
    });

    modules.forEach((mod) => {
      const text = mod.textContent.toLowerCase();
      if (!q || text.includes(q)) {
        mod.style.display = '';
      } else {
        mod.style.display = 'none';
      }
    });
  }

  searchInputs.forEach(input => {
    input.addEventListener('input', (e) => handleSearch(e.target.value));
  });

  // Atalho de teclado Ctrl+K ou Cmd+K
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      const primary = document.getElementById('global-search') || searchInputs[0];
      if (primary) {
        primary.focus();
        primary.select();
      }
    }
  });
}

/* ==========================================================================
   3. CALCULADORA DO ÍNDICE DE BISHOP & CONDUTA
   ========================================================================== */
function initBishopCalculator() {
  const form = document.getElementById('bishop-form');
  if (!form) return;

  const selects = form.querySelectorAll('select');
  const scarCheck = document.getElementById('bishop-cesarean-scar');
  const scoreBadge = document.getElementById('bishop-score');
  const statusBadge = document.getElementById('bishop-status');
  const actionText = document.getElementById('bishop-action');
  const warningBox = document.getElementById('bishop-warning-box');

  function calculateBishop() {
    let score = 0;
    selects.forEach(sel => {
      score += parseInt(sel.value, 10);
    });

    const hasScar = scarCheck ? scarCheck.checked : false;
    scoreBadge.textContent = score;

    if (score >= 8) {
      statusBadge.textContent = "Colo Maduro / Favorável";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-300";
      actionText.innerHTML = `
        <strong class="text-emerald-700 dark:text-emerald-400">Conduta: Indução Direta com Ocitocina IV.</strong><br>
        A probabilidade de sucesso de parto vaginal é similar à do trabalho de parto espontâneo. Iniciar ocitocina 5 UI em 500 mL de SG 5% ou RL em bomba de infusão contínua com titulação escalonada a cada 30 minutos.
      `;
      if (warningBox) warningBox.classList.add('hidden');
    } else if (score >= 6) {
      statusBadge.textContent = "Colo Intermediário";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-amber-100 text-amber-800 dark:bg-amber-900/60 dark:text-amber-300";
      actionText.innerHTML = `
        <strong class="text-amber-700 dark:text-amber-400">Conduta: Avaliação Individualizada.</strong><br>
        Pode-se proceder à maturação cervical ou iniciar teste com ocitocina dependendo da paridade. Em multíparas, ocitocina pode ser suficiente. Em nulíparas, maturação prévia otimiza desfecho.
      `;
      if (warningBox) warningBox.classList.add('hidden');
    } else {
      statusBadge.textContent = "Colo Imaturo / Desfavorável (Bishop < 6)";
      statusBadge.className = "px-3 py-1 text-xs font-bold rounded-full bg-rose-100 text-rose-800 dark:bg-rose-900/60 dark:text-rose-300";
      
      if (hasScar) {
        actionText.innerHTML = `
          <strong class="text-rose-700 dark:text-rose-400">Conduta Obrigatória: Maturação Mecânica com Sonda de Foley.</strong><br>
          <span class="text-rose-600 dark:text-rose-400 font-semibold">⚠️ CONTRAINDICAÇÃO ABSOLUTA: Misoprostol é formalmente proibido em cicatriz uterina prévia pelo risco de rotura uterina catastrófica!</span><br>
          Passar cateter de Foley n° 16-18 transcervical acima do orifício interno, insuflar balão com 30 a 50 mL de SF 0,9% estéril e tracionar levemente.
        `;
        if (warningBox) warningBox.classList.remove('hidden');
      } else {
        actionText.innerHTML = `
          <strong class="text-indigo-700 dark:text-indigo-400">Conduta: Maturação Farmacológica com Misoprostol (PGE1).</strong><br>
          Prescrever Misoprostol 25 mcg em fundo de saco vaginal posterior a cada 6 horas (máximo 4 a 6 doses). Monitorar tônus uterino e BCF. Se contrações regulares (> 3 em 10 min), suspender e aguardar evolução. Ocitocina só pode ser iniciada 4 a 6 horas após a última dose de misoprostol!
        `;
        if (warningBox) warningBox.classList.add('hidden');
      }
    }
  }

  selects.forEach(sel => sel.addEventListener('change', calculateBishop));
  if (scarCheck) scarCheck.addEventListener('change', calculateBishop);
  calculateBishop();
}

/* ==========================================================================
   4. CALCULADORA DE MEDICINA BASEADA EM EVIDÊNCIAS (MBE)
   ========================================================================== */
function initMBECalculator() {
  const form = document.getElementById('mbe-form');
  if (!form) return;

  const vpInput = document.getElementById('mbe-vp');
  const fpInput = document.getElementById('mbe-fp');
  const fnInput = document.getElementById('mbe-fn');
  const vnInput = document.getElementById('mbe-vn');

  const sensOut = document.getElementById('mbe-sens');
  const especOut = document.getElementById('mbe-espec');
  const vppOut = document.getElementById('mbe-vpp');
  const vpnOut = document.getElementById('mbe-vpn');
  const lrPosOut = document.getElementById('mbe-lrpos');
  const lrNegOut = document.getElementById('mbe-lrneg');
  const acuraciaOut = document.getElementById('mbe-acuracia');

  function calculateMBE() {
    const vp = parseFloat(vpInput.value) || 0;
    const fp = parseFloat(fpInput.value) || 0;
    const fn = parseFloat(fnInput.value) || 0;
    const vn = parseFloat(vnInput.value) || 0;

    const totalDoentes = vp + fn;
    const totalSadios = fp + vn;
    const totalPositivos = vp + fp;
    const totalNegativos = fn + vn;
    const totalGeral = vp + fp + fn + vn;

    if (totalDoentes === 0 || totalSadios === 0) return;

    const sens = (vp / totalDoentes) * 100;
    const espec = (vn / totalSadios) * 100;
    const vpp = totalPositivos > 0 ? (vp / totalPositivos) * 100 : 0;
    const vpn = totalNegativos > 0 ? (vn / totalNegativos) * 100 : 0;
    const acuracia = totalGeral > 0 ? ((vp + vn) / totalGeral) * 100 : 0;

    const lrPos = (100 - espec) > 0 ? (sens / (100 - espec)) : 0;
    const lrNeg = espec > 0 ? ((100 - sens) / espec) : 0;

    sensOut.textContent = sens.toFixed(1) + '%';
    especOut.textContent = espec.toFixed(1) + '%';
    vppOut.textContent = vpp.toFixed(1) + '%';
    vpnOut.textContent = vpn.toFixed(1) + '%';
    acuraciaOut.textContent = acuracia.toFixed(1) + '%';
    lrPosOut.textContent = lrPos.toFixed(2);
    lrNegOut.textContent = lrNeg.toFixed(2);
  }

  [vpInput, fpInput, fnInput, vnInput].forEach(inp => {
    if (inp) inp.addEventListener('input', calculateMBE);
  });
  calculateMBE();
}

/* ==========================================================================
   5. CHECKLIST INTERATIVO DE CIRURGIA E PARTO SEGURO (OMS)
   ========================================================================== */
function initSafeSurgeryChecklist() {
  const checkboxes = document.querySelectorAll('.checklist-item');
  const progressText = document.getElementById('checklist-progress-text');
  const progressBar = document.getElementById('checklist-progress-bar');
  const resetBtn = document.getElementById('checklist-reset');
  const completeAlert = document.getElementById('checklist-complete-alert');

  function updateChecklist() {
    const total = checkboxes.length;
    if (total === 0) return;
    const checked = Array.from(checkboxes).filter(cb => cb.checked).length;
    const percent = Math.round((checked / total) * 100);

    if (progressText) progressText.textContent = `${checked} de ${total} itens verificados (${percent}%)`;
    if (progressBar) progressBar.style.width = `${percent}%`;

    if (completeAlert) {
      if (percent === 100) {
        completeAlert.classList.remove('hidden');
      } else {
        completeAlert.classList.add('hidden');
      }
    }
  }

  checkboxes.forEach(cb => cb.addEventListener('change', updateChecklist));
  
  if (resetBtn) {
    resetBtn.addEventListener('click', () => {
      checkboxes.forEach(cb => cb.checked = false);
      updateChecklist();
    });
  }

  updateChecklist();
}

/* ==========================================================================
   6. GERADOR DE PASSAGEM DE PLANTÃO (SBAR)
   ========================================================================== */
function initSBARGenerator() {
  const btn = document.getElementById('sbar-generate-btn');
  const copyBtn = document.getElementById('sbar-copy-btn');
  const outputArea = document.getElementById('sbar-output');
  if (!btn || !outputArea) return;

  btn.addEventListener('click', () => {
    const s = document.getElementById('sbar-s').value.trim();
    const b = document.getElementById('sbar-b').value.trim();
    const a = document.getElementById('sbar-a').value.trim();
    const r = document.getElementById('sbar-r').value.trim();

    const formatted = `📋 PASSAGEM DE PLANTÃO OBSTÉTRICA (PROTOCOLO SBAR)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[S] SITUAÇÃO (Situation):
${s || 'Não preenchido'}

[B] BREVE HISTÓRICO (Background):
${b || 'Não preenchido'}

[A] AVALIAÇÃO CLÍNICA (Assessment):
${a || 'Não preenchido'}

[R] RECOMENDAÇÃO / PLANO (Recommendation):
${r || 'Não preenchido'}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data/Hora: ${new Date().toLocaleString('pt-BR')}`;

    outputArea.value = formatted;
    if (copyBtn) copyBtn.classList.remove('hidden');
  });

  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      outputArea.select();
      navigator.clipboard.writeText(outputArea.value);
      copyBtn.textContent = "Copiado com Sucesso!";
      setTimeout(() => {
        copyBtn.textContent = "Copiar Texto SBAR";
      }, 2500);
    });
  }
}

/* ==========================================================================
   7. ESCADA ANALGÉSICA DA OMS & CUIDADOS PALIATIVOS
   ========================================================================== */
function initPainLadder() {
  const slider = document.getElementById('pain-eva-slider');
  const evaDisplay = document.getElementById('pain-eva-val');
  const stepCard = document.getElementById('pain-step-result');
  if (!slider || !evaDisplay || !stepCard) return;

  function updatePainStep() {
    const val = parseInt(slider.value, 10);
    evaDisplay.textContent = val;

    let title = "";
    let meds = "";
    let colorClass = "";

    if (val === 0) {
      title = "Sem Dor (EVA 0)";
      meds = "Manter observação clínica e reavaliação periódica dos sintomas.";
      colorClass = "border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-900/40";
    } else if (val <= 3) {
      title = "DEGRAU 1: Dor Leve (EVA 1-3)";
      meds = `
        <strong>Analgésicos Não Opióides:</strong><br>
        • Dipirona 1g VO/IV de 6/6h OU Paracetamol 500-750 mg VO de 6/6h.<br>
        • ± Anti-inflamatório não esteroidal (AINE): Cetoprofeno ou Ibuprofeno por curto prazo (3-5 dias), se ausência de disfunção renal ou gastropatia.<br>
        • ± Adjuvantes conforme mecanismo da dor (neuropática, óssea, espasmo visceral).
      `;
      colorClass = "border-emerald-500 bg-emerald-50/50 dark:bg-emerald-950/20";
    } else if (val <= 6) {
      title = "DEGRAU 2: Dor Moderada (EVA 4-6)";
      meds = `
        <strong>Opióides Fracos + Não Opióides:</strong><br>
        • Tramadol 50-100 mg VO de 6/6h (máx 400 mg/dia) OU Codeína 30-60 mg VO de 4/4h a 6/6h (máx 360 mg/dia).<br>
        • Manter analgésico de base: Dipirona 1g de 6/6h.<br>
        • <span class="text-rose-600 dark:text-rose-400 font-bold">⚠️ ALERTA: Prescrever laxativo profilático (ex: Lactulose 15-30 mL/dia ou Picossulfato) — a constipação por opióide não desenvolve tolerância!</span>
      `;
      colorClass = "border-amber-500 bg-amber-50/50 dark:bg-amber-950/20";
    } else {
      title = "DEGRAU 3: Dor Intensa / Refratária (EVA 7-10)";
      meds = `
        <strong>Opióides Fortes Potentes:</strong><br>
        • <strong>Morfina:</strong> 10 mg VO de 4/4h (ou 5 mg se idoso/frágil) com dose de resgate de 10% a 1/6 da dose diária total para dor incidental.<br>
        • Não há teto de dose terapêutica para morfina na dor oncológica: titular progressivamente até o alívio eficaz da dor.<br>
        • Alternativas: Metadona (ótima em dor neuropática/mista), Fentanil transdérmico (se náuseas/obstrução intestinal).<br>
        • <span class="text-rose-600 dark:text-rose-400 font-bold">⚠️ OBRIGATÓRIO: Prescrição conjunta de laxante diário + Antiemético (Haloperidol ou Ondansetrona nas primeiras 48-72h).</span>
      `;
      colorClass = "border-rose-500 bg-rose-50/50 dark:bg-rose-950/20";
    }

    stepCard.className = `p-4 rounded-xl border-2 transition-all ${colorClass}`;
    stepCard.innerHTML = `<h4 class="font-bold text-base mb-1 text-slate-900 dark:text-slate-100">${title}</h4><div class="text-xs text-slate-700 dark:text-slate-300 leading-relaxed">${meds}</div>`;
  }

  slider.addEventListener('input', updatePainStep);
  updatePainStep();
}

/* ==========================================================================
   8. PROTOCOLO INTERATIVO DE VIOLÊNCIA SEXUAL (PCDT MS)
   ========================================================================== */
function initSexualViolenceProtocol() {
  const timeSelect = document.getElementById('violence-time-select');
  const pregnancyCheck = document.getElementById('violence-pregnancy-check');
  const pepStatus = document.getElementById('violence-pep-status');
  const ecStatus = document.getElementById('violence-ec-status');
  const guidanceBox = document.getElementById('violence-guidance');
  if (!timeSelect || !pepStatus || !ecStatus) return;

  function updateProtocol() {
    const hours = parseInt(timeSelect.value, 10);
    const isPregnant = pregnancyCheck ? pregnancyCheck.checked : false;

    if (hours <= 72) {
      pepStatus.innerHTML = `<span class="text-emerald-600 dark:text-emerald-400 font-bold">INDICADA IMEDIATAMENTE (Janela Ideal < 72h)</span><br>Esquema Preferencial MS (28 dias): Tenofovir (TDF 300mg) + Lamivudina (3TC 300mg) + Dolutegravir (DTG 50mg) em dose única diária.`;
      ecStatus.innerHTML = isPregnant 
        ? `<span class="text-slate-500">Gestação confirmada: não aplicável.</span>`
        : `<span class="text-emerald-600 dark:text-emerald-400 font-bold">INDICADA</span><br>Levonorgestrel 1,5 mg VO em dose única imediata.`;
    } else if (hours <= 120) {
      pepStatus.innerHTML = `<span class="text-rose-600 dark:text-rose-400 font-bold">NÃO INDICADA PARA HIV (> 72h)</span><br>Eficácia da PEP não comprovada após 72h do contato. Solicitar testagem rápida basal e acompanhamento sorológico.`;
      ecStatus.innerHTML = isPregnant
        ? `<span class="text-slate-500">Gestação confirmada: não aplicável.</span>`
        : `<span class="text-amber-600 dark:text-amber-400 font-bold">OPÇÃO DE RESGATE (até 120h)</span><br>Inserção de DIU de Cobre pós-coito de emergência (eficácia > 99% até 5 dias), se consentido e ausência de contraindicação infecciosa aguda.`;
    } else {
      pepStatus.innerHTML = `<span class="text-rose-600 dark:text-rose-400 font-bold">FORA DA JANELA (> 120h)</span><br>Realizar testagem rápida para HIV, Sífilis e Hepatites virais. Agendar retorno em 30, 90 e 180 dias.`;
      ecStatus.innerHTML = `<span class="text-rose-600 dark:text-rose-400 font-bold">FORA DA JANELA</span><br>Agendar dosagem de β-hCG em 2 semanas para avaliação de gestação.`;
    }

    if (guidanceBox) {
      guidanceBox.innerHTML = `
        <div class="space-y-1 text-xs text-slate-700 dark:text-slate-300">
          <p><strong>• Antibioticoprofilaxia de ISTs não virais (imediata):</strong> Ceftriaxona 500 mg IM (gonococo) + Azitromicina 1g VO (clamídia) + Metronidazol 2g VO (tricomoníase).</p>
          <p><strong>• Profilaxia para Hepatite B:</strong> Vacina (0, 1 e 6 meses) + Imunoglobulina Humana Anti-Hepatite B (HBIG) até 14 dias se não imunizada ou parceiro HBsAg positivo.</p>
          <p><strong>• Aspectos Legais e Direitos:</strong> Atendimento sem julgamentos. Notificação compulsória obrigatória. <strong>NÃO EXIGIR Boletim de Ocorrência (BO) ou autorização judicial</strong> para profilaxia ou acesso ao aborto legal se gravidez decorrente de estupro.</p>
        </div>
      `;
    }
  }

  timeSelect.addEventListener('change', updateProtocol);
  if (pregnancyCheck) pregnancyCheck.addEventListener('change', updateProtocol);
  updateProtocol();
}

/* ==========================================================================
   9. BANCO DE FLASHCARDS INTERATIVOS (3D FLIP)
   ========================================================================== */
const flashcardsData = [
  {
    cat: 'semiologia',
    q: 'Qual é o rastreamento recomendado para Câncer do Colo Uterino no Brasil (Diretrizes MS)?',
    a: 'Iniciar aos 25 anos em mulheres com sexarca. Coleta anual citopatológica (Papanicolaou); após 2 exames consecutivos normais com intervalo de 1 ano, o rastreamento passa a ser a cada 3 anos até os 64 anos.'
  },
  {
    cat: 'semiologia',
    q: 'O que avalia o Índice de Bishop e qual pontuação indica colo favorável?',
    a: 'Avalia 5 parâmetros cervicais: Dilatação, Apagamento, Consistência, Posição e Altura da Apresentação (Plano De Lee). Pontuação ≥ 8 indica colo maduro/favorável (indução com Ocitocina). Bishop < 6 indica colo desfavorável (maturação prévia necessária).'
  },
  {
    cat: 'semiologia',
    q: 'Qual o sinal semiológico de Chandelier e qual seu significado clínico?',
    a: 'Dor excruciante à mobilização do colo uterino ao toque bimanual. É altamente sugestivo de peritonite pélvica decorrente de Doença Inflamatória Pélvica (DIP) aguda ou Gravidez Ectópica Rota.'
  },
  {
    cat: 'raciocinio',
    q: 'Qual o primeiro exame mandatório diante de qualquer mulher em idade fértil com dor pélvica aguda?',
    a: 'Dosagem de β-hCG (teste imunológico de gravidez). O objetivo prioritário é confirmar ou excluir precocemente gravidez ectópica rota, que constitui emergência cirúrgica potencialmente fatal.'
  },
  {
    cat: 'raciocinio',
    q: 'Como diferenciar clinicamente o Descolamento Prematuro de Placenta (DPP) da Placenta Prévia (PP)?',
    a: 'DPP: Sangramento vermelho-escuro, DOR abdominal súbita intensa, hipertonia uterina (útero em tábua) e sofrimento fetal agudo frequente. Placenta Prévia: Sangramento vermelho-rutilante (vivo), INDOLOR, tônus uterino normal e vitalidade fetal habitualmente preservada no início.'
  },
  {
    cat: 'raciocinio',
    q: 'Por que o toque vaginal é contraindicado em sangramento do 3º trimestre sem ultrassom prévio?',
    a: 'Porque se a etiologia for Placenta Prévia, o dedo examinador pode descolar o tecido placentário sobre o orifício interno do colo, deflagrando hemorragia cataclísmica materna e fetal imediata.'
  },
  {
    cat: 'raciocinio',
    q: 'Quais os 4 critérios de Amsel para diagnóstico de Vaginose Bacteriana (mínimo 3 de 4)?',
    a: '1. Corrimento acinzentado homogêneo e fino; 2. pH vaginal > 4,5; 3. Teste de Whiff positivo (odor a aminas com KOH 10%); 4. Presença de Clue Cells (células-guia) em mais de 20% das células epiteliais à microscopia.'
  },
  {
    cat: 'mbe',
    q: 'O que significam as regras SnNOut e SpPIn em testes diagnósticos?',
    a: 'SnNOut: Teste com alta Sensibilidade, quando Negativo, descarta a doença ("rules out"). SpPIn: Teste com alta Especificidade, quando Positivo, confirma a doença ("rules in").'
  },
  {
    cat: 'mbe',
    q: 'O que é o NNT (Número Necessário para Tratar) e como é calculado?',
    a: 'É o número de pacientes que precisam receber o tratamento experimental em comparação ao controle para evitar 1 desfecho adverso adicional. Fórmula: NNT = 1 / Redução Absoluta do Risco (RAR).'
  },
  {
    cat: 'seguranca',
    q: 'O que preconiza o Modelo do Queijo Suíço de James Reason na segurança do paciente?',
    a: 'Postula que as defesas do sistema consistem em múltiplas barreiras com falhas latentes pontuais (buracos). Um evento sentinela ou dano só ocorre quando as falhas de todas as camadas defensivas se alinham momentaneamente.'
  },
  {
    cat: 'seguranca',
    q: 'Quais as 3 etapas formais do Checklist de Cirurgia Segura da OMS em uma cesariana?',
    a: '1. Sign In: Antes da indução anestésica (identificação ativa, consentimento, via aérea, alergias); 2. Time Out: Antes da incisão cirúrgica (apresentação da equipe, profilaxia antibiótica <60 min, prevenção HPP); 3. Sign Out: Antes da saída de sala (contagem correta de compressas e agulhas, rotulagem de peças).'
  },
  {
    cat: 'comunicacao',
    q: 'Quais são as 6 etapas do Protocolo SPIKES para comunicação de más notícias?',
    a: 'S (Setting - Preparação do ambiente); P (Perception - Avaliar o que a paciente sabe); I (Invitation - Convidar e pedir permissão); K (Knowledge - Transmitir a notícia clara e compassiva); E (Empathy - Acolher as emoções); S (Strategy & Summary - Traçar estratégia e resumir o seguimento).'
  },
  {
    cat: 'bioetica',
    q: 'Em quais circunstâncias o aborto é legalmente permitido no Brasil?',
    a: '1. Risco de vida para a gestante (Código Penal art. 128, I); 2. Gravidez decorrente de estupro (art. 128, II); 3. Anencefalia fetal (STF, ADPF 54/2012). No estupro, a palavra da mulher é suficiente, sendo proibido exigir BO ou ordem judicial.'
  },
  {
    cat: 'paliativos',
    q: 'Qual a conduta obrigatória ao se prescrever opióides fortes (como morfina) na dor oncológica?',
    a: 'Prescrição profilática concomitante e mandatória de laxativos diários (ex: lactulose ou picossulfato), pois a constipação intestinal induzida por opióides não desenvolve tolerância farmacológica com o passar do tempo.'
  },
  {
    cat: 'paliativos',
    q: 'Qual a tríade medicamentosa recomendada no manejo clínico da obstrução intestinal maligna em gineco-oncologia?',
    a: 'Octreotida (análogo da somatostatina para diminuir secreções gastrointestinais) + Dexametasona (reduz edema tumoral peri-obstrutivo) + Haloperidol (antiemético central).'
  }
];

function initFlashcards() {
  const container = document.getElementById('flashcard-card');
  const questionEl = document.getElementById('flashcard-question');
  const answerEl = document.getElementById('flashcard-answer');
  const catBadge = document.getElementById('flashcard-cat');
  const counterEl = document.getElementById('flashcard-counter');
  const filterSelect = document.getElementById('flashcard-filter');
  const prevBtn = document.getElementById('flashcard-prev');
  const nextBtn = document.getElementById('flashcard-next');
  const flipBtn = document.getElementById('flashcard-flip');

  if (!container || !questionEl || !answerEl) return;

  let currentCategory = 'all';
  let filteredCards = [...flashcardsData];
  let currentIndex = 0;

  function filterCards() {
    if (currentCategory === 'all') {
      filteredCards = [...flashcardsData];
    } else {
      filteredCards = flashcardsData.filter(c => c.cat === currentCategory);
    }
    currentIndex = 0;
    renderCard();
  }

  function renderCard() {
    if (filteredCards.length === 0) return;
    const card = filteredCards[currentIndex];
    container.classList.remove('card-flipped');
    
    questionEl.textContent = card.q;
    answerEl.textContent = card.a;
    if (catBadge) catBadge.textContent = card.cat.toUpperCase();
    if (counterEl) counterEl.textContent = `${currentIndex + 1} / ${filteredCards.length}`;
  }

  if (flipBtn) {
    flipBtn.addEventListener('click', () => {
      container.classList.toggle('card-flipped');
    });
  }

  container.addEventListener('click', () => {
    container.classList.toggle('card-flipped');
  });

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (currentIndex < filteredCards.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      renderCard();
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = filteredCards.length - 1;
      }
      renderCard();
    });
  }

  if (filterSelect) {
    filterSelect.addEventListener('change', (e) => {
      currentCategory = e.target.value;
      filterCards();
    });
  }

  renderCard();
}

/* ==========================================================================
   10. SIMULADO DE QUESTÕES COMENTADAS (RESIDÊNCIA / USMLE)
   ========================================================================== */
const quizQuestions = [
  {
    q: "Primigesta de 39 semanas em trabalho de parto é avaliada pelo toque: dilatação de 2 cm, colo medianizado, apagamento de 40%, consistência média e apresentação fetal em plano -2 de De Lee. Qual é o Índice de Bishop e a conduta preconizada se a paciente não possui cicatrizes uterinas anteriores?",
    opts: [
      "Bishop 4; Indução direta com infusão de ocitocina IV.",
      "Bishop 4; Maturação cervical com misoprostol 25 mcg em fundo de saco.",
      "Bishop 8; Indução direta com infusão de ocitocina IV.",
      "Bishop 2; Indicação absoluta de cesariana eletiva imediata."
    ],
    ans: 1,
    exp: "Cálculo do Bishop: Dilatação 2 cm = 1 pt; Apagamento 40% = 1 pt; Consistência média = 1 pt; Posição mediana = 1 pt; De Lee -2 = 1 pt → Total = 5 pontos (Bishop < 6 = Colo Desfavorável). Em colo imaturo e útero sem cicatriz, a conduta padrão é maturação cervical com Misoprostol 25 mcg a cada 6h antes de qualquer infusão de ocitocina."
  },
  {
    q: "Secundigesta com 34 semanas e antecedente de cesárea prévia chega à emergência obstétrica com queixa de sangramento vaginal abundante indolor, vermelho-rutilante, iniciado espontaneamente em repouso. Ao exame físico, o abdome é flácido, indolor e os batimentos cardiofetais estão normais (142 bpm). Qual conduta é FORMALMENTE CONTRAINDICADA neste momento?",
    opts: [
      "Realização de ultrassonografia transvaginal.",
      "Instalação de dois acessos venosos periféricos calibrosos.",
      "Realização de toque vaginal digital.",
      "Coleta de tipagem sanguínea com prova cruzada e hemograma."
    ],
    ans: 2,
    exp: "O quadro clínico de sangramento vermelho-vivo, abundante, INDOLOR, associado a tônus uterino normal em paciente com cesárea prévia é clássico de Placenta Prévia. O toque vaginal digital é FORMALMENTE CONTRAINDICADO até a confirmação ultrassonográfica da localização placentária, sob risco de deflagrar hemorragia materna e fetal cataclísmica."
  },
  {
    q: "Mulher de 24 anos procura atendimento médico na UBS relatando corrimento acinzentado fino com odor fétido acentuado após a relação sexual. A microscopia a fresco revela células epiteliais com bordas obscurecidas por bactérias (clue cells) e pH vaginal de 5,2. Qual é a conduta terapêutica recomendada pelo Ministério da Saúde?",
    opts: [
      "Metronidazol 500 mg VO de 12/12h por 7 dias; não tratar o parceiro sexual.",
      "Fluconazol 150 mg VO dose única; tratar parceiro sexual obrigatoriamente.",
      "Metronidazol 2g VO dose única; tratar parceiro sexual obrigatoriamente.",
      "Ciprofloxacino 500 mg dose única; solicitar cultura endocervical."
    ],
    ans: 0,
    exp: "Trata-se de Vaginose Bacteriana (Critérios de Amsel preenchidos: corrimento característico, clue cells, pH > 4,5). O tratamento preconizado pelo PCDT/MS é Metronidazol 500 mg VO 12/12h por 7 dias. Por se tratar de disbiose endógena da microbiota e não de IST clássica, NÃO se recomenda o tratamento rotineiro do parceiro sexual."
  },
  {
    q: "Durante a passagem de caso de uma paciente que desenvolveu Hemorragia Pós-Parto (HPP) grave por atonia uterina no centro obstétrico, a residente utiliza o protocolo SBAR. A frase 'Paciente puérpera imediata com perda sanguínea estimada em 1.500 mL, taquicárdica com FC 125 bpm e hipotensa com PA 85/50 mmHg' corresponde a qual etapa da ferramenta?",
    opts: [
      "S (Situation)",
      "B (Background)",
      "A (Assessment)",
      "R (Recommendation)"
    ],
    ans: 2,
    exp: "A etapa 'A' (Assessment / Avaliação) compreende a análise clínica do profissional sobre os achados objetivos vigentes, gravidade hemodinâmica e hipótese diagnóstica do momento (choque hipovolêmico por HPP)."
  },
  {
    q: "Mulher de 28 anos, vítima de violência sexual ocorrida há 36 horas, comparece ao pronto atendimento hospitalar desacompanhada. Sobre o manejo clínico e legal desta paciente, assinale a conduta CORRETA:",
    opts: [
      "Exigir apresentação de Boletim de Ocorrência policial para liberar o kit de profilaxia de DSTs.",
      "Prescrever profilaxia pós-exposição para HIV (TDF + 3TC + DTG por 28 dias), antibioticoprofilaxia e contracepção de emergência.",
      "Não prescrever contracepção de emergência, pois a janela terapêutica máxima é de 24 horas.",
      "Recusar atendimento até a realização de exame de corpo de delito no Instituto Médico Legal (IML)."
    ],
    ans: 1,
    exp: "O atendimento à vítima de violência sexual é uma emergência médica. O Ministério da Saúde determina que NENHUM documento policial (BO) ou pericial (corpo de delito) pode ser exigido para o início imediato das condutas. Estando dentro de 72h, está indicada a PEP para HIV por 28 dias, antibioticoprofilaxia (ceftriaxona + azitromicina + metronidazol), vacina/imunoglobulina para hepatite B e contracepção de emergência oral (levonorgestrel até 72h)."
  }
];

function initQuiz() {
  const container = document.getElementById('quiz-container');
  if (!container) return;

  container.innerHTML = quizQuestions.map((q, idx) => `
    <div class="p-6 rounded-2xl glass-panel shadow-sm transition-all" id="quiz-q-${idx}">
      <div class="flex items-center justify-between mb-3">
        <span class="px-2.5 py-1 text-xs font-bold rounded-md bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300">Questão ${idx + 1} de ${quizQuestions.length}</span>
        <span class="text-xs text-slate-500">Residência Médica / USMLE</span>
      </div>
      <p class="font-semibold text-slate-800 dark:text-slate-100 text-sm mb-4 leading-relaxed">${q.q}</p>
      <div class="space-y-2 mb-4">
        ${q.opts.map((opt, oIdx) => `
          <button type="button" class="quiz-opt-btn w-full text-left p-3 rounded-xl border border-slate-200 dark:border-slate-700 hover:border-sky-500 dark:hover:border-sky-400 text-xs font-medium text-slate-700 dark:text-slate-300 transition-all flex items-start gap-2.5" data-q="${idx}" data-opt="${oIdx}">
            <span class="inline-flex items-center justify-center w-5 h-5 rounded-full bg-slate-100 dark:bg-slate-800 text-[10px] font-bold text-slate-600 dark:text-slate-300 flex-shrink-0">${String.fromCharCode(65 + oIdx)}</span>
            <span>${opt}</span>
          </button>
        `).join('')}
      </div>
      <div class="quiz-feedback hidden p-4 rounded-xl text-xs leading-relaxed transition-all"></div>
    </div>
  `).join('');

  const optButtons = container.querySelectorAll('.quiz-opt-btn');
  optButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const qIdx = parseInt(btn.dataset.q, 10);
      const chosenOpt = parseInt(btn.dataset.opt, 10);
      const qData = quizQuestions[qIdx];
      const card = document.getElementById(`quiz-q-${qIdx}`);
      const feedback = card.querySelector('.quiz-feedback');
      const allBtns = card.querySelectorAll('.quiz-opt-btn');

      allBtns.forEach((b, bIdx) => {
        b.disabled = true;
        b.classList.remove('hover:border-sky-500', 'dark:hover:border-sky-400');
        if (bIdx === qData.ans) {
          b.className = "w-full text-left p-3 rounded-xl border-2 border-emerald-500 bg-emerald-50/70 dark:bg-emerald-950/40 text-xs font-bold text-emerald-900 dark:text-emerald-200 flex items-start gap-2.5";
        } else if (bIdx === chosenOpt) {
          b.className = "w-full text-left p-3 rounded-xl border-2 border-rose-500 bg-rose-50/70 dark:bg-rose-950/40 text-xs font-medium text-rose-900 dark:text-rose-200 flex items-start gap-2.5";
        } else {
          b.className = "w-full text-left p-3 rounded-xl border border-slate-200 dark:border-slate-800 opacity-60 text-xs text-slate-500 flex items-start gap-2.5";
        }
      });

      feedback.classList.remove('hidden');
      if (chosenOpt === qData.ans) {
        feedback.className = "quiz-feedback p-4 rounded-xl text-xs leading-relaxed bg-emerald-100/80 dark:bg-emerald-900/40 border border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-100";
        feedback.innerHTML = `<strong>Correto! ✓</strong><br>${qData.exp}`;
      } else {
        feedback.className = "quiz-feedback p-4 rounded-xl text-xs leading-relaxed bg-rose-100/80 dark:bg-rose-900/40 border border-rose-300 dark:border-rose-800 text-rose-900 dark:text-rose-100";
        feedback.innerHTML = `<strong>Incorreto. ✗</strong> Resposta correta: Alternativa ${String.fromCharCode(65 + qData.ans)}.<br>${qData.exp}`;
      }
    });
  });
}

/* ==========================================================================
   11. LIGHTBOX MODAL COM ZOOM PARA INFOGRÁFICOS
   ========================================================================== */
function initLightbox() {
  const modal = document.getElementById('lightbox-modal');
  const imgEl = document.getElementById('lightbox-image');
  const titleEl = document.getElementById('lightbox-title');
  const closeBtn = document.getElementById('lightbox-close');
  const zoomInBtn = document.getElementById('lightbox-zoom-in');
  const zoomOutBtn = document.getElementById('lightbox-zoom-out');
  const zoomResetBtn = document.getElementById('lightbox-zoom-reset');

  if (!modal || !imgEl) return;

  let currentScale = 1;

  document.querySelectorAll('[data-lightbox]').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const src = trigger.dataset.lightbox || trigger.src;
      const title = trigger.dataset.title || trigger.alt || "Infográfico Médico";
      imgEl.src = src;
      if (titleEl) titleEl.textContent = title;
      currentScale = 1;
      imgEl.style.transform = `scale(${currentScale})`;
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    });
  });

  function closeModal() {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      closeModal();
    }
  });

  if (zoomInBtn) {
    zoomInBtn.addEventListener('click', () => {
      currentScale = Math.min(currentScale + 0.25, 3);
      imgEl.style.transform = `scale(${currentScale})`;
    });
  }

  if (zoomOutBtn) {
    zoomOutBtn.addEventListener('click', () => {
      currentScale = Math.max(currentScale - 0.25, 0.5);
      imgEl.style.transform = `scale(${currentScale})`;
    });
  }

  if (zoomResetBtn) {
    zoomResetBtn.addEventListener('click', () => {
      currentScale = 1;
      imgEl.style.transform = `scale(${currentScale})`;
    });
  }
}
