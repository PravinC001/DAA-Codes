def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temporary arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Main function to take input from the user
if __name__ == "__main__":
    # Input: Number of elements
    n = int(input("Enter the number of elements: "))

    # Input: Elements of the array
    arr = list(map(int, input(f"Enter {n} elements separated by spaces: ").split()))

    # Validate input size
    if len(arr) != n:
        print("Error: The number of elements entered does not match the specified size.")
    else:
        print("Original array:", arr)
        merge_sort(arr)
        print("Sorted array:", arr)
