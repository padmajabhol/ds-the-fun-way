#include <stdio.h>

int linearSearch(int A[], int target, int n){
  int i = 0;
  while(i < n){
    if (A[i] == target){
      return i;
    }
    i += 1;
  }
  return -1;
}

int main(){
  int A[] = {4,3,6,1,7,8};
  int target = 1;
  int n = sizeof(A)/sizeof(A[0]);

  printf("%d",linearSearch(A, target, n));

  
}

