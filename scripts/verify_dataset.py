#!/usr/bin/env python3
"""Check MNIST IDX headers and record counts (standard library only)."""
from pathlib import Path
import struct
root = Path(__file__).resolve().parents[1] / 'data/mnist'
for split, count in [('train',60000),('t10k',10000)]:
    for kind, expected_magic in [('images',2051),('labels',2049)]:
        suffix = 'idx3-ubyte' if kind == 'images' else 'idx1-ubyte'
        path = root / f'{split}-{kind}-{suffix}'
        with path.open('rb') as f:
            magic, num = struct.unpack('>II',f.read(8))
            assert magic==expected_magic and num==count,(path,magic,num)
            if kind=='images':
                rows,cols=struct.unpack('>II',f.read(8))
                assert (rows,cols)==(28,28)
                expected_bytes=16+num*rows*cols
            else: expected_bytes=8+num
        assert path.stat().st_size==expected_bytes,(path,expected_bytes)
        print(f'OK {path.name}: {num} records')
