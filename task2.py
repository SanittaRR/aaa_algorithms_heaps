import heapq


def merge_k_sorted(arrs: list) -> list:
    total = []
    heap0 = []

    for i in range(len(arrs)):
        heapq.heappush(heap0, (arrs[i][0], i, 0))

    while heap0:
        val, rows, columns = heapq.heappop(heap0)
        total.append(val)
        if columns + 1 < len(arrs[rows]):
            heapq.heappush(heap0, (arrs[rows][columns + 1], rows, columns + 1))
    return total
