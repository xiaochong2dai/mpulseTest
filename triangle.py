def triangle(n):
    s=''
    for i in range(0, n):
        if i < n - 1:
            for j in range(0, 2*n+1): 
                if j == (n - i - 1):
                    s = s + '/'
                elif j == (n + i + 1):
                    s = s + '\\'
                else:
                    s = s + ' '
            s = s + '\n'
        else:
            for j in range(0, 2*n+1):
                if j == 0:
                    s =s + '/'
                elif j == 2*n:
                    s =s + '\\'
                elif j%2 == 1:
                    s = s + '_'
                else:
                    s= s + ' '
            s = s + '\n'
    print s
if __name__=="__main__":
    while True:
        n = input("please input triangle length: ")
        try:
            n = int(n)
            if n < 0:
                print ("Sorry, input must be a positive integer, please try again.")
                continue
            break
        except ValueError:
            print("Input should be an integer.")
    triangle(n)
