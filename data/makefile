ICT = ict.py
WB = indicator-workbook.xlsx
META = meta.yaml
TEMPLATE = mdMemo.latex
PC = python3
OUTPUT = indicator-categories.pdf
TE = lualatex
MDC = pandoc

pdf:
	$(PC) $(ICT) | $(MDC) --output=$(OUTPUT) --pdf-engine=$(TE) --metadata-file=$(META) --template=$(TEMPLATE)

clean: 
	rm $(wildcard *.pdf)