
FDMHOST=root@prajna
FDMROOT=/data/software/fdm

FDMDST=$(shell lsb_release -i | cut -d ':' -f 2 | sed -e 's/[[:space:]]//' | tr 'A-Z' 'a-z' )
FDMREL=$(shell lsb_release -r | cut -d ':' -f 2 | sed -e 's/[[:space:]]//' | cut -d. -f1 )
FDMDIR=$(FDMROOT)/$(FDMDST)-$(FDMREL)


help:
	@echo "Make targets:"
	@grep -e '^[^[:space:]]*:' Makefile | \
	grep -v '^\.' | \
	sed -e 's/:.*//' | \
	sort | uniq | \
	awk '{ print " " $$1 }'
	@echo

distrib-info:
	@echo Distribution to $(FDMHOST):$(FDMDIR)/

distrib:
	rsync -avzCP --exclude '.?*' RPMS/ $(FDMHOST):$(FDMDIR)/
	ssh $(FDMHOST) "createrepo $(FDMDIR)"

clean-all: clean-build clean-source clean-distrib

clean-build:
	rm -rf BUILD/* TMP/* BUILDROOT/*

clean-source:
	rm -rf SOURCES/*

clean-distrib:
	rm -rf RPMS/*/*.rpm

get-sources:
	grep Source SPECS/tesseract.spec | sed -e 's/%{name}/tesseract-ocr/' -e 's/%{version}/3.02/' | awk ' { print $2 }' | xargs wget -P SOURCES

 
