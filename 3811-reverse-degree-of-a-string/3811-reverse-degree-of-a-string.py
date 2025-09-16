class Solution:
    def reverseDegree(self, s: str) -> int:
        my_str_list=list(s)
        my_alpha=list("abcdefghijklmnopqrstuvwxyz")
        rev_index=[i for i in range(26,0,-1)]
        my_aplha_dic=dict(zip(my_alpha,rev_index))
        str_dic=dict(enumerate(my_str_list,start=1))
        count=0
        for i in str_dic:
            val=str_dic[i]
            if val in my_aplha_dic:
                count+=i*my_aplha_dic[val]
        return count        



        
