import numpy as np
from app.import_etherium_timeseries import etherium_data

def time_in_zones(x, n):
    nb = np.zeros((len(x) - n, n - 1))
    for i in range(0, len(x) - n):
        for j in range(1, n):
            nb[i, j - 1] = np.prod(x[i:i + j])

    return nb


def expected_timefraction(lower_bound, upper_bound, time_horizon):
    time, eth_value = etherium_data()
    r_data = eth_value[1:] / eth_value[:-1]
    r = time_in_zones(r_data, time_horizon)
    time_fraction = np.mean(np.array([len(np.where((r_ < upper_bound) * (r_ > lower_bound))[0]) for r_ in r])) / \
                    r.shape[1]
    return time_fraction


def best_range(desired_timefraction=0.8, time_horizon=100):
    time, eth_value = etherium_data()
    r_data = eth_value[1:] / eth_value[:-1]
    r = time_in_zones(r_data, time_horizon)
    time_fraction = []
    bounds = []
    lower_bound = 0.0
    for upper_bound in np.arange(0.01, 5, 0.01):
        bounds += [upper_bound]
        time_fraction += [
            np.mean(np.array([len(np.where((r_ < upper_bound) * (r_ > lower_bound))[0]) for r_ in r])) / r.shape[1]]
        lower_bound = upper_bound

    best_delta = len(time_fraction)
    best_l_index = 0
    for l_index in range(len(time_fraction)):

        delta = 0
        t_fraction = np.sum(time_fraction[l_index:l_index + delta])
        while t_fraction < desired_timefraction and l_index + delta < len(time_fraction) - 1:
            delta += 1
            t_fraction = np.sum(time_fraction[l_index:l_index + delta])

        if delta < best_delta and t_fraction >= desired_timefraction:
            best_l_index = l_index
            best_delta = delta
    return bounds[best_l_index], bounds[best_l_index + best_delta]
