NVCC ?= nvcc
NVFLAGS ?= -O2
TARGET = lenet5
all: $(TARGET)
$(TARGET): lenet.cu lenet.h
	$(NVCC) $(NVFLAGS) -o $@ lenet.cu
clean:
	rm -f $(TARGET)
.PHONY: all clean
