#
#  Copyright (C) 2003-2020 by Ihor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import base64
import math
import struct
import time
import typing as tp
import uuid


def generate_id() -> str:
    """Generates numeric id based on UNIX time like '159490432636592'

    :return: (str) numeric id
    """
    time.sleep(0.001)
    return str(int(time.time() * 100000))


def generate_base64_id() -> str:
    """Generates base64 encoded id based on UNIX time like 'MTU5NDkwNDM0NDgyMTYw'

    :return: (str) base64 encoded id
    """
    time.sleep(0.001)
    return base64.b64encode(generate_id().encode()).decode()


def generate_guid() -> str:
    """Generates classic GUID like '514a70a4-c764-11ea-8364-28f10e13a705'

    :return: (str) GUID string
    """
    time.sleep(0.001)
    return str(uuid.uuid1())


def byte2py_int(data: bytes) -> int:
    """Converts byte to Python int value.

    :param data: (bytes) 1-character bytes
    :return: (int) integer value of byte
    """
    return struct.unpack('B', data)[0]


def py_int2byte(val: int) -> bytes:
    """Converts Python int value to byte.

    :param val: (int) integer value (0-255)
    :return: (bytes) 1-character bytes
    """
    return struct.pack('B', val)


def word2py_int(data: bytes, be: bool = False) -> int:
    """Converts word of bytes to Python int value.

    :param data: (bytes) 2-character bytes
    :param be: big endian flag
    :return: (int) integer value of two bytes (0-65535)
    """
    sig = '>H' if be else '<H'
    return struct.unpack(sig, data)[0]


def signed_word2py_int(data: bytes, be: bool = False) -> int:
    """Converts signed word of bytes to Python int value.

    :param data: (bytes) 2-character bytes
    :param be: big endian flag
    :return (int) signed integer value of two bytes (−32,768 - 32,767)
    """
    sig = '>h' if be else '<h'
    return struct.unpack(sig, data)[0]


def py_int2word(val: int, be: bool = False) -> bytes:
    """Converts Python int value to word of bytes.

    :param val: (int) integer value (0-65535)
    :param be: big endian flag
    :return: (bytes) 2-character bytes
    """
    sig = '>H' if be else '<H'
    return struct.pack(sig, val)


def py_int2signed_word(val: int, be: bool = False) -> bytes:
    """Converts Python signed int value to word of bytes.

    :param val: (int) signed integer value of two bytes (-32768 - 32767)
    :param be: big endian flag
    :return: (bytes) 2-character bytes
    """
    sig = '>h' if be else '<h'
    return struct.pack(sig, val)


def dword2py_int(data: bytes, be: bool = False) -> int:
    """Converts double word of bytes to Python int value.

    :param data: (bytes) 4-character bytes
    :param be: big endian flag
    :return: (int) integer value of four bytes
    """
    sig = '>I' if be else '<I'
    return struct.unpack(sig, data)[0]


def signed_dword2py_int(data: bytes, be: bool = False) -> int:
    """Converts signed double word of bytes to Python int value.

    :param data: (bytes) 4-character bytes
    :param be: big endian flag
    :return: (int) signed integer value of four bytes
    """
    sig = '>i' if be else '<i'
    return struct.unpack(sig, data)[0]


def py_int2dword(val: int, be: bool = False) -> bytes:
    """Converts Python int value to double word of bytes.

    :param val: (int) integer value of four bytes
    :param be: big endian flag
    :return: (bytes) 4-character bytes
    """
    sig = '>I' if be else '<I'
    return struct.pack(sig, val)


def py_int2signed_dword(val: int, be: bool = False) -> bytes:
    """Converts Python int value to signed double word of bytes.

    :param val: (int) signed integer value of four bytes
    :param be: big endian flag
    :return: (bytes) 4-character bytes
    """
    sig = '>i' if be else '<i'
    return struct.pack(sig, val)


def pair_dword2py_int(data: bytes) -> tp.Tuple[int]:
    """Converts pair of double words (8 bytes) to pair of Python int values.

    :param data: (bytes) 8-character bytes
    :return: (tuple) two integer values
    """
    return struct.unpack('<2L', data)


def py_float2float(val: float, be: bool = False) -> bytes:
    """Converts Python float to 4 bytes (double)

    :param val: (float) float value
    :param be: big endian flag
    :return: (bytes) 4-character bytes
    """
    sig = '>f' if be else '<f'
    return struct.pack(sig, val)


def float2py_float(val: bytes, be: bool = False) -> float:
    """Converts 4 bytes (double) to Python float

    :param val:  (bytes) 4-character bytes
    :param be: big endian flag
    :return: (float) float value
    """
    sig = '>f' if be else '<f'
    return struct.unpack(sig, val)[0]


def double2py_float(data: bytes, be: bool = False) -> float:
    """Converts 8 bytes to Python float value.

    :param data: (bytes) 8-character bytes
    :param be: big endian flag
    :return: (float) float value
    """
    sig = '>d' if be else '<d'
    return struct.unpack(sig, data)[0]


def py_float2double(val: float, be: bool = False) -> bytes:
    """Converts Python float to 8 bytes (double)

    :param val: (float) float value
    :param be: big endian flag
    :return: (bytes) 8-character bytes
    """
    sig = '>d' if be else '<d'
    return struct.pack(sig, val)


def get_chunk_size(size_field: bytes) -> int:
    """Converts RIFF chunk size (4-bytes) into integer value
    taking in account even/odd value type

    :param size_field: (bytes) 4-bytes chunk size
    :return: (int) chunk size
    """
    size = dword2py_int(size_field)
    return size if size % 2 == 0 else size + 1


def uint16_be(chunk: bytes) -> int:
    """Converts 2 bytes to unsigned int (big endian)

    :param chunk: (bytes) 2-character bytes
    :return: (int) integer value
    """
    return word2py_int(chunk, True)


def dib_to_bmp(dib: bytes) -> bytes:
    """Reconstructs BMP bitmap file header for DIB

    :param dib: (bytes) device-independent bitmap string
    :return: (bytes) BMP string
    """
    offset = dib_header_size = struct.unpack('<I', dib[:4])[0]
    if dib_header_size == 12:
        bitsperpixel = struct.unpack('<h', dib[10:12])[0]
        if not bitsperpixel > 8:
            offset += math.pow(2, bitsperpixel) * 3
    else:
        bitsperpixel = struct.unpack('<h', dib[14:16])[0]
        colorsnum = struct.unpack('<I', dib[32:36])[0]
        if bitsperpixel > 8:
            offset += colorsnum * 3
        else:
            offset += math.pow(2, bitsperpixel) * 3
    offset = math.ceil(offset / 4.0) * 4

    pixel_offset = struct.pack('<I', 14 + offset)
    file_size = struct.pack('<I', 14 + len(dib))
    return b'BM' + file_size + b'\x00\x00\x00\x00' + pixel_offset + dib


def bmp_to_dib(bmp: bytes) -> bytes:
    """Extracts DIB from BMP

    :param bmp: BMP string
    :return: DIB string
    """
    return bmp[14:]
