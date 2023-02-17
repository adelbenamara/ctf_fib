import json

# Open the JSON file and read its contents
with open('/home/adel/Documents/hacking/data.json', 'r') as f:
    data = json.load(f)




# s= data[]['_source']['layers']['tcp']['tcp.seq']
# s=  chr(int(s, 16))
# print(s)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

data_length = len(data)

for i in range(data_length):
    fib_i = fibonacci(i)
    
    if fib_i >= data_length:
        break  # stop the loop if the Fibonacci number is larger than the data length

    if data[i]['_source']['layers']['tcp']['tcp.seq'] == fib_i:

            s = data[i]['_source']['layers']['data']['data.data']
            s_ascii = chr(int(s, 16))
            print(s_ascii)
            print(fib_i)



# for i in range(data_length):
#     fib_i = fibonacci(i)
#     print(fib_i,i)  