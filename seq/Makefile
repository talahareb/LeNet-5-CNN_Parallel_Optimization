CC ?= gcc
# For MPI, override make CC=mpicc if environment exports CC=cc.
CFLAGS ?= -O2 -std=c11 -Wall -Wno-unused-function
CFLAGS += 
LDFLAGS +=  -lm
TARGET = lenet5

all: $(TARGET)
$(TARGET): main.o lenet.o
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)
main.o: main.c lenet.h
	$(CC) $(CFLAGS) -c -o $@ $<
lenet.o: lenet.c lenet.h
	$(CC) $(CFLAGS) -c -o $@ $<
clean:
	rm -f main.o lenet.o $(TARGET)
.PHONY: all clean
