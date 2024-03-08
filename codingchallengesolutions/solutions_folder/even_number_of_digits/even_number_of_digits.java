class Solution {
	List<Integer> getEvenDigitNumbers (int[] arr) {
		List<Integer> evenDigits = new ArrayList<>();
		for (int eachValue: arr){
			int divisor = 10;
			while(divisor <= 1_000_000){
				if(eachValue/divisor > 0 && eachValue/divisor < 10){
					evenDigits.add(eachValue);
					break;
				}
				divisor *= 100;
			}
		}
		return evenDigits;
	}
}