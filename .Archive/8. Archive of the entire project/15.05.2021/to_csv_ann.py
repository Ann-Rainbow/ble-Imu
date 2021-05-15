import csv
import numpy as np


def median_filter(x, k):
    """Apply a length-k median filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """
    assert k % 2 == 1, "Median filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    k2 = (k - 1) // 2
    y = np.zeros ((len (x), k), dtype=x.dtype)
    y[:,k2] = x
    for i in range (k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.median (y, axis=1)


def collect_csv_data_dir(directory):
    # global ax, ay, az, gx, gy, gz
    with open(f'{directory}/accelx_data.txt', 'r') as f:
        # print(f.read())
        ax = np.array([float(x) for x in f.read().split('\n')[:-1]])
    # print(ax)
    with open(f'{directory}/accely_data.txt', 'r') as f:
        ay = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{directory}/accelz_data.txt', 'r') as f:
        az = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{directory}/gyrox_data.txt', 'r') as f:
        gx = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{directory}/gyrox_data.txt', 'r') as f:
        gy = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'{directory}/gyrox_data.txt', 'r') as f:
        gz = np.array([float(x) for x in f.read().split('\n')[:-1]])

    ax = median_filter(ax, 5)
    ay = median_filter(ay, 5)
    az = median_filter(az, 5)

    gx = median_filter(gx, 5)
    gy = median_filter(gy, 5)
    gz = median_filter(gz, 5)

    vector = []
    for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
        vector.append(xa)
        vector.append(ya)
        vector.append(za)
        vector.append(xg)
        vector.append(yg)
        vector.append(zg)

    return vector


def collect_csv_data(i):
    # global ax, ay, az, gx, gy, gz
    with open(f'all_probes/{i}_probe/accelx_data.txt', 'r') as f:
        # print(f.read())
        ax = np.array([float(x) for x in f.read().split('\n')[:-1]])
    # print(ax)
    with open(f'all_probes/{i}_probe/accely_data.txt', 'r') as f:
        ay = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/accelz_data.txt', 'r') as f:
        az = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gx = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gy = np.array([float(x) for x in f.read().split('\n')[:-1]])
    with open(f'all_probes/{i}_probe/gyrox_data.txt', 'r') as f:
        gz = np.array([float(x) for x in f.read().split('\n')[:-1]])

    ax = median_filter(ax, 5)
    ay = median_filter(ay, 5)
    az = median_filter(az, 5)

    gx = median_filter(gx, 5)
    gy = median_filter(gy, 5)
    gz = median_filter(gz, 5)

    vector = []
    for xa, ya, za, xg, yg, zg in zip(ax, ay, az, gx, gy, gz):
        vector.append(xa)
        vector.append(ya)
        vector.append(za)
        vector.append(xg)
        vector.append(yg)
        vector.append(zg)

    return vector


def write_csv_file(i, spamWriter):
    # csvfile = open(f'all_probes/{i}_probe/{i}_probe.csv', 'w', newline='')
    # spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # spamwriter.writerow(['ax', 'ay', 'az', 'gx', 'gy', 'gz'])
    # vector = []
    vector = collect_csv_data(i)
    with open(f'all_probes/{i}_probe/Result', 'r') as f:
        success = int(f.read())
    vector.append(success)
    spamWriter.writerow(vector)
    # csvfile.close()
    return


if __name__ == "__main__":
    # make dataset
    csvfile = open(f'all_probes/dataset-arm_raisings_forward.csv', 'w', newline='\n')
    spamWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for i in range(200, 319):
        # collect_csv_data(i)
        write_csv_file(i, spamWriter)

    csvfile.close()
    # for i in range(0, 120):
    #     writeCSVFile(i)
