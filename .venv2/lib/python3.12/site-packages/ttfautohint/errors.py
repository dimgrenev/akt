class TAError(Exception):
    def __init__(self, rv, error_string):
        self.rv = int(rv)
        self.error_string = error_string.decode("utf-8", errors="replace")

    def __str__(self):
        error = self.rv
        error_string = self.error_string
        s = "0x%02X" % error
        if error_string:
            s += ": %s" % error_string
        return s
