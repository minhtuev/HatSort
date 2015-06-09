from house import GRYFFINDOR, SLYTHERINE, RAVENCLAW, HUFFLEPUFF

def hatSort(student):
    """ The magical working under the hat """
    
    if not student.magic:
        return "Hogwarts is not for Muggles"

    brave = student.brave
    cunning = student.cunning
    witty = student.witty

    if (brave + cunning + witty > 1):
        return student.choice

    if brave:
        return GRYFFINDOR
    elif cunning:
        return SLYTHERINE
    elif witty:
        return RAVENCLAW
    else:
        return HUFFLEPUFF