#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int key) {
    int s = 0;          // Start index
    int e = n - 1;      // End index

    while (s <= e) {
        int mid = (s + e) / 2; // Calculate mid-point

        if (arr[mid] == key) {
            return mid; // Key found at index mid
        } else if (arr[mid] > key) {
            e = mid - 1; // Narrow search to the left half
        } else {
            s = mid + 1; // Narrow search to the right half
        }
    }
    return -1; // Key not found
}

int main() {
    int n;

    // Input the number of elements
    cout << "Enter the number of elements: ";
    cin >> n;

    if (n <= 0) {
        cout << "Invalid array size!" << endl;
        return 0;
    }

    int arr[n];

    // Input the array elements
    cout << "Enter the elements of the array (sorted): ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int key;
    // Input the key to search
    cout << "Enter the key to search: ";
    cin >> key;

    // Perform binary search
    int result = binarySearch(arr, n, key);

    // Display the result
    if (result != -1) {
        cout << "Key found at index: " << result << endl;
    } else {
        cout << "Key not found in the array." << endl;
    }

    return 0;
}
