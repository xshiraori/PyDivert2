from pydivert import WinDivert
from pydivert.consts import *

with WinDivert("true", Layer.SOCKET, 0, Flag.SNIFF | Flag.RECV_ONLY) as w:
    w.set_param(Param.QUEUE_LEN, Constants.PARAM_QUEUE_LENGTH_MAX)
    w.set_param(Param.QUEUE_SIZE, Constants.PARAM_QUEUE_SIZE_MAX)
    w.set_param(Param.QUEUE_TIME, Constants.PARAM_QUEUE_TIME_MAX)

    for packet in w:
        print(packet)