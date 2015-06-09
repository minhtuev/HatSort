from student import Student
from hatSort import hatSort
from house import GRYFFINDOR, RAVENCLAW

harry = Student(magic=True, cunning=True, brave=True,choice=GRYFFINDOR)
print hatSort(harry)

draco = Student(magic=True, cunning=True)
print hatSort(draco)

petunia = Student()
print hatSort(petunia)

minhtue = Student(magic=True, brave=True, witty=True,choice=RAVENCLAW)
print hatSort(minhtue)