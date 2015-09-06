from student import Student
from hatSort import hatSort
from house import GRYFFINDOR, RAVENCLAW

harry = Student(name="Harry", magic=True, cunning=True, brave=True, choice=GRYFFINDOR)
print hatSort(harry)

draco = Student(name="Dracgo", magic=True, cunning=True)
print hatSort(draco)

petunia = Student(name="Petunia")
print hatSort(petunia)

aaron = Student(name="Aaron", boxer=True, brave=True, witty=True, choice=GRYFFINDOR)
print hatSort(aaron)

beaver = Student(name="beaver", MIT=True, brave=True, witty=True,choice=RAVENCLAW)
print hatSort(beaver)