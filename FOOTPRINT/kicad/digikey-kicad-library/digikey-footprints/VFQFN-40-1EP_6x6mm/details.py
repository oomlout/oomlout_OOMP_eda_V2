
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "VFQFN-40-1EP_6x6mm"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSVFQFN41EP6X6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VFQFN-40-1EP_6x6mm', 'description': 'http://www.ti.com/lit/ds/symlink/cc2650.pdf', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : VFQFN-40-1EP_6x6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

