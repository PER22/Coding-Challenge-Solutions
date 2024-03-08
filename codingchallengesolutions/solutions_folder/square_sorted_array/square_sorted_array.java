class Solution {
	int[] getSquareSortedArray (int[] arr) {
		int[] result = new int[arr.length];
		
		for (int i = 0; i < arr.length; i++){
			result[i] = arr[i] * arr[i];
		}
		Arrays.sort(result);
		
		
		return result;
	}
}