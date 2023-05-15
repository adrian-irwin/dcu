
bin = compiled

build: $(bin) makefile
	@true

$(bin):
	mkdir -vp $(bin)

makefile:
	@cp ~/makefiles/outer_Makefile.mk Makefile
	@cd $(bin) && cp ~/makefiles/compiled_Makefile.mk Makefile

.PHONY:	build makefile

