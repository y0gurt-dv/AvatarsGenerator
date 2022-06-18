def Overall(color):
    return (
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M68 110L78 110L94 110H170L186 110L196 110V38.6318C188.15 34.0908 179.363 30.9893 170 29.6884V74H94V29.6884C84.6371 30.9893 75.8501 34.0908 68 38.6318V110Z"'
        '    fill="#B7C1DB" />'
        '<mask id="mask0_0_386" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="68" y="29" width="128" height="81">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M68 110L78 110L94 110H170L186 110L196 110V38.6318C188.15 34.0908 179.363 30.9893 170 29.6884V74H94V29.6884C84.6371 30.9893 75.8501 34.0908 68 38.6318V110Z"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_386)">'
        '    <rect width="264" height="110" fill="{color}" />'
        '</g>'
        '<circle cx="81" cy="83" r="5" fill="#F4F4F4" />'
        '<circle cx="183" cy="83" r="5" fill="#F4F4F4" />'
    ).format(color=color)
