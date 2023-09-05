def my_levenshtein(param_1,param_2):
    index=0
    if len(param_1)==len(param_2):
        for i in range(len(param_2)):
            if(param_1[i]!=param_2[i]):
                index+=1
        return index
    else:
        return -1