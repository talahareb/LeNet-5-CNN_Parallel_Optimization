# MNIST dataset (download separately)

The project uses the original MNIST training/test IDX files (60,000 training and 10,000 test images). To keep the GitHub upload lightweight, the large binary dataset is **not included** in this repository.

From the repository root, run:

```bash
python3 scripts/download_mnist.py
python3 scripts/verify_dataset.py
```

The downloader retrieves and decompresses the four files into `data/mnist/`, and checks their SHA-256 hashes. The source is the CVDF MNIST mirror: https://github.com/cvdfoundation/mnist.

The four raw files are gitignored, so they stay on your local machine. If you have an offline copy of the MNIST data bundle, extract the archive at the repository root instead; it contains the same `data/mnist/` paths.
