class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = ""
        for i in s.lower():
            if i.isalpha():
                arr +=i
            elif i.isnumeric():
                arr +=i
        n=len(arr)
        print(arr)
        if n%2 ==0:
            t=int(n/2)
            c=t
        else:
            t=int(n//2)
            c=t+1
        list1=arr[0:t]
        list2=arr[c:n]
        list2=list2[::-1]
        if list1 == list2:
            return True
        else:
            return False
