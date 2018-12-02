def enough(cap, on, wait):
    if (cap-on<wait):
       return (on+wait)-cap
    return 0
