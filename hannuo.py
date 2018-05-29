count = 0


def move(n, From, Buf, To):
    global count
    if n == 1:
        count += 1
        print(str(count)+'. Move from', From, 'to', To)

    else:
        move(n-1, From, To, Buf)    #把除了最大的环之外的环从From移动到Buf
        move(1, From, Buf, To)      #将最大的环从From移动到To
        move(n-1, Buf, From, To)    #把除了最大的环之外的环从Buf移动到To


def main():
    n = int(input('汉诺塔层数：'))
    move(n, 'A', 'B', 'C')
    print('\n共 '+str(count)+' 步')


if __name__ == '__main__':
    main()
