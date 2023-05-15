
bin = compiled

# files = $(wildcard *.c)
files = $(wildcard *.java)
finalLocation = $(addprefix $(bin)/, $(addsuffix .class,$(basename $(files) ) ) )

build: $(bin) $(finalLocation) makefile
	@true

# $(bin)/%: %.c
# 	gcc -o $@ $< -lm -Wall -Werror

$(bin)/%.class: %.java
	javac -d $(bin)/ $<

$(bin):
	mkdir -vp $(bin)

clean:
	rm -vf $(finalLocation)

makefile:
	@cp "../makefiles/outer_Makefile.mk" "Makefile"
	@cd $(bin) && cp "../../makefiles/compiled_Makefile.mk" "Makefile"

.PHONY:	build clean makefile