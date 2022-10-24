
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "FCC-Logo_9.6x8mm_SilkScreen"
    hexID = "FZKSZFCCL96X8SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'FCC-Logo_9.6x8mm_SilkScreen', 'description': 'FCC marking', 'tags': 'Logo FCC certification', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : FCC-Logo_9.6x8mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

