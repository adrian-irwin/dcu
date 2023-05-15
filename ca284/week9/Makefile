
bin = compiled

files = $(wildcard *.c)
finalLocation = $(addprefix $(bin)/, $(basename $(files)))

build: $(bin) $(finalLocation) makefile
	@true

$(bin)/%: %.c
	gcc -o $@ $< -lm

$(bin):
	mkdir -vp $(bin)

clean:
	rm -vf $(finalLocation)

.PHONY:	build clean