# Torch2TRT

This repository demonstrates how to convert a PyTorch model to TensorRT using the NVIDIA's offficial repo's `torch2trt` library and perform inference with the converted model.

## Conversion Method

- **Clones the torch2trt repository from GitHub and installs required dependencies.**
- **Converts a model to TensorRT using torch2trt().**
- **Runs inference using the converted model.**


## Requirements

1. **Python 3.6+**
2. **PyTorch** - Make sure you have PyTorch installed.
3. **TensorRT** - You will need TensorRT to optimize the model for GPU inference.
4. **CUDA** - Ensure you have CUDA installed for GPU support.

You can install the necessary dependencies by following the instructions below.

## Setup

### 1. Clone the repository:

```bash
git clone https://github.com/NVIDIA-AI-IOT/torch2trt
```
### 2. Install the dependencies:

```bash
cd torch2trt
pip install nvidia-pyindex
pip install nvidia-tensorrt
```
### 3. Build and install torch2trt:

```bash
python setup.py install
```

# Torch-TensorRT

Torch-TensorRT brings the power of TensorRT to PyTorch. Accelerate inference latency by up to 5x compared to eager execution in just one line of code.

## Conversion Method

- **Converts a PyTorch model to TorchScript using torch.jit.trace.**
- **Then compiles it to TensorRT using torch_tensorrt.compile().**
- **Saves and reloads the compiled model using torch.jit.save() and torch.jit.load().**

## Dependencies

These are the following dependencies used to verify the testcases. Torch-TensorRT can work with other versions, but the tests are not guaranteed to pass.

1. **Bazel 6.3.2**
2. **Libtorch 2.7.0.dev (latest nightly) (built with CUDA 12.8)**
3. **CUDA 12.8**
4. **TensorRT 10.9.0.43**

## Installation

### 1. Stable versions of Torch-TensorRT are published on PyPI

```bash
pip install torch-tensorrt
```
### 2. Nightly versions of Torch-TensorRT are published on the PyTorch package index

```bash
pip install --pre torch-tensorrt --index-url https://download.pytorch.org/whl/nightly/cu124
```
### 3. Build and install torch2trt:

```bash
python setup.py install
```
