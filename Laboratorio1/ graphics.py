import matplotlib.pyplot as plt
import numpy as np

v1 = [0.006 , 0.009 , 0.018 , 0.026 , 0.044 , 0.054 , 0.067 , 0.085 , 0.107 , 0.129 , 0.153 , 0.223 , 0.23 , 0.272 , 0.299 , 0.337 , 0.401 , 0.704 , 0.775 , 0.861 , 0.984 , 0.652 , 1.009 , 1.085 , 0.875 , 0.936 , 1.865 , 1.13 , 1.572 , 1.221 , 1.254 , 2.109 , 1.767 , 1.561 , 2.499 , 1.801 , 1.847 , 3.106 , 2.915 , 2.271 , 3.2 , 2.328 , 3.201 , 2.844 , 2.881 , 2.784 , 3.735 , 4.408 , 3.367 , 3.978 , 3.652 , 3.798 , 4.522 , 6.171 , 5.319 , 4.623 , 4.249 , 4.407 , 4.84 , 4.916 , 5.65 , 7.665 , 7.39 , 6.255 , 7.241 , 6.017 , 9.096 , 6.093 , 8.117 , 6.565 , 9.172 , 6.685 , 10.544 , 8.489 , 7.233 , 8.679 , 9.274 , 9 , 10.666 , 12.168 , 11.983 , 14.596 , 11.569 , 13.225 , 13.407 , 11.975 , 14.535 , 12.581 , 12.447 , 15.341 , 14.387 , 17.264 , 15.839 , 19.033 , 17.225 , 12.165 , 14.421 , 16.493 , 14.564 , 14.394 , 16.23 , 19.026 , 15.419 , 18.161 , 19.227 , 16.266 , 19.892 , 21.412 , 17.634 , 18.072 , 19.475 , 19.658 , 22.472 , 20.314 , 20.048 , 28.251 , 26.718 , 24.556 , 29.966 , 21.717 , 23.422 , 21.357 , 22.577 , 33.156 , 23.991 , 24.874 , 26.498 , 27.738 , 28.392 , 22.917 , 26.67 , 29.257 , 29.474 , 28.736 , 29.617 , 29.556 , 31.096 , 33.848 , 30.307 , 33.322 , 30.204 , 35.02 , 33.18 , 34.729 , 35.66 , 32.057 , 33.246 , 35.321 , 36.359 , 37.025 , 37.581 , 35.7 , 39.203 , 38.321 , 36.316 , 38.358 , 38.951 , 41.392 , 40.632 , 38.277 , 39.158 , 41.11 , 39.422 , 47.897 , 40.904 , 47.005 , 57.592 , 42.511 , 41.747 , 45.27 , 44.831 , 55.068 , 44.146 , 48.959 , 51.594 , 47.417 , 46.07 , 50.5 , 48.963 , 49.189 , 46.916 , 61.854 , 53.847 , 49.536 , 57.174 , 55.542 , 53.82 , 53.614 , 53.063 , 53.53 , 53.24 , 53.076 , 55.048 , 56.827 , 56.809 , 56.744 , 58.519 , 58.404 , 65.944 , 58.869 , 62.204 , 79.794 , 72.814 , 78.365 , 88.778 , 80.234 , 70.322 , 76.738 , 74.793 , 67.828 , 68.105 , 69.511 , 67.265 , 73.095 , 84.836 , 82.045 , 70.148 , 67.454 , 73.912 , 77.466 , 69.871 , 70.705 , 71.588 , 70.957 , 74.236 , 73.218 , 76.037 , 75.318 , 74.217 , 80.736 , 78.373 , 76.951 , 80.331 , 78.069 , 79.096 , 80.577 , 83 , 83.519 , 83.82 , 84.443 , 82.532 , 82.369 , 84.8 , 84.728 , 85.902 , 84.031 , 85.995 , 92.508 , 92.741 , 91.874 , 91.655 , 92.45 , 108.422 , 95.319 , 90.641 , 92.515 , 94.551 , 95.14 , 93.154 , 94.93 , 94.481 , 98.348 , 99.459 , 99.763 , 98.913 , 100.196 , 98.773 , 98.09 , 100.766 , 99.477 , 106.922 , 104.364 , 111.771 , 108.299 , 121.386 , 116.709 , 120.745 , 113.938 , 110.62 , 112.315 , 112.801 , 111.189 , 111.621 , 112.068 , 113.301 , 117.289 , 119.594 , 125.552 , 118.79 , 116.105 , 127.394 , 147.535 , 138.997 , 137.301 , 138.506 , 136.96 , 142.492 , 136.265 , 144.867 , 140.777 , 147.658 , 146.129 , 146.15 , 147.169 , 144.471 , 133.032 , 136.555 , 133.894 , 137.023 , 150.022 , 152.347 , 158.243 , 157.867 , 137.481 , 140.85 , 163.989 , 154.443 , 158.753 , 144.047 , 156.507 , 144.133 , 144.259 , 147.491 , 148.023 , 152.175 , 148.269 , 152.498 , 150.722 , 155.787 , 154.121 , 153.09 , 169.255 , 197.526 , 180.163 , 174.405 , 179.44 , 179.395 , 178.49 , 175.852 , 187.079 , 184.257 , 194.954 , 163.167 , 167.881 , 178.91 , 158.041 , 191.798 , 194.919 , 159.155 , 161.957 , 174.548 , 159.144 , 183.241 , 162.94 , 170.03 , 168.469 , 168.296 , 184.599 , 193.185 , 171.45 , 169.86 , 181.759 , 171.737 , 174.783 , 231.466 , 231.308 , 232.85 , 190.294 , 202.828 , 200.679 , 189.696 , 209.417 , 192.177 , 225.222 , 194.211 , 191.855 , 194.528 , 214.727 , 196.796 , 199.742 , 199.663 , 200.466 , 201.724 , 205.681 , 215.918 , 203.581 , 206.065 , 208.128 , 208.818 , 214.863 , 215.774 , 211.909 , 211.169 , 222.873 , 231.061 , 241.382 , 241.386 , 229.954 , 218.535 , 229.767 , 228.969 , 215.298 , 217.761 , 218.718 , 219.519 , 221.566 , 218.975 , 222.542 , 247.25 , 224.917 , 226.088 , 270.107 , 233.806 , 240.006 , 232.731 , 229.621 , 241.009 , 243.942 , 251.292 , 254.745 , 256.661 , 354.415 , 243.633 , 244 , 248.652 , 247.828 , 261.765 , 252.045 , 249.441 , 252.13 , 251.429 , 250.826 , 263.777 , 257.721 , 265.142 , 347.134 , 263.035 , 262.93 , 267.906 , 266.019 , 263.492 , 267.938 , 276.86 , 261.569 , 317.663 , 320.433 , 309.554 , 354.136 , 307.979 , 305.667 , 320.515 , 314.609 , 320.191 , 317.899 , 308.142 , 313.626 , 354.096 , 379.517 , 386.399 , 327.277 , 314.278 , 320.804 , 309.922 , 308.577 , 384.414 , 345.052 , 349.412 , 346.635 , 325.473 , 328.977 , 352.982 , 324.464 , 350.511 , 358.058 , 366.665 , 378.798 , 346.826 , 370.4 , 322.898 , 351.592 , 299.468 , 355.074 , 302.305 , 302.53 , 322.39 , 397.273 , 323.648 , 305.676 , 310.81 , 349.666 , 348.735 , 347.386 , 309.37 , 312.647 , 315.624 , 316.172 , 314.246 , 315.331 , 346.449 , 321.895]
v2 = [0.002 , 0.006 , 0.012 , 0.022 , 0.033 , 0.053 , 0.061 , 0.08 , 0.101 , 0.123 , 0.186 , 0.196 , 0.258 , 0.299 , 0.332 , 0.394 , 0.692 , 0.765 , 1.093 , 2.262 , 1.139 , 0.839 , 1.733 , 1.087 , 1.068 , 1.991 , 1.739 , 1.528 , 1.918 , 1.574 , 3.054 , 3.824 , 2.288 , 2.029 , 3.687 , 4.045 , 2.405 , 5.772 , 3.435 , 5.393 , 3.447 , 5.13 , 4.617 , 6.258 , 5.434 , 8.104 , 4.216 , 7.045 , 6.261 , 6.472 , 10.45 , 8.137 , 5.571 , 8.227 , 10.246 , 10.054 , 12.027 , 11.57 , 11.235 , 13.218 , 15.684 , 8.316 , 12.678 , 11.347 , 15.425 , 16.063 , 15.342 , 17.256 , 16.242 , 17.723 , 18.833 , 17.557 , 17.756 , 22.163 , 24.071 , 25.708 , 24.808 , 26.277 , 22.818 , 23.995 , 36.677 , 36.464 , 43.959 , 33.959 , 35.322 , 38.767 , 37.057 , 43.301 , 44.538 , 43.435 , 43.556 , 57.988 , 54.428 , 55.258 , 48.89 , 42.809 , 44.566 , 39.564 , 40.101 , 43.791 , 40.507 , 46.199 , 49.939 , 52.697 , 51.977 , 55.753 , 81.067 , 60.263 , 63.335 , 61.572 , 58.125 , 61.114 , 55.61 , 63.974 , 95.483 , 87.825 , 83.817 , 78.855 , 69.994 , 69.65 , 70.27 , 76.752 , 84.943 , 91.107 , 85.383 , 84.822 , 76.86 , 88.23 , 74.964 , 77.16 , 70.201 , 72.606 , 75.842 , 74.533 , 79.692 , 78.814 , 77.843 , 81.398 , 83.892 , 84.066 , 84.284 , 85.085 , 84.804 , 88.187 , 84.795 , 88.884 , 93.069 , 90.592 , 91.244 , 93.975 , 102.64 , 97.529 , 94.253 , 99.315 , 102.304 , 104.079 , 101.785 , 102.38 , 110.403 , 108.899 , 111.154 , 124.402 , 140.078 , 114.245 , 123.305 , 172.438 , 166.769 , 120.668 , 165.865 , 187.761 , 151.116 , 139.277 , 169.322 , 168.635 , 143.472 , 132.046 , 180.611 , 194.666 , 192.751 , 180.368 , 144.77 , 214.77 , 142.084 , 210.227 , 191.893 , 147.715 , 150.556 , 153.162 , 151.812 , 158.415 , 152.997 , 159.208 , 160.292 , 161.273 , 173.395 , 164.6 , 166.103 , 167.04 , 174.522 , 221.288 , 187.912 , 182.81 , 204.622 , 191.786 , 208.25 , 195.685 , 200.426 , 189.732 , 212.88 , 219.06 , 196.803 , 195.696 , 309.997 , 271.75 , 237.406 , 293.206 , 338.117 , 238.243 , 214.472 , 212.837 , 214.125 , 216.651 , 218.959 , 223.776 , 224.447 , 227.566 , 225.132 , 229.757 , 229.28 , 252.211 , 235.395 , 237.99 , 240.196 , 246.132 , 243.245 , 246.042 , 248.207 , 250.152 , 251.276 , 257.384 , 255.982 , 259.009 , 262.854 , 269.342 , 270.224 , 272.051 , 278.965 , 318.774 , 283.695 , 285.926 , 282.01 , 557.339 , 336.989 , 344.75 , 397.624 , 307.85 , 310.905 , 300.68 , 303.637 , 310.31 , 314.338 , 313.725 , 343.983 , 353.683 , 316.977 , 324.84 , 321.754 , 327.986 , 326.969 , 465.856 , 359.551 , 423.322 , 393.165 , 459.39 , 631.68 , 544.093 , 436.056 , 356.369 , 361.458 , 372.939 , 378.497 , 366.41 , 372.75 , 372.057 , 375.631 , 381.634 , 386.633 , 389.271 , 391.936 , 422.992 , 506.856 , 1120.58 , 617.532 , 591.68 , 597.375 , 637.304 , 605.221 , 600.524 , 625.654 , 778.134 , 778.44 , 668.431 , 664.279 , 687.753 , 557.385 , 460.252 , 469.737 , 474.682 , 658.969 , 696.252 , 696.094 , 746.498 , 517.096 , 696.738 , 790.221 , 776.904 , 745.909 , 874.15 , 572.527 , 545.469 , 516.477 , 521.328 , 520.509 , 632.813 , 540.849 , 559.462 , 535.477 , 544.045 , 548.27 , 549.835 , 562.073 , 1171.87 , 981.272 , 896.355 , 889.78 , 865.163 , 878.846 , 1181.08 , 883.475 , 893.881 , 1452.66 , 618.11 , 607.914 , 891.048 , 631.23 , 510.617 , 1085.65 , 617.96 , 534.923 , 543.989 , 617.463 , 707.286 , 626.992 , 600.319 , 741.722 , 534.528 , 557.559 , 757.497 , 569.924 , 571.918 , 644.179 , 562.178 , 597.126 , 1083.27 , 2400.46 , 2112.01 , 1162.75 , 722.904 , 902.886 , 749.974 , 1008.13 , 760.978 , 733.167 , 756.33 , 800.225 , 738.808 , 787.45 , 794.21 , 744.929 , 761.074 , 780.977 , 783.171 , 791.136 , 944.444 , 781.218 , 791.901 , 811.314 , 799.385 , 809.64 , 859.662 , 935.94 , 1152.26 , 1084.76 , 1132.97 , 1212.15 , 1174.33 , 1016.41 , 1882.48 , 1152.78 , 1360.05 , 909.339 , 842.115 , 843.363 , 888.694 , 849.979 , 919.555 , 892.095 , 866.965 , 1305.84 , 1159 , 1465.6 , 1438.58 , 1895.68 , 909.329 , 1048.78 , 883.226 , 1376.92 , 985.089 , 1264.94 , 1893.31 , 1801.19 , 1055.77 , 1035.74 , 992.85 , 979.702 , 1058.62 , 1001.58 , 1015.89 , 1003.86 , 1013.19 , 1086.42 , 1017.34 , 1621.38 , 1218.85 , 1870.08 , 1998.91 , 1131.71 , 1135.17 , 1102.65 , 1159.01 , 1137.84 , 1174.11 , 1271.41 , 1789.09 , 1676.04 , 2732.06 , 3236.08 , 2151.83 , 1699.09 , 1667.95 , 1680.94 , 1751.72 , 1752.84 , 1668.46 , 1933.57 , 2060.6 , 1999.31 , 2273.03 , 2284.04 , 2037.31 , 1741.53 , 1946.5 , 1590.64 , 1972.93 , 2514.74 , 2729.72 , 2553.57 , 1790.57 , 1807.83 , 2489.02 , 1471.19 , 1740.77 , 2528.41 , 2367.19 , 2155.29 , 2656.49 , 2738.79 , 2549.46 , 2070.1 , 1466.4 , 1672.9 , 1771.96 , 1305.05 , 1424.92 , 1922.84 , 2751.41 , 1275.18 , 1419.12 , 1347.67 , 1869.76 , 1564.17 , 1435.82 , 1217.71 , 1204.73 , 1227.13 , 1216.7 , 1234.25 , 1601.76 , 1309.54 , 1280.56]
n  = [20 , 40 , 60 , 80 , 100 , 120 , 140 , 160 , 180 , 200 , 220 , 240 , 260 , 280 , 300 , 320 , 340 , 360 , 380 , 400 , 420 , 440 , 460 , 480 , 500 , 520 , 540 , 560 , 580 , 600 , 620 , 640 , 660 , 680 , 700 , 720 , 740 , 760 , 780 , 800 , 820 , 840 , 860 , 880 , 900 , 920 , 940 , 960 , 980 , 1000 , 1020 , 1040 , 1060 , 1080 , 1100 , 1120 , 1140 , 1160 , 1180 , 1200 , 1220 , 1240 , 1260 , 1280 , 1300 , 1320 , 1340 , 1360 , 1380 , 1400 , 1420 , 1440 , 1460 , 1480 , 1500 , 1520 , 1540 , 1560 , 1580 , 1600 , 1620 , 1640 , 1660 , 1680 , 1700 , 1720 , 1740 , 1760 , 1780 , 1800 , 1820 , 1840 , 1860 , 1880 , 1900 , 1920 , 1940 , 1960 , 1980 , 2000 , 2020 , 2040 , 2060 , 2080 , 2100 , 2120 , 2140 , 2160 , 2180 , 2200 , 2220 , 2240 , 2260 , 2280 , 2300 , 2320 , 2340 , 2360 , 2380 , 2400 , 2420 , 2440 , 2460 , 2480 , 2500 , 2520 , 2540 , 2560 , 2580 , 2600 , 2620 , 2640 , 2660 , 2680 , 2700 , 2720 , 2740 , 2760 , 2780 , 2800 , 2820 , 2840 , 2860 , 2880 , 2900 , 2920 , 2940 , 2960 , 2980 , 3000 , 3020 , 3040 , 3060 , 3080 , 3100 , 3120 , 3140 , 3160 , 3180 , 3200 , 3220 , 3240 , 3260 , 3280 , 3300 , 3320 , 3340 , 3360 , 3380 , 3400 , 3420 , 3440 , 3460 , 3480 , 3500 , 3520 , 3540 , 3560 , 3580 , 3600 , 3620 , 3640 , 3660 , 3680 , 3700 , 3720 , 3740 , 3760 , 3780 , 3800 , 3820 , 3840 , 3860 , 3880 , 3900 , 3920 , 3940 , 3960 , 3980 , 4000 , 4020 , 4040 , 4060 , 4080 , 4100 , 4120 , 4140 , 4160 , 4180 , 4200 , 4220 , 4240 , 4260 , 4280 , 4300 , 4320 , 4340 , 4360 , 4380 , 4400 , 4420 , 4440 , 4460 , 4480 , 4500 , 4520 , 4540 , 4560 , 4580 , 4600 , 4620 , 4640 , 4660 , 4680 , 4700 , 4720 , 4740 , 4760 , 4780 , 4800 , 4820 , 4840 , 4860 , 4880 , 4900 , 4920 , 4940 , 4960 , 4980 , 5000 , 5020 , 5040 , 5060 , 5080 , 5100 , 5120 , 5140 , 5160 , 5180 , 5200 , 5220 , 5240 , 5260 , 5280 , 5300 , 5320 , 5340 , 5360 , 5380 , 5400 , 5420 , 5440 , 5460 , 5480 , 5500 , 5520 , 5540 , 5560 , 5580 , 5600 , 5620 , 5640 , 5660 , 5680 , 5700 , 5720 , 5740 , 5760 , 5780 , 5800 , 5820 , 5840 , 5860 , 5880 , 5900 , 5920 , 5940 , 5960 , 5980 , 6000 , 6020 , 6040 , 6060 , 6080 , 6100 , 6120 , 6140 , 6160 , 6180 , 6200 , 6220 , 6240 , 6260 , 6280 , 6300 , 6320 , 6340 , 6360 , 6380 , 6400 , 6420 , 6440 , 6460 , 6480 , 6500 , 6520 , 6540 , 6560 , 6580 , 6600 , 6620 , 6640 , 6660 , 6680 , 6700 , 6720 , 6740 , 6760 , 6780 , 6800 , 6820 , 6840 , 6860 , 6880 , 6900 , 6920 , 6940 , 6960 , 6980 , 7000 , 7020 , 7040 , 7060 , 7080 , 7100 , 7120 , 7140 , 7160 , 7180 , 7200 , 7220 , 7240 , 7260 , 7280 , 7300 , 7320 , 7340 , 7360 , 7380 , 7400 , 7420 , 7440 , 7460 , 7480 , 7500 , 7520 , 7540 , 7560 , 7580 , 7600 , 7620 , 7640 , 7660 , 7680 , 7700 , 7720 , 7740 , 7760 , 7780 , 7800 , 7820 , 7840 , 7860 , 7880 , 7900 , 7920 , 7940 , 7960 , 7980 , 8000 , 8020 , 8040 , 8060 , 8080 , 8100 , 8120 , 8140 , 8160 , 8180 , 8200 , 8220 , 8240 , 8260 , 8280 , 8300 , 8320 , 8340 , 8360 , 8380 , 8400 , 8420 , 8440 , 8460 , 8480 , 8500 , 8520 , 8540 , 8560 , 8580 , 8600 , 8620 , 8640 , 8660 , 8680 , 8700 , 8720 , 8740 , 8760 , 8780 , 8800 , 8820 , 8840 , 8860 , 8880 , 8900 , 8920 , 8940 , 8960 , 8980 , 9000 , 9020 , 9040 , 9060 , 9080 , 9100 , 9120 , 9140 , 9160 , 9180 , 9200 , 9220 , 9240 , 9260 , 9280 , 9300 , 9320 , 9340 , 9360 , 9380 , 9400 , 9420 , 9440 , 9460 , 9480 , 9500 , 9520 , 9540 , 9560 , 9580 , 9600 , 9620 , 9640 , 9660 , 9680 , 9700 , 9720 , 9740 , 9760 , 9780 , 9800 , 9820 , 9840 , 9860 , 9880 , 9900 , 9920 , 9940 , 9960 , 9980 , 10000]


plt.plot(n, v1, color="red", label="Primer par de bucles anidados")
plt.plot(n, v2, color="blue", label="Segundo par de bucles anidados")
plt.xlabel("n")
plt.ylabel("Tiempo(s)")
plt.legend()
plt.title("PRUEBAS CON LA MEMORIA CACHE BUCLES FOR ANIDADOS")
plt.show()


v1 = [0.008 , 1.354 , 8.99 , 30.089 , 60.908 , 73.919 , 136.008 , 222.733 , 364.663 , 671.188 , 1281.04 , 1343.37 , 2004.03 , 2233.63 , 2693.11 , 3632.46 , 4395.05 , 5009.75 , 6446.75 , 6783.76 , 8590.68 , 9438.62]
v2 = [0.007 , 0.899 , 5.783 , 22.266 , 47.152 , 90.437 , 157.79 , 257.435 , 380.962 , 549.723 , 751.573 , 1004.31 , 1309.28 , 1668.59 , 2113.86 , 2601.91 , 3244.32 , 4837.2 , 5558.36 , 7145.83 , 8386.93 , 10333.5]
n  = [2 , 52 , 102 , 152 , 202 , 252 , 302 , 352 , 402 , 452 , 502 , 552 , 602 , 652 , 702 , 752 , 802 , 852 , 902 , 952 , 1002 , 1052]

plt.plot(n, v1, color="red", label="Clasica")
plt.plot(n, v2, color="blue", label="Por bloques de n/2")
plt.xlabel("n")
plt.ylabel("Tiempo(s)")
plt.legend()
plt.title("MUMTIPLICACION DE MATRICES")
plt.show()