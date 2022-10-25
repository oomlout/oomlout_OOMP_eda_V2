
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Polarity_Center_Positive_8mm_SilkScreen"
    hexID = "FZKSZPOLARITYCENTERPOSITIVE8SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Polarity_Center_Positive_8mm_SilkScreen', 'description': 'Polarity Logo, Center Positive', 'tags': 'Logo Polarity Center Positive', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Polarity_Center_Positive_8mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

