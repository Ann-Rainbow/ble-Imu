import csv


def collectCsvData(i):
    global ax, ay, az, gx, gy, gz
    with open(f'all_probes/{i}_probe/accelx_data.txt', 'r') as f:
        # print(f.read())
        ax = [float(x) for x in f.read().split('\n')[:-1]]
    # print(ax)
    with open(f'all_probes/{i}_probe/accely_data.txt', 'r') as f:
        ay = [float(x) for x in f.read().split('\n')[:-1]]
    with open(f'all_probes/{i}_probe/accelz_data.txt', 'r') as f:
        az = [float(x) for x in f.read().split('\n')[:-1]]
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gx = [float(x) for x in f.read().split('\n')[:-1]]
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gy = [float(x) for x in f.read().split('\n')[:-1]]
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gz = [float(x) for x in f.read().split('\n')[:-1]]


def writeCSVFile(i):
    csvfile = open(f'all_probes/{i}_probe/{i}_probe.csv', 'w', newline='')
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['ax', 'ay', 'az', 'gx', 'gy', 'gz'])
    for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
        spamwriter.writerow([xa, ya, za, xg, yg, zg])
    csvfile.close()


if __name__ == "__main__":
    for i in range(121, 122):
        collectCsvData(i)

    for i in range(121, 122):
        writeCSVFile(i)
