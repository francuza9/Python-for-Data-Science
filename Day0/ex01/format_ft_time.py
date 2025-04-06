import time as time

time_since_epoch = time.time()
time_since_epoch_scientific_notation = "{:.2e}".format(time_since_epoch)

print(f"Seconds since January 1, 1970: {time_since_epoch:,.4f} or {time_since_epoch_scientific_notation} in scientific notation")
print(time.strftime("%b %d %Y", time.localtime()))
