#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int binarySearch(int arr[], int firstIndex, int lastIndex, int target)
{
  int size = (lastIndex - firstIndex);
  int mid = size / 2;

  if (firstIndex <= lastIndex)
  {
    int mindex = firstIndex + mid;

    if (arr[mindex] == target)
    {
      return 1;
    }
    else if (arr[mindex] > target)
    {
      binarySearch(arr, firstIndex, mindex - 1, target);
    }
    else
      binarySearch(arr, mindex + 1, lastIndex, target);
  }

  return 0;
}

int main()
{
  int n;
  int *list;
  int i, j, temp = 0;
  int target;

  printf("자연수 N을 입력하시오: ");
  scanf("%d", &n);

  list = (int *)malloc(sizeof(int) * n);

  srand((unsigned int)time(NULL));

  printf("생성된 난수들: ");
  for (i = 0; i < n; i++)
  {
    list[i] = rand() % 101;
    printf("%d ", list[i]);
  }
  printf("\n");

  for (i = 0; i < n - 1; i++)
  {
    for (j = 0; j < n - i - 1; j++)
    {
      if (list[j] > list[j + 1])
      {
        temp = list[j];
        list[j] = list[j + 1];
        list[j + 1] = temp;
      }
    }
  }

  printf("정렬결과: ");
  for (i = 0; i < n; i++)
    printf("%d ", list[i]);
  printf("\n");

  printf("찾고자 하는 임의의 정수를 입력하시오: ");
  scanf("%d", &target);

  if (binarySearch(list, 0, n, target) == 1)
  {
    printf("입력받은 정수가 존재합니다");
  }
  else
  {
    printf("입력받은 정수가 없습니다");
  }

  free(list);
}