class Solution {
    int getElementIndex(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        // Finding the pivot
        while (left < right) {
            int pivot = left + (right - left) / 2;
            if (array[pivot] > array[right]) {
                left = pivot + 1;
            } else {
                right = pivot;
            }
        }

        // Determine search range
        int start, end;
        if (target >= array[left] && target <= array[array.length - 1]) {
            start = left;
            end = array.length - 1;
        } else {
            start = 0;
            end = left;
        }

        // Binary search in the determined range
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (array[mid] == target) {
                return mid;
            } else if (array[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return -1;
    }
}
