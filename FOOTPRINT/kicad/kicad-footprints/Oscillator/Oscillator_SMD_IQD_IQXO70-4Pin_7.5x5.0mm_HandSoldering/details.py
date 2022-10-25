
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm_HandSoldering"
    hexID = "FZKOCSOCSSMIQDIQXO74PIN75X5HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm_HandSoldering', 'description': 'IQD Crystal Clock Oscillator IQXO-70, http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf, hand-soldering, 7.5x5.0mm^2 package', 'tags': 'SMD SMT crystal oscillator hand-soldering', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm_HandSoldering.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

