def extractAreacode(no, d):
    return int(no//pow(10, d-1))%10

def funSort(list,numberofphones, digitpos,maxdigits):

    if digitpos > maxdigits:
        return
    #@start-editable@

    l_list = len(list)
    temp = [0] * (l_list)
    count = [0] * (10)
    for i in range(0, l_list):
        a_code = extractAreacode(list[i], digitpos)
        count[int(a_code % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
        i = l_list - 1
    while i >= 0:
        a_code = extractAreacode(list[i], digitpos)
        temp[count[int(a_code % 10)] - 1] = list[i]
        count[int(a_code % 10)] = count[int(a_code % 10)]-1
        i=i-1
    i = 0
    for i in range(0, len(list)):
        list[i] = temp[i]
    print(list)            
    funSort(list,numberofphones,digitpos+1,maxdigits)

    #@end-editable@
    
    

def getPhoneNumbers():
    phone = []
    noOfElements = int(input())
    while noOfElements > 0:
        element=int(input())
        phone.append(element)
        noOfElements-=1
    funSort(phone,len(phone), 6,7)

def main():
    getPhoneNumbers()
    
if __name__ == '__main__':
    main()