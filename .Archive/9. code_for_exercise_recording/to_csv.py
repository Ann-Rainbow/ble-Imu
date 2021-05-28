import csv
with open("1_probe/accelx_data.txt", 'r') as f:
    # print(f.read())
    ax = [float(x) for x in f.read().split('\n')[:-1]]
# print(ax)
with open('1_probe/accely_data.txt', 'r') as f:
    ay = [float(x) for x in f.read().split('\n')[:-1]]
with open('1_probe/accelz_data.txt', 'r') as f:
    az = [float(x) for x in f.read().split('\n')[:-1]]

with open('1_probe/gyrox_data.txt', 'r') as f:
    gx = [float(x) for x in f.read().split('\n')[:-1]]
with open('1_probe/gyrox_data.txt', 'r') as f:
    gy = [float(x) for x in f.read().split('\n')[:-1]]
with open('1_probe/gyrox_data.txt', 'r') as f:
    gz = [float(x) for x in f.read().split('\n')[:-1]]

csvfile = open('probe.csv', 'w', newline='')
spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(['ax', 'ay', 'az', 'gx', 'gy', 'gz'])
for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
    spamwriter.writerow([xa, ya, za, xg, yg, zg])
csvfile.close()