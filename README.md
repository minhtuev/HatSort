# HatSort
The inner working of Hogwarts' mysterious Sorting Hat

```python
harry = Student(name="Harry", magic=True, cunning=True, brave=True, choice=GRYFFINDOR)
print hatSort(harry)
```

```bash
>> Sorting Harry...
>> Gryffindor
```

```python
petunia = Student(name="Petunia")
print hatSort(petunia)
```

```bash
>> Sorting Petunia...
>> Hogwarts is not for Muggles
```

```python
aaron = Student(name="Aaron", boxer=True, brave=True, witty=True, choice=GRYFFINDOR)
print hatSort(aaron)
```

```bash
>> Sorting Aaron...
>> Unicorns are welcomed at Hogwarts
>> Gryffindor
```

```python
beaver = Student(name="beaver", MIT=True, brave=True, witty=True,choice=RAVENCLAW)
print hatSort(beaver)
```

```bash
>> Sorting beaver...
>> Hogwarts - MIT exchange programme. Welcome!
>> Ravenclaw
```