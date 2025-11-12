#cython: language_level=3
#distutils: define_macros=CYTHON_TRACE_NOGIL=1

from .parser cimport (
    ParseInfo,
    line_number_strings as _line_number_strings,
    advance_to_non_space as _advance_to_non_space,
    get_slashed_char as _get_slashed_char,
    parse_unquoted_plist_string as _parse_unquoted_plist_string,
    parse_plist_string as _parse_plist_string,
)
from .util cimport (
    tounicode,
    is_valid_unquoted_string_char as _is_valid_unquoted_string_char,
)
from .writer cimport string_needs_quotes
from cpython.mem cimport PyMem_Free
from cpython.unicode cimport (
    PyUnicode_AsUCS4Copy, PyUnicode_GET_LENGTH,
)


cdef class ParseContext:

    cdef unicode s
    cdef ParseInfo pi
    cdef Py_UCS4 *buf
    cdef object dict_type

    def __cinit__(
        self,
        string,
        Py_ssize_t offset=0,
        dict_type=dict,
        bint use_numbers=False
    ):
        self.s = tounicode(string)
        cdef Py_ssize_t length = PyUnicode_GET_LENGTH(self.s)
        self.buf = PyUnicode_AsUCS4Copy(self.s)
        if not self.buf:
            raise MemoryError()
        self.dict_type = dict_type
        self.pi = ParseInfo(
            begin=self.buf,
            curr=self.buf + offset,
            end=self.buf + length,
            dict_type=<void*>dict_type,
            use_numbers=use_numbers,
        )

    def __dealloc__(self):
        PyMem_Free(self.buf)


def is_valid_unquoted_string_char(Py_UCS4 c):
    return _is_valid_unquoted_string_char(c)


def line_number_strings(s, offset=0):
    cdef ParseContext ctx = ParseContext(s, offset)
    return _line_number_strings(&ctx.pi)


def advance_to_non_space(s, offset=0):
    cdef ParseContext ctx = ParseContext(s, offset)
    eof = not _advance_to_non_space(&ctx.pi)
    return None if eof else s[ctx.pi.curr - ctx.pi.begin]


def get_slashed_char(s, offset=0):
    cdef ParseContext ctx = ParseContext(s, offset)
    return _get_slashed_char(&ctx.pi)


def parse_unquoted_plist_string(s):
    cdef ParseContext ctx = ParseContext(s)
    return _parse_unquoted_plist_string(&ctx.pi)


def parse_plist_string(s, required=True):
    cdef ParseContext ctx = ParseContext(s)
    return _parse_plist_string(&ctx.pi, required=required)
