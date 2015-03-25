import re

CHAR_ESCAPE = {
    u'&': u'\\&',
    u'%': u'\\%',
    u'$': u'\\$',
    u'#': u'\\#',
    u'_': u'\\_',
    u'{': u'\\{',
    u'}': u'\\}',
    u'~': u'\\textasciitilde{}',
    u'^': u'\\textasciicircum{}',
    u'\\': u'\\textbackslash{}',

    # these may be optional:
    u'<': u'\\textless{}',
    u'>': u'\\textgreater{}',
    u'|': u'\\textbar{}',
    u'"': u'\\textquoteddbl{}',
}


def _sub_tbl(tbl):
    return r'|'.join(re.escape(k) for k in sorted(tbl.keys()))


ESCAPE_RE = re.compile(r'\n+|' + _sub_tbl(CHAR_ESCAPE))


def escape(s, fold_newlines=True):
    def sub(m):
        c = m.group()
        if c in CHAR_ESCAPE:
            return CHAR_ESCAPE[c]

        if c.isspace():
            if fold_newlines:
                return r'\\'
            return r'\\[{}\baselineskip]'.format(len(c))

    return ESCAPE_RE.sub(sub, s)
