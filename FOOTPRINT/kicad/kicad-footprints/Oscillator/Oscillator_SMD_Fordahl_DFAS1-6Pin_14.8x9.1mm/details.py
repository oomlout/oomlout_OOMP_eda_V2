
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Fordahl_DFAS1-6Pin_14.8x9.1mm"
    hexID = "FZKOCSOCSSMFORDAHLDFAS16PIN148X91"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Fordahl_DFAS1-6Pin_14.8x9.1mm', 'description': 'Miniature Crystal Clock Oscillator TXCO Fordahl DFA S1-KHZ/LHZ, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, 14.8x9.1mm^2 package', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Fordahl_DFAS1-6Pin_14.8x9.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Fordahl_DFAS1-6Pin_14.8x9.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

