# # to get odd elements

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

i = 1
# for item in l1:
#     if i%2 is not 0:
#         print(f"Jarvis please buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if index%2==0:      # # index of bhindi is 0 which want
        print(f"Zuckerberg please buy {item}")
