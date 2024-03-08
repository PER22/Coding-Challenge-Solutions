class Solution {
	void insertionSort (int[] arr) {
		for (int sortedBefore = 0; sortedBefore < arr.length; sortedBefore++){
			int temp = arr[sortedBefore];
			int j;
			for(j = sortedBefore; j > 0 && temp < arr[j - 1]; j--) {
    			arr[j] = arr[j - 1];
			}
			arr[j] = temp;
		}
	}
}