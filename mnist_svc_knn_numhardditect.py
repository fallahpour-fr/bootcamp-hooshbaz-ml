# Function that find the number of misdiagnosis in pair number
import numpy as np
def numberhardditect(pair_info):  
   seccond_dict=np.array(list(pair_info.items()),dtype=object)
   if seccond_dict[2][1] >=10 and seccond_dict[3][1] >=10:
      c=f'in model {seccond_dict[0][1]} , {seccond_dict[0][1][0]} and {seccond_dict[0][1][1]} hard to detect'
      return c
   else:
        if seccond_dict[2][1] >=10:
            b=f'in model {seccond_dict[0][1]} , {seccond_dict[0][1][0]} hard to detect for {seccond_dict[2][1]} times'
            return b
        if seccond_dict[3][1] >=10:
            a=f'in model {seccond_dict[0][1]} , {seccond_dict[0][1][1]} hard to detect for {seccond_dict[3][1]} times'   
            return a
        else:
          return 1   
