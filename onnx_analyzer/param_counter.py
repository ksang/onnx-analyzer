import onnx
import logging
import numpy as np
from onnx import numpy_helper

def count_param(model: onnx.ModelProto) -> int:
    onnx_weights = model.graph.initializer
    params = 0

    for onnx_w in onnx_weights:
        try:
            weight = numpy_helper.to_array(onnx_w)
            params += np.prod(weight.shape)
        except Exception as e:
            logging.warn("error calculating weight param: {}".format(e))

    return params