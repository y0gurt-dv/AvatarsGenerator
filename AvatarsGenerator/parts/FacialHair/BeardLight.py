def BeardLight(color):
    return (
        '<path fill-rule="evenodd" clip-rule="evenodd"'
        '    d="M101.428 98.1686C98.9148 100.463 96.2372 101.494 92.8529 100.773C92.2706 100.649 89.8963 96.2346 83.9998 96.2346C78.1033 96.2346 75.7294 100.649 75.1467 100.773C71.7624 101.494 69.0848 100.463 66.5713 98.1686C61.8462 93.8556 57.9166 87.9082 60.2778 81.4192C61.5084 78.0369 63.5097 74.3237 67.1506 73.2459C71.0384 72.0955 76.4969 73.2439 80.4148 72.4583C81.6841 72.2035 83.0707 71.7509 83.9998 71C84.929 71.7509 86.3159 72.2035 87.5846 72.4583C91.5028 73.2439 96.9613 72.0955 100.849 73.2459C104.49 74.3237 106.491 78.0369 107.722 81.4192C110.083 87.9082 106.154 93.8556 101.428 98.1686M140.081 26C136.671 34.4003 137.988 44.858 137.357 53.6759C136.844 60.8432 135.337 71.5858 128.973 76.2145C125.718 78.5816 119.794 82.5599 115.542 81.4502C112.615 80.6864 112.302 72.2901 108.455 69.147C104.092 65.5823 98.643 64.016 93.1491 64.2579C90.7785 64.3623 85.9841 64.3375 83.9999 66.1605C82.0157 64.3375 77.2217 64.3623 74.8511 64.2579C69.3569 64.016 63.9081 65.5823 59.5446 69.147C55.6977 72.2901 55.3857 80.6864 52.4583 81.4502C48.2058 82.5599 42.2818 78.5816 39.027 76.2145C32.6624 71.5858 31.1562 60.8432 30.6429 53.6759C30.0121 44.858 31.3292 34.4003 27.9188 26C26.2598 26 27.354 42.1289 27.354 42.1289V62.4851C27.3857 77.7732 36.9351 100.655 58.108 109.393C63.2861 111.53 75.0153 115 83.9999 115C92.9846 115 104.714 111.86 109.892 109.723C131.065 100.986 140.614 77.7732 140.646 62.4851V42.1289C140.646 42.1289 141.74 26 140.081 26"'
        '    fill="#331B0C" />'
        '<mask id="mask0_0_591" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="27" y="26" width="114" height="89">'
        '    <path fill-rule="evenodd" clip-rule="evenodd"'
        '        d="M101.428 98.1686C98.9148 100.463 96.2372 101.494 92.8529 100.773C92.2706 100.649 89.8963 96.2346 83.9998 96.2346C78.1033 96.2346 75.7294 100.649 75.1467 100.773C71.7624 101.494 69.0848 100.463 66.5713 98.1686C61.8462 93.8556 57.9166 87.9082 60.2778 81.4192C61.5084 78.0369 63.5097 74.3237 67.1506 73.2459C71.0384 72.0955 76.4969 73.2439 80.4148 72.4583C81.6841 72.2035 83.0707 71.7509 83.9998 71C84.929 71.7509 86.3159 72.2035 87.5846 72.4583C91.5028 73.2439 96.9613 72.0955 100.849 73.2459C104.49 74.3237 106.491 78.0369 107.722 81.4192C110.083 87.9082 106.154 93.8556 101.428 98.1686M140.081 26C136.671 34.4003 137.988 44.858 137.357 53.6759C136.844 60.8432 135.337 71.5858 128.973 76.2145C125.718 78.5816 119.794 82.5599 115.542 81.4502C112.615 80.6864 112.302 72.2901 108.455 69.147C104.092 65.5823 98.643 64.016 93.1491 64.2579C90.7785 64.3623 85.9841 64.3375 83.9999 66.1605C82.0157 64.3375 77.2217 64.3623 74.8511 64.2579C69.3569 64.016 63.9081 65.5823 59.5446 69.147C55.6977 72.2901 55.3857 80.6864 52.4583 81.4502C48.2058 82.5599 42.2818 78.5816 39.027 76.2145C32.6624 71.5858 31.1562 60.8432 30.6429 53.6759C30.0121 44.858 31.3292 34.4003 27.9188 26C26.2598 26 27.354 42.1289 27.354 42.1289V62.4851C27.3857 77.7732 36.9351 100.655 58.108 109.393C63.2861 111.53 75.0153 115 83.9999 115C92.9846 115 104.714 111.86 109.892 109.723C131.065 100.986 140.614 77.7732 140.646 62.4851V42.1289C140.646 42.1289 141.74 26 140.081 26"'
        '        fill="white" />'
        '</mask>'
        '<g mask="url(#mask0_0_591)">'
        '    <rect width="168" height="152" fill="{color}" />'
        '</g>'
    ).format(color=color)