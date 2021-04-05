ICT = ict.py
WB = ../indicator-workbook.xlsx
META = meta.yaml
TEMPLATE = mdMemo.latex
PC = python3
OUTPUT = indicator-categories.pdf
MANOUT = indicators-manual.pdf
MD = indicator-categories.md
TE = lualatex
MDC = pandoc
MANUAL = indicators-manual.md

.PHONY : all

all : pdf manual

manual : $(MANOUT)

pdf : $(OUTPUT)

md : $(MD)

$(OUTPUT) : $(TEMPLATE) $(META) $(MD)
	$(MDC) $(MD) --output=$(OUTPUT) --pdf-engine=$(TE) --metadata-file=$(META) --template=$(TEMPLATE)

$(MANOUT) : $(MANUAL) $(META) $(TEMPLATE)
	$(MDC) $(MANUAL) --output=$(MANOUT) --pdf-engine=$(TE) --metadata-file=$(META) --template=$(TEMPLATE)

$(MD) : $(WB) $(ICT)
	$(PC) $(ICT) > $(MD)

.PHONY : clean

clean: 
	rm $(OUTPUT) $(MD) $(MANOUT)