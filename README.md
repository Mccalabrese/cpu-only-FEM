## Environment
* [PyTorch 1.0](http://pytorch.org/)

## CPU-only quickstart (recommended for laptops)

These scripts run on CPU. The code uses `.cuda()` in many places, so this repo includes a small CPU fallback and a few optional flags to keep CPU runs short.

### 1) Create a Python 3.12 environment

PyTorch does not currently ship wheels for Python 3.14. Use Python 3.12.

macOS/Linux:
```
python3.12 -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

Windows (PowerShell):
```
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install numpy scipy matplotlib
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### 2) Run from the example folder

Always `cd` into the example folder before running. This fixes common import errors like `computational_tree.py` not found.

#### FEX examples

Poisson (smoke test):
```
cd fex/Poisson
python controller_poisson.py --epoch 1 --domainbs 10 --bdbs 10 --finetune 0 --eval_iters 0
```

Conservation law (smoke test):
```
cd fex/Conservationlaw
python controller_conservative.py --epoch 1 --domainbs 10 --bdbs 10 --finetune 0 --eval_iters 0
```

Schrodinger (smoke test):
```
cd fex/Schrodinger
python controller_cubic_sh_firstdeflation_thenintegral.py --epoch 1 --domainbs 10 --intbs 10 --integral_iters 0 --finetune 0 --eval_iters 0
```

#### NN examples

Poisson (smoke test):
```
cd nn/Poisson
python train.py --iters 1 --trainbs 5 --bdbs 10 --eval_iters 0
```

Conservation law (smoke test):
```
cd nn/Conservationlaw
python train.py --iters 1 --trainbs 5 --bdbs 10 --eval_iters 0
```

Schrodinger (smoke test):
```
cd nn/Schrodinger
python train_integral.py --iters 1 --trainbs 5 --intbs 10 --integral_iters 0 --eval_iters 0
```

### Notes

- Full runs are slow on CPU. Start with the smoke tests above, then increase `--epoch` or `--iters` and batch sizes as needed.
- If you see a warning about `is not` with an int, it is harmless.