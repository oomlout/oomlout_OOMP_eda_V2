
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_Qantek_QC5CB-2Pin_5x3.2mm"
    hexID = "FZKXXSMQANTEKQC5CB2PIN5X32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_Qantek_QC5CB-2Pin_5x3.2mm', 'description': 'SMD Crystal Qantek QC5CB, https://www.qantek.com/tl_files/products/crystals/QC5CB.pdf', 'tags': 'SMD SMT crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_Qantek_QC5CB-2Pin_5x3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_Qantek_QC5CB-2Pin_5x3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

