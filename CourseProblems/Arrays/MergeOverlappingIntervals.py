def mergeOverlappingIntervals(intervals):   
    return intervals[-1]
    #return sorted(intervals, key=lambda x:x[0])

intervals = [[3,4],[1,2]]
print(mergeOverlappingIntervals(intervals))