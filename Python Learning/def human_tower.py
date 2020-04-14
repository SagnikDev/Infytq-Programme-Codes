def human_tower(no_of_humans):
    if(no_of_humans==1):
        return 1*50
    else:
        return no_of_humans*50+human_tower(no_of_humans-2)

print(human_tower(5))