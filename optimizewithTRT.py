import torch
import torch_tensorrt
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        return x

model = MyModel().eval().cuda()
input_tensor = torch.randn(1, 3, 224, 224).cuda()

# Convert to TorchScript first
traced_model = torch.jit.trace(model, input_tensor)

# Compile with torch_tensorrt
compiled_model = torch_tensorrt.compile(
    traced_model,
    inputs=[input_tensor],
    enabled_precisions={torch.float32}
)

# Save the compiled model
torch.jit.save(compiled_model, "tensorrt_model.ts")

# Run inference on the compiled model
output1 = compiled_model(input_tensor)
print("First inference completed")

output2 = compiled_model(input_tensor)
print("Second inference completed")

# Load the saved model
loaded_model = torch.jit.load("tensorrt_model.ts")

# Run inference on the loaded model
new_input = torch.randn(1, 3, 224, 224).cuda()
output3 = loaded_model(new_input)
print("Inference completed on the loaded model!")