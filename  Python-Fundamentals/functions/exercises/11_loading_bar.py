def bar(number):
    loading = ["."] * 10
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        for char_index in range(int(number / 10)):
            loading[char_index] = "%"
        print(f"{number}% [{''.join(loading)}]")
        print("Still loading...")


number = int(input())

bar(number)