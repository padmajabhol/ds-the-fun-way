#include <stdio.h>
#include <math.h>

int binarySearch(int A[], int n, int target){
  int indexHigh = n - 1;
  int indexLow = 0;
  int midIndex;
  while(indexLow <= indexHigh){
    midIndex = round((indexHigh + indexLow)/2);
    if (A[midIndex] == target){
      return midIndex;
    }
    if (A[midIndex] < target){
      indexLow = midIndex + 1;
    }
    else{
      indexHigh = midIndex - 1;
    }
  }
  return -1;
}

int main(){
  int A[] = {8,9,2,3,4};
  int n = sizeof(A)/sizeof(A[0]);
  int target = 3;

  printf("%d", binarySearch(A, n, target));

};
