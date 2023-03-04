# The first line contains . The second line contains an array   of  integers each separated by a space.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))

    # Sort the list in descending order
    arr.sort(reverse=True)

    # Print the second element of the list
    print(arr[1])