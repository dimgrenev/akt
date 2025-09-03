import atexit
import io
import os
import stat
import subprocess
import sys
from contextlib import ExitStack
from importlib.resources import as_file, files, is_resource

from ttfautohint._version import __version__
from ttfautohint.errors import TAError
from ttfautohint.options import validate_options, format_kwargs, StemWidthMode


__all__ = ["__version__", "ttfautohint", "TAError", "StemWidthMode", "run"]


# clean up resources on exit
_exit_stack = ExitStack()
atexit.register(_exit_stack.close)

_exe_basename = "ttfautohint"
if sys.platform == "win32":
    _exe_basename += ".exe"
_exe_full_path = None


def _executable_path() -> str:
    global _exe_full_path

    if _exe_full_path is None:
        if is_resource(__name__, _exe_basename):
            _exe_full_path = str(
                _exit_stack.enter_context(
                    as_file(files(__name__).joinpath(_exe_basename))
                )
            )
            # need to chmod +x in case it was extracted from a zip
            if not os.access(_exe_full_path, os.X_OK):
                os.chmod(_exe_full_path, os.stat(_exe_full_path).st_mode | stat.S_IEXEC)
        else:
            import shutil

            _exe_full_path = shutil.which(_exe_basename)
            if _exe_full_path is None:
                raise TAError("ttfautohint executable not found on $PATH")

    return _exe_full_path


def run(args, **kwargs):
    """Run the 'ttfautohint' executable with the list of positional arguments.

    All keyword arguments are forwarded to subprocess.run function.

    The bundled copy of the 'ttfautohint' executable is tried first; if this
    was not included at installation, the version which is on $PATH is used.

    Return:
        subprocess.CompletedProcess object with the following attributes:
        args, returncode, stdout, stderr.
    """
    return subprocess.run([_executable_path()] + list(args), **kwargs)


# TODO: add docstring
def ttfautohint(**kwargs):
    options = validate_options(kwargs)

    in_buffer = options.pop("in_buffer")
    out_file = options.pop("out_file")

    capture_output = True
    stdout = None
    should_close_stdout = False
    if out_file is not None:
        if isinstance(out_file, (str, bytes, os.PathLike)):
            stdout, out_file = open(out_file, "w"), None
            should_close_stdout = True
            capture_output = False
        else:
            try:
                out_file.fileno()
            except io.UnsupportedOperation:
                if not out_file.writable():
                    raise TypeError(f"{out_file} is not writable")
            else:
                stdout, out_file = out_file, None
                capture_output = False

    args = format_kwargs(**options)

    result = run(
        args,
        input=in_buffer,
        capture_output=capture_output,
        stdout=stdout,
    )
    if result.returncode != 0:
        raise TAError(result.returncode, result.stderr)

    output_data = result.stdout

    if output_data and out_file is not None:
        out_file.write(output_data)

    if stdout is not None and should_close_stdout:
        stdout.close()

    return output_data
