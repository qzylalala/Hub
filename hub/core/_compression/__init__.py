import sys
import struct


if sys.byteorder == "little":
    NATIVE_INT32 = "<i4"
    NATIVE_FLOAT32 = "<f4"
else:
    NATIVE_INT32 = ">i4"
    NATIVE_FLOAT32 = ">f4"

STRUCT_HHB = struct.Struct(">HHB")
STRUCT_II = struct.Struct(">ii")


from .image.jpeg import JPEG
from .image.png import PNG