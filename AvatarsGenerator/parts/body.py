def get_skin(config):
    skin_color = config.get('skin_color')
    return (
    '<g id="body">'
    '   <mask id="mask0_0_151" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="32" y="36" width="200" height="244">'
    '       <path fill-rule="evenodd" clip-rule="evenodd"'
    '           d="M132 36C101.072 36 76 61.0721 76 92V98.1659C70.3246 99.1181 66 104.054 66 110V124C66 130.052 70.4803 135.058 76.3051 135.881C78.3722 155.687 90.7626 172.422 108 180.611V199H104C64.2355 199 32 231.236 32 271V280H232V271C232 231.236 199.764 199 160 199H156V180.611C173.237 172.422 185.628 155.687 187.695 135.881C193.52 135.058 198 130.052 198 124V110C198 104.054 193.675 99.1181 188 98.1659V92C188 61.0721 162.928 36 132 36Z"'
    '           fill="white" />'
    '   </mask>'
    '   <g mask="url(#mask0_0_151)" fill="{skin_color}">'
    '       <g transform="translate(0.000000, 0.000000)" id="Color">'
    '           <rect x="0" y="0" width="264" height="280"></rect>'
    '       </g>'
    '       <path fill-rule="evenodd" clip-rule="evenodd"'
    '           d="M76 130V138C76 168.928 101.072 194 132 194C162.928 194 188 168.928 188 138V130C188 160.928 162.928 186 132 186C101.072 186 76 160.928 76 130Z"'
    '           fill="black" fill-opacity="0.1" />'
    '   </g>'
    '</g>'
    ).format(skin_color=skin_color)
