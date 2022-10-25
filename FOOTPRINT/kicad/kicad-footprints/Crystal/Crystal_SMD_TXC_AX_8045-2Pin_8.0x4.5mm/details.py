
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_TXC_AX_8045-2Pin_8.0x4.5mm"
    hexID = "FZKXXSMTXCAX8452PIN8X45"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_TXC_AX_8045-2Pin_8.0x4.5mm', 'description': 'http://www.txccrystal.com/images/pdf/ax-automotive.pdf', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_TXC_AX_8045-2Pin_8.0x4.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Crystal : Crystal_SMD_TXC_AX_8045-2Pin_8.0x4.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

