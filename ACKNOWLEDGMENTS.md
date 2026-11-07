# Credits and sources

This is a collaborative academic project completed at Lebanese American University (LAU) as part of the Parallel Programming and Multi-Cluster Systems course.

**Project team:** Abdulaziz Al Sayyed, Ibrahim Mabrouki, and Tala Hareb.

The C LeNet-5 implementation uses and adapts pre-existing open-source work:

- **Original serial C LeNet-5 implementation:** [fan-wenjie/LeNet-5](https://github.com/fan-wenjie/LeNet-5), distributed under the MIT license in that repository.
- **Reference OpenMP / CUDA optimization code:** [SnailWalkerYC/LeNet-5_Speed_Up](https://github.com/SnailWalkerYC/LeNet-5_Speed_Up), associated with the 2017 project report by Yu Chen, Yifei Gong, and Guangbo Li. The supplied 2017 archive does not contain a redistribution license; please verify permission before publicly publishing code substantially derived from those implementations.
- **MNIST:** handwritten digit dataset originally created by Yann LeCun, Corinna Cortes, and Christopher Burges. The four IDX files were included in the provided LAU project archive.

This repository preserves the collaborative project's implementation and documents code-review fixes and reproducibility improvements in `docs/notes/maintenance.md`.
