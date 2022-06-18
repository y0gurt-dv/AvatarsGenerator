def TheCaesarSidePart(color):
    return (
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M78.0001 98C77.6729 99.2227 76.347 99.4884 76.0001 98C75.281 87.7019 76.0001 35.7256 133 35C190 34.2744 190.719 87.7019 190 98C189.653 99.4884 188.327 99.2227 188 98C188.463 96.4457 184.704 69.2481 175 62C173.241 60.7763 167.753 59.6102 160.359 58.739L164 50L157.018 58.3785C149.986 57.6847 141.657 57.2515 133.313 57.2456C114.008 57.2319 94.6184 59.4834 91.0001 62C81.2961 69.2481 77.5374 96.4457 78.0001 98Z"'
        '    fill="#28354B" />'
        '<mask id="mask0_0_1699" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="75" y="34" width="116" height="66">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M78.0001 98C77.6729 99.2227 76.347 99.4884 76.0001 98C75.281 87.7019 76.0001 35.7256 133 35C190 34.2744 190.719 87.7019 190 98C189.653 99.4884 188.327 99.2227 188 98C188.463 96.4457 184.704 69.2481 175 62C173.241 60.7763 167.753 59.6102 160.359 58.739L164 50L157.018 58.3785C149.986 57.6847 141.657 57.2515 133.313 57.2456C114.008 57.2319 94.6184 59.4834 91.0001 62C81.2961 69.2481 77.5374 96.4457 78.0001 98Z"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_1699)">'
        '    <rect x="1" width="264" height="280" fill="{color}" />'
        '</g>'

    ).format(color=color)