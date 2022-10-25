
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_OCXO_ConnorWinfield_OH300"
    hexID = "FZKOCSOCSSMOCXOCONNORWINFIELDOH3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_OCXO_ConnorWinfield_OH300', 'description': 'http://www.conwin.com/datasheets/cx/cx282.pdf', 'tags': 'OCXO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_OCXO_ConnorWinfield_OH300.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_OCXO_ConnorWinfield_OH300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

