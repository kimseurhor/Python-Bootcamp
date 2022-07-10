def p(k,i,m):
    print(f"make_list({k},'{i}',{m})")
    return k,i,m
make_list = (p(21,'hello',45))
print(list(make_list))