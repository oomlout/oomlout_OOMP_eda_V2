
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_DIP-14"
    hexID = "FZKOCSOCSDIP14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_DIP-14', 'description': 'Oscillator, DIP14, http://cdn-reichelt.de/documents/datenblatt/B400/OSZI.pdf', 'tags': 'oscillator', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_DIP-14.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_DIP-14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

