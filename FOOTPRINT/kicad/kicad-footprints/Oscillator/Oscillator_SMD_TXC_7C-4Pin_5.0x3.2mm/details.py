
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_TXC_7C-4Pin_5.0x3.2mm"
    hexID = "FZKOCSOCSSMTXC7C4PIN5X32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_TXC_7C-4Pin_5.0x3.2mm', 'description': 'Miniature Crystal Clock Oscillator TXC 7C series, http://www.txccorp.com/download/products/osc/7C_o.pdf, 5.0x3.2mm^2 package', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_TXC_7C-4Pin_5.0x3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_TXC_7C-4Pin_5.0x3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

