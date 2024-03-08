class Solution {
	boolean hasTwoSumZero (int[] A) {
		int left = 0; 
		int right = A.length - 1;
		while(left < right){
			if(A[left] + A[right] == 0){return true;}
			else if(A[left] + A[right] < 0){left++;}
			else{right--;}
		}
		return false;
	}
}