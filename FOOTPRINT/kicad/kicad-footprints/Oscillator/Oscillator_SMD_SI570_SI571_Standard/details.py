
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_SI570_SI571_Standard"
    hexID = "FZKOCSOCSSMSI57SI571STANDARD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_SI570_SI571_Standard', 'description': 'SI570, SI571, Programmable oscillator, Standard', 'tags': 'SI570 SI571 Programmable oscillator Standard', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_SI570_SI571_Standard.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_SI570_SI571_Standard')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

