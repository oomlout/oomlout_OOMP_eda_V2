
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering"
    hexID = "FZKLGABOSCHLGA825X25P65CLWISEPINNUMBERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering', 'description': 'LGA-8', 'tags': 'lga land grid array', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_LGA : Bosch_LGA-8_2.5x2.5mm_P0.65mm_ClockwisePinNumbering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

