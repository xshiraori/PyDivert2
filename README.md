# PyDivert2

So, PyDivert2 isn't some shiny new project. It's more like a slightly polished version of the original PyDivert because the original author seems to have other priorities right now.

You can visit the original PyDivert repository and learn about its usage here: https://github.com/ffalcinelli/pydivert 

Also there is a great documentation available: https://pythonhosted.org/pydivert/

## Changes

Not much has changed in terms of usage. It's mostly the same old stuff, but I added access to the socket and flow layers, plus their data structures like events, constants, some fixes over parameters etc.

The WinDivert binaries are also updated to their latest version (2.2.2).

If you run into any issues or want to contribute, feel free to do so.

### Installation and example

You can either

* Clone this repo and directly import from it.
or
* Install the original repo with `pip install pydivert` then change the pydivert folder with the one in this repo.

Example.py
```python
from pydivert import WinDivert
from pydivert.consts import *

with WinDivert("true", Layer.SOCKET, 0, Flag.SNIFF | Flag.RECV_ONLY) as w:
    w.set_param(Param.QUEUE_LEN, Constants.PARAM_QUEUE_LENGTH_MAX)
    w.set_param(Param.QUEUE_SIZE, Constants.PARAM_QUEUE_SIZE_MAX)
    w.set_param(Param.QUEUE_TIME, Constants.PARAM_QUEUE_TIME_MAX)

    for packet in w:
        print(packet)

```
