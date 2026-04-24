VENV ?= .venv2
VENV_TEST ?= .venv2-test
REQ_BUILD := $(firstword $(wildcard requirements.txt requirements-test.txt))
VARFONT := fonts/variable/Akt[wght].ttf
SOURCES = sources/Akt.glyphs
FAMILY = Akt
DRAWBOT_SCRIPTS =
DRAWBOT_OUTPUT =
export PATH := $(abspath $(VENV)/bin):$(PATH)

.PHONY: help build venv venv-test test proof images clean clean-all rebuild update-project-template

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the packaged variable TTF at $(VARFONT)"
	@echo "  make test:   Runs FontBakery and refreshes reports in sources/"
	@echo "  make proof:  Creates HTML proof documents in out/proof"
	@echo "  make images: Runs configured specimen scripts, if any"
	@echo

build: venv sources/config.yaml $(SOURCES)
	rm -rf fonts master_ufo instance_ufos sources/.dsbuild
	(for config in sources/config*.yaml; do PATH=$(VENV)/bin:$$PATH $(VENV)/bin/gftools builder $$config; done)
	test -f "$(VARFONT)"
	$(VENV)/bin/python tools/add_avar_identity.py "$(VARFONT)"
	$(VENV)/bin/python tools/add_meta.py "$(VARFONT)" METADATA.pb
	$(VENV)/bin/python tools/fix_names.py "$(VARFONT)"
	$(VENV)/bin/python tools/cleanup_gpos_pairpos1.py "$(VARFONT)"

venv: $(VENV)/touchfile

venv-test: $(VENV_TEST)/touchfile

$(VENV)/touchfile: $(REQ_BUILD)
	test -n "$(REQ_BUILD)"
	test -d $(VENV) || python3 -m venv $(VENV)
	$(VENV)/bin/pip install -Ur $(REQ_BUILD)
	touch $(VENV)/touchfile

$(VENV_TEST)/touchfile: requirements-test.txt
	test -d $(VENV_TEST) || python3 -m venv $(VENV_TEST)
	$(VENV_TEST)/bin/pip install -Ur requirements-test.txt
	touch $(VENV_TEST)/touchfile

test: venv-test build
	mkdir -p sources/fontbakery sources/badges
	TOCHECK="$(VARFONT)"; \
	[ -f "$$TOCHECK" ] || { echo "$$TOCHECK not found"; exit 1; }; \
	$(VENV_TEST)/bin/fontbakery check-googlefonts -l WARN --full-lists --succinct --badges sources/badges --html sources/fontbakery/fontbakery-report.html --ghmarkdown sources/fontbakery/fontbakery-report.md "$$TOCHECK" || echo '::warning file=sources/config.yaml,title=Fontbakery failures::The fontbakery QA check reported errors in your font. Please check the generated report.'

proof: venv build
	TOCHECK="$(VARFONT)"; \
	[ -f "$$TOCHECK" ] || { echo "$$TOCHECK not found"; exit 1; }; \
	$(VENV)/bin/diffenator2 proof "$$TOCHECK" -o out/proof

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build
	$(VENV)/bin/python $< --output $@

clean:
	find . -name "*.pyc" -delete

clean-all:
	rm -rf fonts master_ufo instance_ufos out proof
	rm -rf sources/fontbakery sources/badges sources/.dsbuild
	rm -rf $(VENV) $(VENV_TEST)
	find . -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +

rebuild: clean build

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/
