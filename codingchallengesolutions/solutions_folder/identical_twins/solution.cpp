long long nP2(int num){

	return num * (num-1) / 2;
}

int getIdenticalTwinsCount(vector<int> &arr) {
        std::unordered_map<int, int> Map;

    for (int i = 0; i < arr.size(); ++i) {
        if (Map.find(arr[i]) == Map.end()) {
            Map[arr[i]] = 1;
        } else {
            Map[arr[i]]++;
        }
    }
	long long sum = 0;
    for (const auto& pair : Map) {
        sum += nP2(pair.second);
    }
	return sum;
}