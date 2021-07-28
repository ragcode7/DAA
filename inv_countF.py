#https://www.geeksforgeeks.org/counting-inversions/
def solution(arr, n):
	arr_temp = [0]*n #temporary array to store sorted array
	return mergeSort(arr, arr_temp, 0, n-1)
	
#merge sort technique (sort, divide) to count the number the count inversions
def mergeSort(arr, arr_temp, arr_left, arr_right):
	count = 0 
	if arr_left < arr_right:
		mid = (arr_left + arr_right)//2
		count += mergeSort(arr, arr_temp, arr_left, mid)
		count += mergeSort(arr, arr_temp, mid + 1, arr_right)
		count += merge(arr, arr_temp, arr_left, mid, arr_right)
	return count
	
#in order to merge the subarrays into a single sorted one	
def merge(arr, arr_temp, arr_left, mid, arr_right):
	l = arr_left	 
	m = mid + 1 
	k = arr_left	 
	count = 0
	while l <= mid and m <= arr_right:
		if arr[l] <= arr[m]:
			arr_temp[k] = arr[l]
			k = k+ 1
			l = l+ 1
		else:
			arr_temp[k] = arr[m]
			count += (mid-l + 1)
			k = k+ 1
			m = m+ 1
	while l <= mid:
		arr_temp[k] = arr[l]
		k = k+ 1
		l = l+ 1
	while m <= arr_right:
		arr_temp[k] = arr[m]
		k = k+ 1
		m = m+ 1
	for i in range(arr_left, arr_right + 1):
		arr[i] = arr_temp[i]
		
	return count

def main():
    arraysize=int(input())
    arr=list(map(int,input().split(",")))
    count=solution(arr,arraysize)
    print(count)

if __name__=='__main__':
    main()
