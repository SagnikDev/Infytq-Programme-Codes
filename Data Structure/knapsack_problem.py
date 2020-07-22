objects=[0,1,2,3,4,5,6]
profit=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
n=7
m=15
knapsack={}
profit_weight=[profit[i]/weight[i] for i in range(0,len(objects))]

max_profit_weight=max(profit_weight)
index_of_max=profit_weight.index(max_profit_weight)
weight_of_max=weight[index_of_max]
profit_weight[index_of_max]=-1


while(weight_of_max<=m and weight_of_max!=-1):
    knapsack[index_of_max]=1
    m-=weight_of_max
    max_profit_weight=max(profit_weight)
    index_of_max=profit_weight.index(max_profit_weight)
    weight_of_max=weight[index_of_max]
    profit_weight[index_of_max]=-1


if(m>1 and weight_of_max!=-1):
    knapsack[index_of_max]=m/weight_of_max


print("Total Weight")
total_weight=0
for i,j in knapsack.items():
    total_weight+=(j*weight[i])
print(total_weight)

print("Total Sum")
total_profit=0
for i,j in knapsack.items():
    total_profit+=(j*profit[i])
print(total_profit)