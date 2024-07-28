if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) # Transformado o objeto map em lista
    
    new_list = sorted(set(arr), reverse=True)
    print(new_list[1])
    