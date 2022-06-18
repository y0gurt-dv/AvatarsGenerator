def ShortRound(color):
    return (
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M167.309 35.006C147.121 23.3064 127.129 25.2219 112.037 29.0299C96.9448 32.8379 88.0168 43.6512 80.3567 59.648C76.5956 67.5028 74.366 76.7914 74.0231 85.4813C73.8884 88.8932 74.3484 92.4151 75.2677 95.7003C75.6049 96.9061 77.4232 101.087 77.9225 97.7088C78.0885 96.5842 77.4804 95.0327 77.4216 93.8375C77.3444 92.2693 77.4273 90.6807 77.5342 89.1148C77.7341 86.1873 78.256 83.3153 79.1847 80.5246C80.5119 76.5367 82.2014 72.2128 84.7874 68.848C91.1884 60.5205 102.269 60.0458 111.066 55.4635C110.303 56.8686 107.36 59.1432 108.379 60.7268C109.084 61.8206 111.749 61.489 113.022 61.4539C116.371 61.3623 119.735 60.7796 123.043 60.3069C128.256 59.5617 133.141 58.0517 138.047 56.218C142.063 54.7163 146.65 53.3256 149.669 50.1404C154.54 55.188 160.81 59.9345 167.07 63.1428C172.688 66.0221 181.749 67.461 185.183 73.3006C189.248 80.2147 187.378 88.7073 188.619 96.2007C189.091 99.0503 190.164 98.9865 190.751 96.4377C191.748 92.1082 192.219 87.6101 191.902 83.1592C191.184 73.1114 187.497 46.7056 167.309 35.006Z"'
        '    fill="#28354B" />'
        '<mask id="mask0_0_1667" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="74" y="26" width="118" height="73">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M167.309 35.006C147.121 23.3064 127.129 25.2219 112.037 29.0299C96.9448 32.8379 88.0168 43.6512 80.3567 59.648C76.5956 67.5028 74.366 76.7914 74.0231 85.4813C73.8884 88.8932 74.3484 92.4151 75.2677 95.7003C75.6049 96.9061 77.4232 101.087 77.9225 97.7088C78.0885 96.5842 77.4804 95.0327 77.4216 93.8375C77.3444 92.2693 77.4273 90.6807 77.5342 89.1148C77.7341 86.1873 78.256 83.3153 79.1847 80.5246C80.5119 76.5367 82.2014 72.2128 84.7874 68.848C91.1884 60.5205 102.269 60.0458 111.066 55.4635C110.303 56.8686 107.36 59.1432 108.379 60.7268C109.084 61.8206 111.749 61.489 113.022 61.4539C116.371 61.3623 119.735 60.7796 123.043 60.3069C128.256 59.5617 133.141 58.0517 138.047 56.218C142.063 54.7163 146.65 53.3256 149.669 50.1404C154.54 55.188 160.81 59.9345 167.07 63.1428C172.688 66.0221 181.749 67.461 185.183 73.3006C189.248 80.2147 187.378 88.7073 188.619 96.2007C189.091 99.0503 190.164 98.9865 190.751 96.4377C191.748 92.1082 192.219 87.6101 191.902 83.1592C191.184 73.1114 187.497 46.7056 167.309 35.006Z"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_1667)">'
        '    <rect x="1" width="264" height="280" fill="{color}" />'
        '</g>'
    ).format(color=color)