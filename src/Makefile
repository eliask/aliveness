# Makefile for The Four Axioms of Aliveness
# Professional LaTeX book compilation

# Configuration
MAIN = book
PDF = Aliveness__Principles_of_Telic_Systems.pdf
HTML = Aliveness__Principles_of_Telic_Systems.html
EPUB = Aliveness__Principles_of_Telic_Systems.epub
LATEX = xelatex
BIBTEX = bibtex
PANDOC = pandoc
TEXDIR = .

# Part PDFs
PART1_TEX = part1_diagnosis
PART1_PDF = Part1_The_Diagnosis.pdf
PART1_TXT = Part1_The_Diagnosis.txt
PART2_TEX = part2_autopsy
PART2_PDF = Part2_The_Autopsy.pdf
PART2_TXT = Part2_The_Autopsy.txt
PART3_TEX = part3_source_code
PART3_PDF = Part3_The_Source_Code.pdf
PART3_TXT = Part3_The_Source_Code.txt
PART4_TEX = part4_blueprint
PART4_PDF = Part4_The_Blueprint.pdf
PART4_TXT = Part4_The_Blueprint.txt
PART5_TEX = part5_integrated_human
PART5_PDF = Part5_The_Integrated_Human.pdf
PART5_TXT = Part5_The_Integrated_Human.txt

ALL_PART_PDFS = $(PART1_PDF) $(PART2_PDF) $(PART3_PDF) $(PART4_PDF) $(PART5_PDF)
ALL_PART_TXTS = $(PART1_TXT) $(PART2_TXT) $(PART3_TXT) $(PART4_TXT) $(PART5_TXT)

# Appendices PDF
APPENDICES_TEX = appendices
APPENDICES_PDF = Appendices.pdf
APPENDICES_TXT = Appendices.txt

# Color output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
NC = \033[0m

# Default target - build everything
.PHONY: all
all: $(PDF) $(ALL_PART_PDFS) $(ALL_PART_TXTS) $(APPENDICES_PDF) $(APPENDICES_TXT) $(HTML) $(EPUB)
	@echo ""
	@echo "$(GREEN)========================================$(NC)"
	@echo "$(GREEN)✓ All formats built successfully!$(NC)"
	@echo "$(GREEN)========================================$(NC)"
	@echo "  Main book PDF:   $(PDF)"
	@echo "  Part PDFs:       5 files (Part1-5_*.pdf)"
	@echo "  Part TXTs:       5 files (Part1-5_*.txt)"
	@echo "  Appendices PDF:  $(APPENDICES_PDF)"
	@echo "  Appendices TXT:  $(APPENDICES_TXT)"
	@echo "  HTML:            $(HTML)"
	@echo "  EPUB:            $(EPUB)"
	@echo ""

# Build main PDF only (without parts/html/epub)
.PHONY: pdf
pdf: $(PDF)

# Build PDF (requires 2 passes for TOC, 3 for references if added)
# Note: Warnings about multiply-defined labels are normal and harmless
$(PDF): $(MAIN).tex preamble.tex $(wildcard $(TEXDIR)/*.tex)
	@echo "$(GREEN)[1/3]$(NC) First LaTeX pass..."
	-@$(LATEX) -interaction=nonstopmode $(MAIN).tex > /dev/null 2>&1
	@echo "$(GREEN)[2/3]$(NC) Second LaTeX pass (for TOC)..."
	-@$(LATEX) -interaction=nonstopmode $(MAIN).tex > /dev/null 2>&1
	@echo "$(GREEN)[3/3]$(NC) Third LaTeX pass (finalize)..."
	@$(LATEX) -interaction=nonstopmode $(MAIN).tex | grep -E '(Output written|Error|Fatal)' || true
	@if [ -f $(MAIN).pdf ]; then \
		mv $(MAIN).pdf $(PDF); \
		echo "$(GREEN)✓ Build complete:$(NC) $(PDF)"; \
		PAGES=$$(grep -o 'Output written.*(\([0-9]*\) page' $(MAIN).log 2>/dev/null | grep -o '[0-9]*' || echo '?'); \
		echo "  Pages: $$PAGES"; \
		echo "  Size: $$(du -h $(PDF) | cut -f1)"; \
	else \
		echo "$(RED)✗ Build failed - no PDF generated$(NC)"; \
		exit 1; \
	fi

# Quick build (single pass, for testing)
.PHONY: quick
quick: $(MAIN).tex preamble.tex
	@echo "$(YELLOW)Quick build (single pass)...$(NC)"
	$(LATEX) -interaction=nonstopmode $(MAIN).tex
	@mv $(MAIN).pdf $(PDF)
	@echo "$(GREEN)✓ Quick build complete$(NC)"

# ============================================================================
# PART PDFS (for reader convenience)
# ============================================================================

# Build all parts
.PHONY: parts
parts: part1 part2 part3 part4 part5
	@echo "$(GREEN)✓ All parts built successfully$(NC)"

# Generic part build function
define build_part
	@echo "$(GREEN)[1/2]$(NC) Building $(2)..."
	-@$(LATEX) -interaction=nonstopmode $(1).tex > /dev/null 2>&1
	@echo "$(GREEN)[2/2]$(NC) Finalizing $(2)..."
	@$(LATEX) -interaction=nonstopmode $(1).tex | grep -E '(Output written|Error|Fatal)' || true
	@if [ -f $(1).pdf ]; then \
		mv $(1).pdf $(2); \
		echo "$(GREEN)✓ Part complete:$(NC) $(2)"; \
		PAGES=$$(grep -o 'Output written.*(\([0-9]*\) page' $(1).log 2>/dev/null | grep -o '[0-9]*' || echo '?'); \
		echo "  Pages: $$PAGES"; \
		echo "  Size: $$(du -h $(2) | cut -f1)"; \
	else \
		echo "$(RED)✗ Build failed - no PDF generated$(NC)"; \
		exit 1; \
	fi
endef

# Individual part targets
# (make the PDFs real file targets so `make ALL` can build them)
$(PART1_PDF): $(PART1_TEX).tex preamble.tex
	$(call build_part,$(PART1_TEX),$(PART1_PDF))

$(PART2_PDF): $(PART2_TEX).tex preamble.tex
	$(call build_part,$(PART2_TEX),$(PART2_PDF))

$(PART3_PDF): $(PART3_TEX).tex preamble.tex
	$(call build_part,$(PART3_TEX),$(PART3_PDF))

$(PART4_PDF): $(PART4_TEX).tex preamble.tex
	$(call build_part,$(PART4_TEX),$(PART4_PDF))

$(PART5_PDF): $(PART5_TEX).tex preamble.tex
	$(call build_part,$(PART5_TEX),$(PART5_PDF))

.PHONY: part1 part2 part3 part4 part5
part1: $(PART1_PDF)
part2: $(PART2_PDF)
part3: $(PART3_PDF)
part4: $(PART4_PDF)
part5: $(PART5_PDF)

# ============================================================================
# APPENDICES PDF
# ============================================================================

# Build appendices standalone PDF
.PHONY: appendices
appendices: $(APPENDICES_PDF)

$(APPENDICES_PDF): $(APPENDICES_TEX).tex preamble.tex $(wildcard appendix_*.tex)
	$(call build_part,$(APPENDICES_TEX),$(APPENDICES_PDF))

# ============================================================================
# TXT FILES FROM PARTS AND APPENDICES
# ============================================================================

# Generic PDF to TXT conversion function
define pdf_to_txt
	@echo "$(GREEN)Converting $(1) to text...$(NC)"
	@pdftotext -layout $(1) $(2)
	@if [ -f $(2) ]; then \
		echo "$(GREEN)✓ Text conversion complete:$(NC) $(2)"; \
		echo "  Size: $$(du -h $(2) | cut -f1)"; \
		echo "  Words: $$(wc -w < $(2) | xargs)"; \
	else \
		echo "$(YELLOW)Trying alternative method (no layout)...$(NC)"; \
		pdftotext $(1) $(2); \
	fi
endef

# Part TXT targets
$(PART1_TXT): $(PART1_PDF)
	$(call pdf_to_txt,$(PART1_PDF),$(PART1_TXT))

$(PART2_TXT): $(PART2_PDF)
	$(call pdf_to_txt,$(PART2_PDF),$(PART2_TXT))

$(PART3_TXT): $(PART3_PDF)
	$(call pdf_to_txt,$(PART3_PDF),$(PART3_TXT))

$(PART4_TXT): $(PART4_PDF)
	$(call pdf_to_txt,$(PART4_PDF),$(PART4_TXT))

$(PART5_TXT): $(PART5_PDF)
	$(call pdf_to_txt,$(PART5_PDF),$(PART5_TXT))

# Appendices TXT target
$(APPENDICES_TXT): $(APPENDICES_PDF)
	$(call pdf_to_txt,$(APPENDICES_PDF),$(APPENDICES_TXT))

# Build all TXT files
.PHONY: txts
txts: $(ALL_PART_TXTS) $(APPENDICES_TXT)
	@echo "$(GREEN)✓ All TXT files generated$(NC)"

# ============================================================================
# HTML AND EPUB GENERATION
# ============================================================================

# Generate HTML from LaTeX
.PHONY: html
html: $(HTML)

$(HTML): $(PDF)
	@echo "$(GREEN)Converting LaTeX to HTML...$(NC)"
	@if ! command -v $(PANDOC) >/dev/null 2>&1; then \
		echo "$(RED)✗ Pandoc not found$(NC)"; \
		echo "$(YELLOW)Install: brew install pandoc$(NC)"; \
		exit 1; \
	fi
	@echo "$(YELLOW)[1/3]$(NC) Preparing build directory..."
	@rm -rf build && mkdir -p build
	@cp *.tex build/ 2>/dev/null || true
	@echo "$(YELLOW)[2/3]$(NC) Preprocessing LaTeX files for pandoc..."
	@./preprocess_for_pandoc.sh
	@echo "$(YELLOW)[3/3]$(NC) Converting to HTML..."
	@cd build && $(PANDOC) $(MAIN).tex -f latex -t html5 --standalone --toc --toc-depth=2 \
		--metadata title='Aliveness: Principles of Telic Systems' \
		--metadata author='Elias Kunnas' \
		--mathjax \
		-o ../$(HTML) || true
	@if [ -f $(HTML) ]; then \
		echo "$(GREEN)✓ HTML created:$(NC) $(HTML)"; \
		echo "  Size: $$(du -h $(HTML) | cut -f1)"; \
	else \
		echo "$(RED)✗ HTML generation failed$(NC)"; \
		echo "$(YELLOW)Check build/ directory for preprocessed files$(NC)"; \
		exit 1; \
	fi

# Generate EPUB from LaTeX
.PHONY: epub
epub: $(EPUB)

$(EPUB): $(MAIN).tex preamble.tex $(wildcard $(TEXDIR)/*.tex)
	@echo "$(GREEN)Converting LaTeX to EPUB...$(NC)"
	@if ! command -v $(PANDOC) >/dev/null 2>&1; then \
		echo "$(RED)✗ Pandoc not found$(NC)"; \
		echo "$(YELLOW)Install: brew install pandoc$(NC)"; \
		exit 1; \
	fi
	@echo "$(YELLOW)[1/3]$(NC) Preparing build directory..."
	@rm -rf build && mkdir -p build
	@cp *.tex build/ 2>/dev/null || true
	@echo "$(YELLOW)[2/3]$(NC) Preprocessing LaTeX files for pandoc..."
	@./preprocess_for_pandoc.sh
	@echo "$(YELLOW)[3/3]$(NC) Converting to EPUB..."
	@cd build && $(PANDOC) $(MAIN).tex -f latex -t epub3 --toc --toc-depth=2 \
		--metadata title='Aliveness: Principles of Telic Systems' \
		--metadata author='Elias Kunnas' \
		--metadata lang=en-US \
		--mathjax \
		-o ../$(EPUB) || true
	@if [ -f $(EPUB) ]; then \
		echo "$(GREEN)✓ EPUB created:$(NC) $(EPUB)"; \
		echo "  Size: $$(du -h $(EPUB) | cut -f1)"; \
	else \
		echo "$(RED)✗ EPUB generation failed$(NC)"; \
		echo "$(YELLOW)Check build/ directory for preprocessed files$(NC)"; \
		exit 1; \
	fi

# ============================================================================

# Convert markdown to LaTeX
.PHONY: convert
convert:
	@echo "Converting markdown to LaTeX..."
	./convert_to_latex.sh

# Clean auxiliary files
.PHONY: clean
clean:
	@echo "Cleaning auxiliary files..."
	@rm -f *.aux *.log *.out *.toc *.lot *.lof *.bbl *.blg *.idx *.ilg *.ind
	@rm -f $(MAIN).pdf $(PART1_TEX).pdf $(PART2_TEX).pdf $(PART3_TEX).pdf $(PART4_TEX).pdf $(PART5_TEX).pdf $(APPENDICES_TEX).pdf
	@rm -f $(PDF) $(ALL_PART_PDFS) $(APPENDICES_PDF) $(HTML) $(EPUB)
	@rm -f $(TXT) $(ALL_PART_TXTS) $(APPENDICES_TXT)
	@rm -rf build
	@echo "$(GREEN)✓ Clean complete$(NC)"

# Clean everything including generated tex files
.PHONY: distclean
distclean: clean
	@echo "Removing generated tex files..."
	@rm -rf $(TEXDIR)
	@echo "$(GREEN)✓ Distribution clean complete$(NC)"

# View PDF
.PHONY: view
view: $(PDF)
	@echo "Opening PDF..."
	@open $(PDF)

# Convert PDF to plain text (for AI analysis, etc.)
TXT = Aliveness__Principles_of_Telic_Systems.txt
.PHONY: txt
txt: $(PDF)
	@echo "$(GREEN)Converting PDF to plain text...$(NC)"
	@pdftotext -layout $(PDF) $(TXT)
	@if [ -f $(TXT) ]; then \
		echo "$(GREEN)✓ Text conversion complete:$(NC) $(TXT)"; \
		echo "  Size: $$(du -h $(TXT) | cut -f1)"; \
		echo "  Words: $$(wc -w < $(TXT) | xargs)"; \
	else \
		echo "$(RED)✗ Conversion failed$(NC)"; \
		echo "$(YELLOW)Trying alternative method (no layout)...$(NC)"; \
		pdftotext $(PDF) $(TXT); \
	fi

# Watch and rebuild on changes (requires fswatch: brew install fswatch)
.PHONY: watch
watch:
	@echo "$(YELLOW)Watching for changes...$(NC)"
	@echo "$(YELLOW)Press Ctrl+C to stop$(NC)"
	@fswatch -o $(TEXDIR)/*.tex $(MAIN).tex preamble.tex | while read num; do \
		echo "$(GREEN)Change detected, rebuilding...$(NC)"; \
		$(MAKE) quick; \
	done

# Show word count (approximate)
.PHONY: wordcount
wordcount:
	@echo "Approximate word count:"
	@texcount -brief -total $(MAIN).tex 2>/dev/null || \
		echo "  Install texcount for accurate counts: brew install texcount"
	@echo "  Rough estimate from tex files:"
	@wc -w $(TEXDIR)/*.tex | tail -1

# Help
.PHONY: help
help:
	@echo "$(GREEN)Aliveness: Principles of Telic Systems - Build System$(NC)"
	@echo ""
	@echo "$(YELLOW)Main Target:$(NC)"
	@echo "  make          - Build ALL formats (PDF + 5 parts + HTML + EPUB)"
	@echo ""
	@echo "$(YELLOW)Individual Format Targets:$(NC)"
	@echo "  make pdf      - Build main PDF only (~824 pages)"
	@echo "  make parts    - Build all 5 part PDFs"
	@echo "  make txts     - Generate all TXT files from parts/appendices"
	@echo "  make html     - Generate HTML version"
	@echo "  make epub     - Generate EPUB ebook"
	@echo "  make quick    - Quick PDF build (1 pass, for testing)"
	@echo ""
	@echo "$(YELLOW)Part PDFs (for reader convenience):$(NC)"
	@echo "  make part1      - Part I: The Diagnosis (Chapters 1-3)"
	@echo "  make part2      - Part II: The Autopsy (Chapters 4-7)"
	@echo "  make part3      - Part III: The Source Code (Chapters 8-12)"
	@echo "  make part4      - Part IV: The Blueprint (Chapters 13-17)"
	@echo "  make part5      - Part V: The Integrated Human (Chapters 18-25)"
	@echo "  make appendices - Appendices Only (All 3 parts A/B/C)"
	@echo ""
	@echo "$(YELLOW)Utility Targets:$(NC)"
	@echo "  make view     - Open main PDF in viewer"
	@echo "  make txt      - Convert PDF to plain text (for AI analysis)"
	@echo "  make convert  - Convert markdown files to LaTeX"
	@echo "  make clean    - Remove all generated files"
	@echo "  make distclean- Remove all generated files + source artifacts"
	@echo "  make watch    - Watch for changes and rebuild"
	@echo "  make wordcount- Show approximate word count"
	@echo "  make help     - Show this help"
	@echo ""
	@echo "$(YELLOW)Prerequisites:$(NC)"
	@echo "  - XeLaTeX (brew install --cask mactex-no-gui)"
	@echo "  - Pandoc (brew install pandoc)"
	@echo "  - Perl (built-in on macOS)"
	@echo ""
	@echo "$(YELLOW)Workflow:$(NC)"
	@echo "  1. Edit markdown files (ch*.md, appendix*.md)"
	@echo "  2. make convert  (convert to LaTeX)"
	@echo "  3. make          (build PDF)"
	@echo "  4. make view     (view result)"
