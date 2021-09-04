import sklearn as sk
import sys
from  sklearn.ensemble import RandomForestClassifier

import  python_function

from  python_fibonacci import fibonacci
print(sk.__version__)
print(sys.path)
print(RandomForestClassifier())

python_function.functionTwo(5,7)

print(fibonacci(7))