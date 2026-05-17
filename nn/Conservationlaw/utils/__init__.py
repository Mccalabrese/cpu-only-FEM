"""Useful utils
"""
import torch

# CPU fallback for code paths that call .cuda() unconditionally.
if not torch.cuda.is_available():
	def _cpu_only_cuda(self, *args, **kwargs):
		return self

	torch.Tensor.cuda = _cpu_only_cuda
	torch.nn.Module.cuda = _cpu_only_cuda
	torch.cuda.FloatTensor = torch.FloatTensor
	torch.cuda.LongTensor = torch.LongTensor

from .misc import *
from .logger import *
from .visualize import *
from .eval import *

# progress bar
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "progress"))
# from progress.bar import Bar as Bar