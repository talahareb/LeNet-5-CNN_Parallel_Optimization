# Reproducibility and maintenance notes

The source files originate in the LAU team project. Changes made when preparing this repository:

- Collected the identical 4 MNIST IDX files, repeated under every implementation in the original ZIP, into one `data/mnist/` directory.
- Replaced hard-coded per-folder dataset paths with project-root paths for a consistent way to run the program.
- Simplified GNU Makefiles to remove nonessential `cppunit` link dependencies.
- Corrected sequential/OpenMP/MPI batch-loop bounds to include the final partial batch.
- Corrected MPI training/test scatter to use `MPI_Scatterv` so unequal partition sizes do not discard examples. Removed the redundant broadcast of all dataset bytes.
- Removed an unsynchronized OpenMP progress counter from the multi-threaded test loop.
- Exit safely when required dataset files are missing instead of using freed buffers.
- Guard against division by zero when normalizing a constant-value image.
- Added a header validation tool and configurable compile-time sample limits to support quick smoke checks.

## Benchmark validity

The original 2024 report contains inconsistent MPI timings and speedup summaries. Those historical results have not been reproduced here and are not represented as verified measurements. There is no new CUDA/GPU or multi-process MPI benchmark in this distribution. Please record hardware, compiler, threads/ranks, data counts, test accuracy, and wall-clock timings before presenting new speedups.

For example, the report's MPI section lists 12.316 s for 60,000-image training, while its later summary lists 17.8024 s while attaching the same 9.03× speedup. Those figures cannot all describe the same run.

## Running context

All commands in the main README execute from the *repository root*. Do not launch `./lenet5` from inside an implementation folder, as dataset paths are relative to the project root.
