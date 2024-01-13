# module in python is a file with some python code. We use this to organize our code into files

import converters # (if you will call all codes)
print(converters.kg_to_lbs(70))

from converters import kg_to_lbs # if you will call a certain part

kg_to_lbs(100)

