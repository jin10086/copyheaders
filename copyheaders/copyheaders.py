def headers_raw_to_dict(headers_raw):
    r"""
    Convert raw headers (single multi-line bytestring)
    to a dictionary.

    For example:

    >>> from copyheaders import headers_raw_to_dict
    >>> headers_raw_to_dict(b"Content-type: text/html\n\rAccept: gzip\n\n")   # doctest: +SKIP
    {'Content-type': ['text/html'], 'Accept': ['gzip']}

    Incorrect input:

    >>> headers_raw_to_dict(b"Content-typt gzip\n\n")
    {}
    >>>

    Argument is ``None`` (return ``None``):

    >>> headers_raw_to_dict(None)
    >>>

    """

    if headers_raw is None:
        return None
    headers = headers_raw.splitlines()
    headers_tuples = [header.split(b':', 1) for header in headers]

    result_dict = {}
    for header_item in headers_tuples:
        if not len(header_item) == 2:
            continue

        item_key = header_item[0].strip()
        item_value = header_item[1].strip()
        result_dict[item_key] = item_value

    return result_dict




