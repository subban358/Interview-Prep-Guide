#include <iostream>
using namespace std;

int arr[1000000];


int main() {
	int n;
	cin >> n;
	while(n--){
	   int size, miss=1000000, rep=1000000;
	   cin >> size;
	   for(int i=0; i<size; i++){
	       cin >> arr[i];
	   }
	   for(int i=0;i<size;i++){
	       int idx = abs(arr[i])-1;
	       if(arr[idx]>=0) arr[idx] = (0-arr[idx]);
	       else rep=min(rep, abs(arr[i]));
	   }
	   for(int i=0; i<size; i++){
	       if(arr[i]>0) miss=min(miss, i+1);
	   }
	   cout << rep <<" " << miss << endl;
	}
	return 0;
}

------------------------------------------------------------------------------------------------------------------

def repeatedNumber(A): 
	
	length = len(A) 
	Sum_N = (length * (length + 1)) // 2
	Sum_NSq = ((length * (length + 1) * (2 * length + 1)) // 6) 
	
	missingNumber, repeating = 0, 0
	
	for i in range(len(A)): 
		Sum_N -= A[i] 
		Sum_NSq -= A[i] * A[i] 
		
	missingNumber = (Sum_N + Sum_NSq // Sum_N) // 2
	repeating = missingNumber - Sum_N 
	
	ans = [] 
	ans.append(repeating) 
	ans.append(missingNumber) 
	
	return ans 
	
v = [ 4, 3, 6, 2, 1, 6, 7 ] 
res = repeatedNumber(v) 

for i in res: 
	print(i, end = " ") 
