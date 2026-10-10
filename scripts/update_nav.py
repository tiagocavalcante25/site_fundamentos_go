"""
update_nav.py
Substitui o header antigo e remove o menu lateral redundante em index.html.
Instala o novo header com position: fixed no topo da tela, 100% responsivo.
"""
import os
import re

site_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_path = os.path.join(site_dir, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_header = '''  <!-- ======================================================================
       HEADER / NAVBAR FIXO NO TOPO (POSITION: FIXED, 100% RESPONSIVO, SEM GAVETA REDUNDANTE)
       ====================================================================== -->
  <header class="fixed top-0 left-0 right-0 w-full z-50 glass-nav border-b border-slate-200/80 dark:border-slate-800/80 transition-colors">
    <!-- Nível 1: Barra Principal -->
    <div class="w-full max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-14 sm:h-16 gap-2 sm:gap-3">
        
        <!-- Logo e Título com Identidade Visual SUS / FEBRASGO -->
        <a href="#" class="flex items-center gap-2 sm:gap-2.5 min-w-0 flex-shrink group" title="Fundamentos em GO - Início">
          <div class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-tr from-sky-600 via-teal-500 to-emerald-500 flex items-center justify-center text-white shadow-md shadow-sky-500/20 group-hover:scale-105 transition-transform flex-shrink-0">
            <i data-lucide="stethoscope" class="w-4 h-4"></i>
          </div>
          <div class="min-w-0">
            <div class="flex items-center gap-1.5">
              <span class="nav-brand-title font-extrabold text-xs sm:text-base tracking-tight text-slate-900 dark:text-white truncate">Fundamentos em GO</span>
              <span class="text-[9px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hidden xs:inline-block flex-shrink-0">SUS</span>
            </div>
          </div>
        </a>

        <!-- Barra de Busca Global Inteligente (Desktop & Tablet) -->
        <div class="hidden md:flex items-center flex-1 max-w-sm lg:max-w-md mx-2 lg:mx-4">
          <div class="relative w-full">
            <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
            <input type="text" id="global-search" placeholder="Buscar módulos, condutas, escores..." 
              class="w-full pl-9 pr-14 py-2 text-xs rounded-xl bg-slate-100/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 focus:outline-none focus:ring-2 focus:ring-sky-500 text-slate-800 dark:text-slate-200 placeholder-slate-400 transition-all">
            <kbd class="hidden lg:inline-flex items-center absolute right-2.5 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-semibold text-slate-400 dark:text-slate-500 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded shadow-sm">Ctrl K</kbd>
          </div>
        </div>

        <!-- Ações Rápidas: Top 20, Flashcards, Simulado, Font Size e Tema (Adaptados para Mobile) -->
        <div class="flex items-center gap-1 sm:gap-2 flex-shrink-0">
          
          <!-- Hubs de Treinamento Rápido -->
          <nav class="flex items-center gap-1 sm:gap-1.5">
            <a href="#high-yield" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg font-bold text-amber-700 dark:text-amber-300 bg-amber-50 hover:bg-amber-100 dark:bg-amber-950/40 dark:hover:bg-amber-900/40 border border-amber-200/80 dark:border-amber-800/60 transition-colors" title="Top 20 Pérolas Clínicas">
              <i data-lucide="star" class="w-3.5 h-3.5 text-amber-500"></i>
              <span class="hidden sm:inline">Top 20</span>
            </a>
            <a href="#flashcards" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg font-bold text-sky-700 dark:text-sky-300 bg-sky-50 hover:bg-sky-100 dark:bg-sky-950/40 dark:hover:bg-sky-900/40 border border-sky-200/80 dark:border-sky-800/60 transition-colors" title="Flashcards Interativos">
              <i data-lucide="layers" class="w-3.5 h-3.5 text-sky-500"></i>
              <span class="hidden sm:inline">Cards</span>
            </a>
            <a href="#quiz" class="nav-pill-btn inline-flex items-center gap-1 px-2 py-1 sm:px-2.5 sm:py-1.5 rounded-lg font-bold text-emerald-700 dark:text-emerald-300 bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/40 dark:hover:bg-emerald-900/40 border border-emerald-200/80 dark:border-emerald-800/60 transition-colors" title="Simulado de Questões">
              <i data-lucide="check-square" class="w-3.5 h-3.5 text-emerald-500"></i>
              <span class="hidden sm:inline">Simulado</span>
            </a>
          </nav>

          <!-- Controle de Tamanho da Fonte (A / A+ / A++) Direto na Barra Fixa -->
          <div class="inline-flex items-center bg-slate-100 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-lg p-0.5" title="Ajustar tamanho da fonte para leitura confortável">
            <button type="button" data-font-size-set="normal" aria-label="Tamanho de fonte normal" title="Fonte padrão" class="font-size-btn px-1.5 py-0.5 font-bold rounded transition-colors">A</button>
            <button type="button" data-font-size-set="large" aria-label="Tamanho de fonte grande" title="Fonte ampliada" class="font-size-btn px-1.5 py-0.5 font-bold rounded transition-colors">A+</button>
            <button type="button" data-font-size-set="xlarge" aria-label="Tamanho de fonte máximo" title="Fonte máxima" class="font-size-btn px-1.5 py-0.5 font-black rounded transition-colors">A++</button>
          </div>

          <!-- Botão de Alternância de Tema Claro/Escuro -->
          <button id="theme-toggle" type="button" aria-label="Alternar modo claro/escuro" title="Alternar modo claro/escuro" 
            class="theme-toggle-btn p-1.5 sm:p-2 rounded-xl text-slate-600 hover:text-slate-900 dark:text-slate-300 dark:hover:text-white bg-slate-100 hover:bg-slate-200 dark:bg-slate-900 hover:dark:bg-slate-800 border border-slate-200 dark:border-slate-800 transition-colors flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-sky-500">
            <i data-lucide="sun" class="w-3.5 h-3.5 sm:w-4 sm:h-4 icon-sun text-amber-500"></i>
            <i data-lucide="moon" class="w-3.5 h-3.5 sm:w-4 sm:h-4 icon-moon text-slate-700 dark:text-slate-300"></i>
          </button>

        </div>

      </div>
    </div>

    <!-- Nível 2: Faixa Subnav Contínua de Módulos Clínicos & Ferramentas Rápidas (Acesso Direto em Celulares, Tablets e Desktops) -->
    <div class="w-full border-t border-slate-200/70 dark:border-slate-800/70 bg-slate-50/80 dark:bg-slate-950/80 backdrop-blur-md">
      <div class="w-full max-w-7xl mx-auto px-3 sm:px-6 lg:px-8">
        <div class="flex items-center gap-1 sm:gap-1.5 overflow-x-auto no-scrollbar py-1.5 text-xs font-semibold whitespace-nowrap">
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-0.5 flex items-center gap-1 flex-shrink-0">
            <i data-lucide="layers" class="w-3 h-3 text-sky-500"></i> Módulos:
          </span>
          <a href="#modulo-21" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-sky-100 dark:bg-sky-950 text-sky-700 dark:text-sky-300 text-[10px] font-bold flex items-center justify-center">21</span>
            Semiologia
          </a>
          <a href="#modulo-22" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">22</span>
            Raciocínio
          </a>
          <a href="#modulo-23" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 text-[10px] font-bold flex items-center justify-center">23</span>
            MBE
          </a>
          <a href="#modulo-24" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-teal-100 dark:bg-teal-950 text-teal-700 dark:text-teal-300 text-[10px] font-bold flex items-center justify-center">24</span>
            Segurança OMS
          </a>
          <a href="#modulo-25" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-300 text-[10px] font-bold flex items-center justify-center">25</span>
            Comunicação
          </a>
          <a href="#modulo-26" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 text-[10px] font-bold flex items-center justify-center">26</span>
            Bioética
          </a>
          <a href="#modulo-27" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-sky-100 dark:bg-sky-950 text-sky-700 dark:text-sky-300 text-[10px] font-bold flex items-center justify-center">27</span>
            Direitos
          </a>
          <a href="#modulo-28" class="subnav-pill px-2 py-0.5 rounded-md text-slate-700 dark:text-slate-300 hover:text-sky-600 dark:hover:text-sky-400 hover:bg-sky-50 dark:hover:bg-slate-800/80 transition-colors flex items-center gap-1 flex-shrink-0">
            <span class="w-4 h-4 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 text-[10px] font-bold flex items-center justify-center">28</span>
            Paliativos
          </a>

          <!-- Separador -->
          <span class="h-3.5 w-px bg-slate-300 dark:bg-slate-700 mx-1 flex-shrink-0"></span>

          <!-- Ferramentas Clínicas Diretas -->
          <span class="text-[10px] uppercase font-bold text-slate-400 dark:text-slate-500 mr-0.5 flex items-center gap-1 flex-shrink-0">
            <i data-lucide="zap" class="w-3 h-3 text-amber-500"></i> Ferramentas:
          </span>
          <a href="#calc-bishop" class="subnav-pill px-2 py-0.5 rounded-md text-emerald-700 dark:text-emerald-400 hover:bg-emerald-50 dark:hover:bg-emerald-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="calculator" class="w-3 h-3"></i>
            Bishop
          </a>
          <a href="#calc-mbe" class="subnav-pill px-2 py-0.5 rounded-md text-indigo-700 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="bar-chart-2" class="w-3 h-3"></i>
            MBE 2x2
          </a>
          <a href="#checklist-cirurgico" class="subnav-pill px-2 py-0.5 rounded-md text-teal-700 dark:text-teal-400 hover:bg-teal-50 dark:hover:bg-teal-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="clipboard-check" class="w-3 h-3"></i>
            Checklist OMS
          </a>
          <a href="#gerador-sbar" class="subnav-pill px-2 py-0.5 rounded-md text-amber-700 dark:text-amber-400 hover:bg-amber-50 dark:hover:bg-amber-950/40 transition-colors flex items-center gap-1 flex-shrink-0">
            <i data-lucide="message-square" class="w-3 h-3"></i>
            SBAR
          </a>
        </div>
      </div>
    </div>

    <!-- Barra de Progresso de Leitura Contínua -->
    <div id="reading-progress" class="h-1 bg-gradient-to-r from-sky-500 via-teal-400 to-emerald-500 w-0 transition-all duration-150 ease-out" role="progressbar" aria-label="Progresso de leitura"></div>
  </header>'''

# Match from start of header to end of aside
pattern = re.compile(r'  <!-- =+\s+HEADER / NAVBAR.*?</aside>', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(new_header, content)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('SUCCESS: Header replaced and redundant drawer removed cleanly!')
else:
    print('ERROR: Pattern not matched!')
