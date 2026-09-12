TEX_SRC = paper.tex
PDF_OUT = paper.pdf
TEMP = paper.aux paper.log paper.toc paper.out

all: $(PDF_OUT)

$(PDF_OUT): $(TEX_SRC)
	pdflatex $(TEX_SRC)

clean:
	rm -f $(PDF_OUT) $(TEMP)

.PHONY: clean
