
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_DIP-8_LargePads"
    hexID = "FZKOCSOCSDIP8LPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_DIP-8_LargePads', 'description': 'Oscillator, DIP8, Large Pads, http://cdn-reichelt.de/documents/datenblatt/B400/OSZI.pdf', 'tags': 'oscillator', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_DIP-8.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_DIP-8_LargePads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

