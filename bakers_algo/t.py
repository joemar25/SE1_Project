import numpy as np

processes = np.array(
    [
        # ['id', [allocation matrix], [max need matrix], [available matrix], [need matrix]]
        ['P1', [0, 1, 1, 0], [0, 2, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        ['P2', [1, 2, 3, 1], [1, 6, 5, 2], [0, 0, 0, 0], [0, 0, 0, 0]],
        ['P3', [1, 3, 6, 5], [2, 3, 6, 6], [0, 0, 0, 0], [0, 0, 0, 0]],
        ['P4', [0, 6, 3, 2], [0, 6, 5, 2], [0, 0, 0, 0], [0, 0, 0, 0]],
        ['P5', [0, 0, 1, 4], [0, 6, 5, 6], [0, 0, 0, 0], [0, 0, 0, 0]],
    ],
    dtype=object,
    copy=False,
    order='K',
    subok=False,
    ndmin=0
)

# processes

a = np.subtract(processes[0][1], processes[0][2])

print(a)
print(a[1])
