
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Fordahl_DFAS7-4Pin_19.9x12.9mm"
    hexID = "FZKOCSOCSSMFORDAHLDFAS74PIN199X129"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Fordahl_DFAS7-4Pin_19.9x12.9mm', 'description': 'Miniature Crystal Clock Oscillator TXCO Fordahl DFA S7-K/L, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, 19.9x12.9mm^2 package', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Fordahl_DFAS7-4Pin_19.9x12.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Fordahl_DFAS7-4Pin_19.9x12.9mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

