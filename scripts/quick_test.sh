#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/verify_dataset.py
# Builds 300 train / 100 test samples, then restores full build.
for impl in seq omp; do
  make -C "$impl" clean
  if [ "$impl" = omp ]; then
    make -C "$impl" CFLAGS='-O2 -std=c11 -Wall -Wno-unused-function -fopenmp -DCOUNT_TRAIN=300 -DCOUNT_TEST=100'
  else
    make -C "$impl" CFLAGS='-O2 -std=c11 -Wall -Wno-unused-function -DCOUNT_TRAIN=300 -DCOUNT_TEST=100'
  fi
  if [ "$impl" = omp ]; then OMP_NUM_THREADS=2 "./$impl/lenet5"; else "./$impl/lenet5"; fi
  make -C "$impl" clean
  make -C "$impl"
done
