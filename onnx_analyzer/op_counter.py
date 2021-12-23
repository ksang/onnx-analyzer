import onnx
import operator
from collections import defaultdict, OrderedDict
def count_op(model: onnx.ModelProto, calculate_macs=False) -> tuple[dict, dict]:
    nodes = model.graph.node
    ops = defaultdict(lambda: 0)
    for n in nodes:
        ops[n.op_type] += 1
    return OrderedDict(sorted(ops.items(), key=operator.itemgetter(1), reverse=True)), {}