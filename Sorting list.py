def sort_numbers(n):
    for i in range(len(n)):
        for j in range(0,i+1):
            if(n[i]<n[j]):
                n[i],n[j]=n[j],n[i]       
    return n
a=eval(input("Enter numbers:"))
x=list(a)
print("Given list:",x)
print("Sorted list:",sort_numbers(x))
