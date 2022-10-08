def solution(files):
    answer = []
    arr=[]
    loc=[0, 0]

    #1. 숫자이거나, 스트링 끝이면 자름
    #2. 문자이거나, 스트링 끝이면 자름
    
    for i in files:
        sliced=0
        loc=[0, 0]
        for j in range(len(i)):
            if sliced:
                if i[j].isdigit()==False:
                    sliced=2
                    loc[1]=j
                    break
            else:  
                if i[j].isdigit():
                    sliced=1
                    loc[0]=j
        print(loc, sliced)
        if sliced==0:
            arr.append([i,"",""])
        elif sliced==1:
            arr.append([i[:loc[0]], i[loc[0]:],""])
        else:
            arr.append([i[:loc[0]], i[loc[0]:loc[1]], i[loc[1]:]])
        
        print(arr)
                
    
    #헤드가 같은 경우 넘버로 정렬
    arr.sort(key= lambda x : (x[0].lower(), int(x[1])))#??
    
    print(arr)

    #합쳐서 출력
    for i in range(len(arr)):
        arr[i]=''.join(arr[i])
    
    return arr


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print()
print()
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))