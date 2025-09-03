def ensure_binary(s, encoding="ascii", errors="strict"):
    if isinstance(s, str):
        return s.encode(encoding, errors)
    elif isinstance(s, bytes):
        return s
    else:
        raise TypeError("not expecting type '%s'" % type(s))


def ensure_text(s, encoding="ascii", errors="strict"):
    if isinstance(s, bytes):
        return s.decode(encoding, errors)
    elif isinstance(s, str):
        return s
    else:
        raise TypeError("not expecting type '%s'" % type(s))
