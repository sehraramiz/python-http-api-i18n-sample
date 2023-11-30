ifndef LANG
override LANG = fa
endif
MSGDIR = locales/$(LANG)/LC_MESSAGES
MSGFILE = locales/$(LANG)/LC_MESSAGES/messages.po
MSGBASE = messages.pot

makemessages:
	find -iname "*.py" | xargs xgettext -L Python --from-code=UTF-8 -o $(MSGBASE)
	sed -i -e 's/CHARSET/UTF-8/g' $(MSGBASE)
	mkdir -p $(MSGDIR)
	- cp -n $(MSGBASE) $(MSGFILE)
	msgmerge --update $(MSGFILE) $(MSGBASE)

compilemessages:
	msgfmt -o $(MSGDIR)/messages.mo $(MSGFILE)
