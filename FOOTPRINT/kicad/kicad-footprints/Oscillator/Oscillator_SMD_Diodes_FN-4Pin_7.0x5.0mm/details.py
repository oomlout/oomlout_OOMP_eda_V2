
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Diodes_FN-4Pin_7.0x5.0mm"
    hexID = "FZKOCSOCSSMDIODESFN4PIN7X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Diodes_FN-4Pin_7.0x5.0mm', 'description': 'FN Series Crystal Clock Oscillator (XO) (https://www.diodes.com/assets/Datasheets/FN_3-3V.pdf)', 'tags': 'Oscillator Crystal SMD SMT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Diodes_FN-4Pin_7.0x5.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Diodes_FN-4Pin_7.0x5.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

