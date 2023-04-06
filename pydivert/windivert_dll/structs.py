# -*- coding: utf-8 -*-
# Copyright (C) 2016  Fabio Falcinelli, Maximilian Hils
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import ctypes


class WINDIVERT_DATA_NETWORK(ctypes.Structure):
    _fields_ = [
        ("IfIdx", ctypes.c_uint32),
        ("SubIfIdx", ctypes.c_uint32),
    ]

# WINDIVERT_DATA_FLOW
class WINDIVERT_DATA_FLOW(ctypes.Structure):
    _fields_ = [
        ("Endpoint", ctypes.c_uint64),
        ("ParentEndpoint", ctypes.c_uint64),
        ("ProcessId", ctypes.c_uint32),
        ("LocalAddr", ctypes.c_uint32 * 4),
        ("RemoteAddr", ctypes.c_uint32 * 4),
        ("LocalPort", ctypes.c_uint16),
        ("RemotePort", ctypes.c_uint16),
        ("Protocol", ctypes.c_uint8),
    ]

# WINDIVERT_DATA_SOCKET
class WINDIVERT_DATA_SOCKET(ctypes.Structure):
    _fields_ = [
        ("Endpoint", ctypes.c_uint64),
        ("ParentEndpoint", ctypes.c_uint64),
        ("ProcessId", ctypes.c_uint32),
        ("LocalAddr", ctypes.c_uint32 * 4),
        ("RemoteAddr", ctypes.c_uint32 * 4),
        ("LocalPort", ctypes.c_uint16),
        ("RemotePort", ctypes.c_uint16),
        ("Protocol", ctypes.c_uint8),
    ]

# WINDIVERT_LAYER
class WINDIVERT_LAYER(ctypes.c_uint32):
    pass

# WINDIVERT_DATA_REFLECT
class WINDIVERT_DATA_REFLECT(ctypes.Structure):
    _fields_ = [
        ("Timestamp", ctypes.c_int64),
        ("ProcessId", ctypes.c_uint32),
        ("Layer", WINDIVERT_LAYER),
        ("Flags", ctypes.c_uint64),
        ("Priority", ctypes.c_int16),
    ]

# Union for WINDIVERT_ADDRESS
class WINDIVERT_DATA_UNION(ctypes.Union):
    _fields_ = [
        ("Network", WINDIVERT_DATA_NETWORK),
        ("Flow", WINDIVERT_DATA_FLOW),
        ("Socket", WINDIVERT_DATA_SOCKET),
        ("Reflect", WINDIVERT_DATA_REFLECT),
    ]

# WINDIVERT_ADDRESS
class WinDivertAddress(ctypes.Structure):
    def __repr__(self) -> str:
        values = ", ".join(f"{name}={value}"for name, value in self._asdict().items())
        return f"<{self.__class__.__name__}: {values}>"

    def _asdict(self) -> dict:
        return {field[0]: getattr(self, field[0]) for field in self._fields_}


    _fields_ = [
        ("Timestamp", ctypes.c_int64),
        ("Layer", ctypes.c_uint64, 8),
        ("Event", ctypes.c_uint64, 8),
        ("Sniffed", ctypes.c_uint64, 1),
        ("Outbound", ctypes.c_uint64, 1),
        ("Loopback", ctypes.c_uint64, 1),
        ("Impostor", ctypes.c_uint64, 1),
        ("IPv6", ctypes.c_uint64, 1),
        ("IPChecksum", ctypes.c_uint64, 1),
        ("TCPChecksum", ctypes.c_uint64, 1),
        ("UDPChecksum", ctypes.c_uint64, 1),
        ("Data", WINDIVERT_DATA_UNION),
    ]