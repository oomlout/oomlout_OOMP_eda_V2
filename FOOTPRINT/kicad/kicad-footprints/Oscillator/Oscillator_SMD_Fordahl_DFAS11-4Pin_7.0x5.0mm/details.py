
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Fordahl_DFAS11-4Pin_7.0x5.0mm"
    hexID = "FZKOCSOCSSMFORDAHLDFAS114PIN7X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Fordahl_DFAS11-4Pin_7.0x5.0mm', 'description': 'Miniature Crystal Clock Oscillator TXCO Fordahl DFA S11-OV/UOV, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, 7.0x5.0mm^2 package', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Fordahl_DFAS11-4Pin_7.0x5.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Fordahl_DFAS11-4Pin_7.0x5.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

