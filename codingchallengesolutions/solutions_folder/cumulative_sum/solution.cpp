vector<int> getCumulativeSum(vector<int> &arr) {
	vector<int> sums;
	if(arr.size() > 0){
		sums.push_back(arr[0]);
		for (int i = 1; i < arr.size(); i++){
			sums.push_back(arr[i] + sums[i-1]);
		}
	}
	return sums;
}