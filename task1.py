def get_kth_element(arr: list, k: int):
    def max_heapify_sized(arr: list, i: int, size: int):
        left = i * 2 + 1
        right = i * 2 + 2
        if left >= size:
            return

        if right < len(arr) and arr[left] < arr[right]:
            index_to_swap = right
            value_to_swap = arr[right]
        else:
            index_to_swap = left
            value_to_swap = arr[left]
        if arr[i] < value_to_swap:
            arr[i], arr[index_to_swap] = arr[index_to_swap], arr[i]
            max_heapify_sized(arr, index_to_swap, size)
        return arr

    def build_max_heap(arr: list):
        for i in range(len(arr) // 2, -1, -1):
            max_heapify_sized(arr, i, len(arr))
        return arr

    def heapsort(arr: list):
        build_max_heap(arr)
        for i in range(len(arr) - 1, 0, -1):
            if arr[0] > arr[i]:
                arr[0], arr[i] = arr[i], arr[0]
            max_heapify_sized(arr, 0, i - 1)
        return arr

    arr = heapsort(arr)
    return arr[k]
