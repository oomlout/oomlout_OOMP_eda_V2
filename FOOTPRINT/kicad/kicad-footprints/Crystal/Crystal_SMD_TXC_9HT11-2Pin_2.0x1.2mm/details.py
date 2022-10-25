
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_TXC_9HT11-2Pin_2.0x1.2mm"
    hexID = "FZKXXSMTXC9HT112PIN2X12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_TXC_9HT11-2Pin_2.0x1.2mm', 'description': 'SMD Crystal TXC 9HT11 http://txccrystal.com/images/pdf/9ht11.pdf, 2.0x1.2mm^2 package', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_TXC_9HT11-2Pin_2.0x1.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_TXC_9HT11-2Pin_2.0x1.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

