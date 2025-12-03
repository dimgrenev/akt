VENV ?= .venv2
VENV_TEST ?= .venv2-test
export PATH := $(abspath $(VENV)/bin):$(PATH)
SOURCES=sources/Akt.glyphs
FAMILY=Akt
DRAWBOT_SCRIPTS=
DRAWBOT_OUTPUT=

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds minimal: outputs a single TTF in fonts/ (no subfolders)"
	@echo "  make test:   Tests the fonts with fontbakery"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the fonts/ directory"
	@echo

build: venv sources/config.yaml $(SOURCES)
	# Полная очистка артефактов, чтобы сборка всегда была «с нуля»
	rm -rf fonts master_ufo instance_ufos sources/.dsbuild
	(for config in sources/config*.yaml; do PATH=$(VENV)/bin:$$PATH $(VENV)/bin/gftools builder $$config; done)
	VARFONT="ofl/akt/variable/Akt[wght].ttf"; \
	 if [ ! -f "$$VARFONT" ]; then VARFONT="ofl/akt/Akt[wght].ttf"; fi; \
	 if [ -f "$$VARFONT" ]; then $(VENV)/bin/python tools/add_avar_identity.py "$$VARFONT"; fi
	 if [ -f "$$VARFONT" ]; then $(VENV)/bin/python tools/fix_naming_fsselection.py "$$VARFONT"; fi
	 if [ -f "$$VARFONT" ]; then $(VENV)/bin/python tools/add_meta.py "$$VARFONT" ofl/akt/METADATA.pb; fi
	 if [ -f "$$VARFONT" ]; then $(VENV)/bin/python tools/fix_names.py "$$VARFONT"; fi
	 if [ -f "$$VARFONT" ]; then $(VENV)/bin/python tools/cleanup_kern_pairpos1.py "$$VARFONT"; fi
	 if [ -f "$$VARFONT" ]; then $(VENV)/bin/python tools/cleanup_gpos_pairpos1.py "$$VARFONT"; fi
	 # Перемещение итогового файла из подкаталога variable и удаление лишних артефактов
	 if [ -f "ofl/akt/variable/Akt[wght].ttf" ]; then mv -f "ofl/akt/variable/Akt[wght].ttf" "ofl/akt/Akt[wght].ttf"; fi
	 if [ -d "ofl/akt/variable" ]; then rmdir "ofl/akt/variable" 2>/dev/null || true; fi
	 if [ -f "ofl/akt/Akt[wght].ttf" ]; then $(VENV)/bin/python tools/fix_names.py "ofl/akt/Akt[wght].ttf"; fi

venv: $(VENV)/touchfile

venv-test: $(VENV_TEST)/touchfile

customize: venv
	$(VENV)/bin/python tools/customize.py

$(VENV)/touchfile: requirements.txt
	test -d $(VENV) || python3 -m venv $(VENV)
	$(VENV)/bin/pip install -Ur requirements.txt
	touch $(VENV)/touchfile

$(VENV_TEST)/touchfile: requirements-test.txt
	test -d $(VENV_TEST) || python3 -m venv $(VENV_TEST)
	$(VENV_TEST)/bin/pip install -Ur requirements-test.txt
	touch $(VENV_TEST)/touchfile

test: venv-test build
	 mkdir -p sources/fontbakery sources/badges
	 TOCHECK=$$( (find fonts -maxdepth 1 -type f \( -name '*.ttf' -o -name '*.otf' \) 2>/dev/null; \
	             find ofl/akt -maxdepth 1 -type f -name '*.ttf' 2>/dev/null) ); \
	 $(VENV_TEST)/bin/fontbakery check-googlefonts -l WARN --full-lists --succinct --badges sources/badges --html sources/fontbakery/fontbakery-report.html --ghmarkdown sources/fontbakery/fontbakery-report.md $$TOCHECK  || echo '::warning file=sources/config.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

proof: venv out/build.stamp
	TOCHECK=$$(find fonts -maxdepth 1 -type f \( -name '*.ttf' -o -name '*.otf' \) 2>/dev/null); $(VENV)/bin/diffenator2 proof $$TOCHECK -o out/proof

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py out/build.stamp
	$(VENV)/bin/python $< --output $@

clean:
	find . -name "*.pyc" -delete


clean-all:
	 rm -rf proof fonts master_ufo instance_ufos
	 rm -rf sources/fontbakery sources/badges sources/.dsbuild
	 rm -rf $(VENV) $(VENV_TEST)
	 find . -name "*.pyc" -delete
	 find . -type d -name "__pycache__" -exec rm -rf {} +

# Helper to rebuild without post-snap
rebuild-nosnap: clean build

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv venv-test
	$(VENV)/bin/pip install --upgrade pip-tools
	$(VENV)/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	$(VENV)/bin/pip-sync requirements.txt
	$(VENV_TEST)/bin/pip install --upgrade pip-tools
	$(VENV_TEST)/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements-test.in
	$(VENV_TEST)/bin/pip-sync requirements-test.txt
	git commit -m "Update requirements" requirements.txt requirements-test.txt
	git push

# ---- Convenience targets for no-snap QA loop ----

# Reports directory for QA logs
REPORT_DIR ?= out/reports

# Analyze source with reports saved to files
analyze-source-report: venv
	mkdir -p $(REPORT_DIR)
	$(VENV)/bin/python tools/auto_snap_nodes.py sources/Akt.glyphs analyze --points-only --threshold 2 | tee $(REPORT_DIR)/analyze-points.txt || true
	$(VENV)/bin/python tools/auto_snap_nodes.py sources/Akt.glyphs analyze --components-only --threshold 2 | tee $(REPORT_DIR)/analyze-components.txt || true

# Backward-compatible alias
analyze-source: analyze-source-report

# Apply source snapping and save log
snap-source-report: venv
	mkdir -p $(REPORT_DIR)
	# Создаст .glyphs.snap_backup и применит снаппинг к узлам и компонентам с порогом 2
	$(VENV)/bin/python tools/auto_snap_nodes.py sources/Akt.glyphs snap --threshold 2 | tee $(REPORT_DIR)/snap-source.txt || true

# Backward-compatible alias
snap-source: snap-source-report

# Per-glyph binary report (baseline)
bin-report-baseline: venv out/build.stamp
	mkdir -p $(REPORT_DIR)
	TOCHECK=fonts/Akt[wght].ttf; \
	[ -f "$$TOCHECK" ] || { echo "fonts/Akt[wght].ttf not found"; exit 1; }; \
	$(VENV)/bin/python tools/snap_outline_points.py --report --threshold 2 $$TOCHECK | tee $(REPORT_DIR)/bin-report-baseline.txt || true

# Per-glyph binary report (post-fix)
bin-report-postfix: venv out/build.stamp
	mkdir -p $(REPORT_DIR)
	TOCHECK=fonts/Akt[wght].ttf; \
	[ -f "$$TOCHECK" ] || { echo "fonts/Akt[wght].ttf not found"; exit 1; }; \
	$(VENV)/bin/python tools/snap_outline_points.py --report --threshold 2 $$TOCHECK | tee $(REPORT_DIR)/bin-report-postfix.txt || true

# Optional backward-compatible alias
bin-report: bin-report-baseline

# FontBakery outline check (baseline)
check-outline-baseline: venv out/build.stamp
	mkdir -p $(REPORT_DIR)
	TOCHECK=fonts/Akt[wght].ttf; \
	[ -f "$$TOCHECK" ] || { echo "fonts/Akt[wght].ttf not found"; exit 1; }; \
	$(VENV)/bin/fontbakery check-googlefonts --full-lists -c com.google.fonts/check/outline_alignment_miss $$TOCHECK | tee $(REPORT_DIR)/outline-baseline.txt || true

# FontBakery outline check (post-fix)
check-outline-postfix: venv out/build.stamp
	mkdir -p $(REPORT_DIR)
	TOCHECK=fonts/Akt[wght].ttf; \
	[ -f "$$TOCHECK" ] || { echo "fonts/Akt[wght].ttf not found"; exit 1; }; \
	$(VENV)/bin/fontbakery check-googlefonts --full-lists -c com.google.fonts/check/outline_alignment_miss $$TOCHECK | tee $(REPORT_DIR)/outline-postfix.txt || true

# Optional backward-compatible alias
check-outline: check-outline-baseline

# Full QA cycle with report artifacts saved
qa-nosnap-report: rebuild-nosnap bin-report-baseline check-outline-baseline analyze-source-report snap-source-report rebuild-nosnap bin-report-postfix check-outline-postfix
	@echo "QA (no post-snap) report cycle completed. See $(REPORT_DIR)"

# Базовая проверка без изменений источника
qa-nosnap-baseline: rebuild-nosnap bin-report-baseline check-outline-baseline
	@echo "Baseline QA (no post-snap, no source snap) завершён"

# Применение фиксов в источнике и повторная проверка
qa-nosnap-fix: analyze-source-report snap-source-report rebuild-nosnap bin-report-postfix check-outline-postfix
	@echo "Post-fix QA (source snap applied, no post-snap) завершён"

# Полный цикл: сначала baseline, затем фиксы и повторная проверка
qa-nosnap: qa-nosnap-baseline qa-nosnap-fix
	@echo "Полный QA (no post-snap) цикл завершён"
