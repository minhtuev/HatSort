
def hatSort(student):
    """ The magical working under the hat """
    
    if not student.magic():
        return "Hogwarts is not for Muggles"

    brave = student.brave()
    cunning = student.cunning()
    witty = student.witty()

    if (brave + cunning + witty > 1):
        return student.choice()

    if brave:
        return "Gryffindor!"
    elif cunning:
        return "Slytherine!"
    elif witty:
        return "Ravenclaw!"
    else:
        return "Hufflepuff!" 