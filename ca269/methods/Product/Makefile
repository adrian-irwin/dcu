
bin = compiled

cSource = $(wildcard *.c)
cFinal = $(addprefix $(bin)/, $(basename $(cSource)))
javaSource = $(wildcard *.java)
javaFinal = $(addprefix $(bin)/, $(addsuffix .class,$(basename $(javaSource))))

build: $(bin) $(cFinal) $(javaFinal)
	@true

$(bin)/%: %.c
	gcc -o $@ $< -lm -Wall -Werror

$(bin)/%.class: %.java
	javac -d $(bin)/ $<

$(bin):
	mkdir -vp $(bin)

clean:
	rm -vf $(cFinal)
	rm -vf $(javaFinal)

.PHONY:	build clean