void countingSort(vector<int> &arr) {
	std::array<int, 2001> counts= {0};
	for(int val : arr){
		counts[val+1000]++;
	}
	int arrIter = 0;
	for (int mapIter = 0; mapIter <= 2000; mapIter++){
		for(int occurences = 0; occurences < counts[mapIter]; occurences++){
			arr[arrIter] = 	mapIter-1000;
			arrIter++;
		}	
	}
}
