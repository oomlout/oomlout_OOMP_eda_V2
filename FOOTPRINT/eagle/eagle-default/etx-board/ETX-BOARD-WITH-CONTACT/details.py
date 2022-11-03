
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "eagle"
    oColor = "eagle-default"
    oDesc = "etx-board"
    oIndex = "ETX-BOARD-WITH-CONTACT"
    hexID = "FZEETXBOARDETXBOARDWITHCONTACT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('etx-board : ETX-BOARD-WITH-CONTACT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

