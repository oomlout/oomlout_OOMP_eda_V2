
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "QFN-20-1EP_3x3mm"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSQFN21EP3X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-20-1EP_3x3mm', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : QFN-20-1EP_3x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

