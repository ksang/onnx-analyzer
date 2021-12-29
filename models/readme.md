## benchmarks
Below onnx graphs are named in format `<model_name>_<source>_<input_shape>.onnx`
They are exported with pretrained parameters and onnx opset 11

|Task | File      | Model | Comment |
| ----------- | ----------- | ----------- | ---------- |
| 2D detection/segmentation |detection.maskrcnn_resnet50_fpn_torchvision_3x720x1280.onnx | Mask R-CNN with resnet50 backbone and FPN | from torchvsion implementation |
| |yolov5l_pytorch_hub_640.onnx | YOLOv5 large  | from PyTorch Hub |
| |unet_3x720x1280.onnx | UNet  | from official PyTorch implementation |
| 3D Object detection | | Pointpillars | no CUDA env, pending for export |
| Traffic sign | detection.ssdlite320_mobilenet_v3_large_torchvision_3x320x320.onnx | SSDlite with MobileNetV3 Large backbone | from torchvsion implementation |
| | ssd_mobilenet_v1_10.onnx | SSD with MobileNetV1 backbone | from onnx model zoo, opset 10 |
| Feature fusion | mobilebert_squad11_int8_qdq_89.4f1.onnx | mobilebert | use NLP QA pretrained model |
| | transformer_512dim_8heads_6enc_6dec.onnx | pure multihead transformer | without pretrained parameters |
| other | resnet50_torchvision_3x720x1280.onnx | pure resnet50 for classification | from torchvsion implementation |
