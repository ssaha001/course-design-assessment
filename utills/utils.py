def merge_sort(data, comparison_logic):
    if len(data) > 1:
        mid = len(data)//2
        first_half = data[:mid]
        second_half = data[mid:]

        merge_sort(first_half, comparison_logic)
        merge_sort(second_half, comparison_logic)

        i = j = k = 0

        # Compare the values
        while i < len(first_half) and j < len(second_half):
            if comparison_logic(first_half[i], second_half[j]):
                data[k] = first_half[i]
                i += 1
            else:
                data[k] = second_half[j]
                j += 1
            k += 1
        
        # Add remaining values to the list
        while i < len(first_half):
            data[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            data[k] = second_half[j]
            j += 1
            k += 1