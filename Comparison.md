# Torch2TRT vs Torch-TensorRT

This document provides a comparative analysis of Torch2TRT and Torch-TensorRT, both of which are used to convert PyTorch models to TensorRT for optimized inference. Torch2TRT is part of NVIDIA's official repository, while Torch-TensorRT is maintained as an official PyTorch repository.

## Overview

### Torch2TRT
Torch2TRT is a lightweight PyTorch to TensorRT converter that enables model acceleration by converting a PyTorch model to TensorRT using the `torch2trt()` API.

### Torch-TensorRT
Torch-TensorRT is an official NVIDIA library that integrates TensorRT into PyTorch, providing seamless conversion of models using `torch_tensorrt.compile()`.

## Conversion Method

### Torch2TRT
* **Clones the torch2trt repository and installs dependencies.**
* **Converts a PyTorch model to TensorRT using `torch2trt()` API.**
* **Performs inference using the converted model.**

### Torch-TensorRT
* **Converts a PyTorch model to TorchScript using `torch.jit.trace()`.**
* **Compiles it to TensorRT using `torch_tensorrt.compile()`.**
* **Saves and reloads the compiled model using `torch.jit.save()` and `torch.jit.load()`.**

## Dependencies

### Torch2TRT
1. **Python 3.6+**
2. **PyTorch** (Ensure it is installed)
3. **TensorRT** (Required for GPU inference optimization)
4. **CUDA** (Required for GPU acceleration)

### Torch-TensorRT
1. **Bazel 6.3.2**
2. **Libtorch 2.7.0.dev (Latest Nightly) (Built with CUDA 12.8)**
3. **CUDA 12.8**
4. **TensorRT 10.9.0.43**

## Installation

### Torch2TRT
1. Clone the repository:

```bash
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
```

2. Install dependencies:

```bash
cd torch2trt
pip install nvidia-pyindex
pip install nvidia-tensorrt
```

3. Build and install Torch2TRT:

```bash
python setup.py install
```

### Torch-TensorRT
1. Install stable version from PyPI:

```bash
pip install torch-tensorrt
```

2. Install nightly version from PyTorch package index:

```bash
pip install --pre torch-tensorrt --index-url https://download.pytorch.org/whl/nightly/cu124
```

## Key Differences

| Feature | Torch2TRT | Torch-TensorRT |
|---------|-----------|---------------|
| **Integration** | Standalone library | Official NVIDIA PyTorch integration |
| **Conversion API** | `torch2trt()` | `torch_tensorrt.compile()` |
| **Requires TorchScript?** | ❌ No | ✅ Yes |
| **Model Type** | PyTorch Module | TorchScript Module |
| **Installation Complexity** | Medium (Requires manual cloning) | Easy (PyPI package) |
| **Performance Optimization** | Good | Better (Deeper integration with PyTorch) |
| **Support & Updates** | Community-maintained | Officially supported by NVIDIA |
| **Inference Speedup** | Moderate | Higher due to deeper TensorRT integration |

## Conclusion

Both Torch2TRT and Torch-TensorRT help in optimizing PyTorch models for deployment using TensorRT. However, **Torch-TensorRT** is better suited for production applications due to its official NVIDIA support, better performance, and PyTorch-native integration. **Torch2TRT**, on the other hand, is a lightweight alternative that is easier to use for quick model conversion without requiring TorchScript.

Choose the right tool based on your specific needs and deployment requirements!
