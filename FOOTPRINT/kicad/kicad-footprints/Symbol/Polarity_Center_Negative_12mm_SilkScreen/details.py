
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Polarity_Center_Negative_12mm_SilkScreen"
    hexID = "FZKSZPOLARITYCENTERNEGATIVE12SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Polarity_Center_Negative_12mm_SilkScreen', 'description': 'Polarity Logo, Center Negative', 'tags': 'Logo Polarity Center Negative', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Polarity_Center_Negative_12mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

