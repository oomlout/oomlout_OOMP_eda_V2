
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Kyocera_2520-6Pin_2.5x2.0mm"
    hexID = "FZKOCSOCSSMKYOCERA2526PIN25X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Kyocera_2520-6Pin_2.5x2.0mm', 'description': 'https://global.kyocera.com/prdct/electro/product/pdf/kt2520_e.pdf', 'tags': '2.5mm 2mm SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Kyocera_2520-6Pin_2.5x2.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Kyocera_2520-6Pin_2.5x2.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

