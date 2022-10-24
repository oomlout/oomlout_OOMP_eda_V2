
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "NetTie"
    oIndex = "NetTie-3_SMD_Pad2.0mm"
    hexID = "FZKNTNT3SMPAD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'NetTie-3_SMD_Pad2.0mm', 'description': 'Net tie, 3 pin, 2.0mm square SMD pads', 'tags': 'net tie', 'attributeType': None, 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('NetTie : NetTie-3_SMD_Pad2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

