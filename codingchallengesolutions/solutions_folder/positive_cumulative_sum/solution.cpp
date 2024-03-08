vector<int> getPositiveCumulativeSum(vector<int> &arr) {
    std::vector<int> cumulativeSums(arr.size());
	int sum = 0;
    std::transform(arr.begin(), arr.end(), cumulativeSums.begin(), [&sum](int n) {
		sum+=n;
        return sum;
    });
		
	std:vector<int> positivecumulativeSums;
	std::copy_if(cumulativeSums.begin(), cumulativeSums.end(), std::back_inserter(positivecumulativeSums), [](int number){return number > 0;});
	return positivecumulativeSums;
}