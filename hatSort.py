from house import GRYFFINDOR, SLYTHERINE, RAVENCLAW, HUFFLEPUFF

def hatSort(student):
    """ The magical working under the hat """
    
    print ("Sorting " + str(student))
    if not (student.magic or student.MIT or student.boxer):
        return "Hogwarts is not for Muggles"

    if student.MIT:
        print ("Hogwarts - MIT exchange programme. Welcome!")
    elif student.boxer:
        print ("Unicorns are welcomed at Hogwarts")

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