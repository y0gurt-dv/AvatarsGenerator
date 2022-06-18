def ShirtCrewNeck(color):
    return (
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M132.5 51.8276C151.002 51.8276 166 42.2107 166 30.3476C166 29.9946 165.987 29.6437 165.96 29.2949C202.936 32.325 232 63.2943 232 101.052V110H32V101.052C32 62.9525 61.592 31.7649 99.0454 29.2195C99.0153 29.5931 99 29.9692 99 30.3476C99 42.2107 113.998 51.8276 132.5 51.8276Z"'
        '    fill="#E6E6E6" />'
        '<mask id="mask0_0_403" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="32" y="29" width="200" height="81">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M132.5 51.8276C151.002 51.8276 166 42.2107 166 30.3476C166 29.9946 165.987 29.6437 165.96 29.2949C202.936 32.325 232 63.2943 232 101.052V110H32V101.052C32 62.9525 61.592 31.7649 99.0454 29.2195C99.0153 29.5931 99 29.9692 99 30.3476C99 42.2107 113.998 51.8276 132.5 51.8276Z"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_403)">'
        '    <rect width="264" height="110" fill="{color}" />'
        '    <g opacity="0.6">'
        '        <ellipse cx="132.5" cy="31.8476" rx="39.6351" ry="26.9138" fill="black" fill-opacity="0.16" />'
        '    </g>'
        '</g>'
    ).format(color=color)