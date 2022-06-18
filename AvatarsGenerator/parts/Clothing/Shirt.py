def Shirt(color):
    return (
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M132.5 54C151.002 54 166 44.3741 166 32.5C166 31.4015 165.872 30.3223 165.624 29.2681C202.76 32.1373 232 63.1798 232 101.052V110H32V101.052C32 62.8348 61.7752 31.5722 99.3929 29.1967C99.1342 30.2735 99 31.3767 99 32.5C99 44.3741 113.998 54 132.5 54Z"'
        '    fill="#E6E6E6" />'
        '<mask id="mask0_0_242" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="32" y="29" width="200" height="81">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M132.5 54C151.002 54 166 44.3741 166 32.5C166 31.4015 165.872 30.3223 165.624 29.2681C202.76 32.1373 232 63.1798 232 101.052V110H32V101.052C32 62.8348 61.7752 31.5722 99.3929 29.1967C99.1342 30.2735 99 31.3767 99 32.5C99 44.3741 113.998 54 132.5 54Z"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_242)">'
        '    <rect width="264" height="110" fill="{color}" />'
        '</g>'
    ).format(color=color)