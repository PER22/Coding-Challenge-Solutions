class Solution {
	int[] mergeSortedArrays(int[] A, int[] B) {
	    int[] C = new int[A.length + B.length];
		int a_index = 0;
		int b_index = 0;
		int c_index = 0;
		while(a_index < A.length && b_index < B.length){
			if(A[a_index] < B[b_index]){
				C[c_index++] = A[a_index++];
			}
			else{
				C[c_index++] = B[b_index++];
			}
		}
		if(a_index < A.length){
			while (c_index < C.length){
				C[c_index++] = A[a_index++];
			}
		}
		else{
			while (c_index < C.length){
				C[c_index++] = B[b_index++];
			}
		}
		return C;
	}
}