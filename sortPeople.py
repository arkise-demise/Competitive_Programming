class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = dict(zip(heights,names))
        names.clear()
        for key in sorted(height_dict.keys(),reverse=True):
            names.append(height_dict[key])
        return names
        # or simply we can do as foolows
        # a=zip(heights,names)
        # l=[]
        # for i,j in sorted(a):
        #     l.append(j)
        # return l[::-1]