#include <stdio.h>

void insertionSort(int A[], int n){
    int i = 1;
    while(i < n){
        int current = A[i];
        int j = i - 1;
        while(j >= 0 && A[j] > current){
            A[j+1] = A[j];
            j = j - 1;
        }
        A[j+1] = current;
        i = i + 1;
    }
}

int main(){
    int A[] = {6,8,1,2,5};
    int n = sizeof(A)/sizeof(A[0]);

    insertionSort(A, n);

    for(int i = 0; i < n; i++){
        printf("%d ", A[i]);
    }
    printf("\n");

    return 0;
}
