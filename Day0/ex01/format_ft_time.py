import time

"""
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
"""

seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(time.strftime("%B %d %Y", time.localtime(seconds)))