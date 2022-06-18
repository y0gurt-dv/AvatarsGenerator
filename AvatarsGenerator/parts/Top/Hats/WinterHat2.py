def WinterHat2(color):
    return (
        '<circle cx="70" cy="241" r="9" fill="#F4F4F4" />'
        '<rect x="69" y="176" width="2" height="58" fill="#F4F4F4" />'
        '<circle cx="196" cy="233" r="9" fill="#F4F4F4" />'
        '<rect x="195" y="168" width="2" height="58" fill="#F4F4F4" />'
        '<circle cx="133" cy="20" r="20" fill="#F4F4F4" />'
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M93.4486 77.5347H133H172.551C178.635 77.5347 182.367 80.4596 182.367 86.5347V165.989C182.367 196.447 205 196.405 205 176.91V103.045C205 68.8032 187.773 21 133 21C78.2273 21 61 68.8032 61 103.045V176.91C61 196.405 83.6331 196.447 83.6331 165.989V86.5347C83.6331 80.4596 87.3649 77.5347 93.4486 77.5347Z"'
        '    fill="#F4F4F4" />'
        '<mask id="mask0_0_810" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="61" y="21" width="144" height="170">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M93.4486 77.5347H133H172.551C178.635 77.5347 182.367 80.4596 182.367 86.5347V165.989C182.367 196.447 205 196.405 205 176.91V103.045C205 68.8032 187.773 21 133 21C78.2273 21 61 68.8032 61 103.045V176.91C61 196.405 83.6331 196.447 83.6331 165.989V86.5347C83.6331 80.4596 87.3649 77.5347 93.4486 77.5347Z"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_810)">'
        '    <rect x="59" y="19" width="149" height="172" fill="{color}" />'
        '    <rect x="60" y="21" width="146" height="46" fill="black" fill-opacity="0.2" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M102.5 50L90 32H115L102.5 50Z" fill="white"'
        '        fill-opacity="0.5" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M133.5 50L121 32H146L133.5 50Z" fill="white"'
        '        fill-opacity="0.5" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M164.5 50L152 32H177L164.5 50Z" fill="white"'
        '        fill-opacity="0.5" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M86.5 41L99 59H74L86.5 41Z" fill="black" fill-opacity="0.5" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M117.5 41L130 59H105L117.5 41Z" fill="black"'
        '        fill-opacity="0.5" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M148.5 41L161 59H136L148.5 41Z" fill="black"'
        '        fill-opacity="0.5" />'
        '    <path fill-rule="evenodd" clip-rule="evenodd" d="M179.5 41L192 59H167L179.5 41Z" fill="black"'
        '        fill-opacity="0.5" />'
        '</g>'
    ).format(color=color)