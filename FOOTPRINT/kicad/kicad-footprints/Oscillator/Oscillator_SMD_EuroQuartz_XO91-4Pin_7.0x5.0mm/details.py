
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm"
    hexID = "FZKOCSOCSSMEUROQUARTZXO914PIN7X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm', 'description': 'Miniature Crystal Clock Oscillator EuroQuartz XO91 series, http://cdn-reichelt.de/documents/datenblatt/B400/XO91.pdf, 7.0x5.0mm^2 package', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

