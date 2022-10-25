
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_3215-2Pin_3.2x1.5mm"
    hexID = "FZKXXSM32152PIN32X15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_3215-2Pin_3.2x1.5mm', 'description': 'SMD Crystal FC-135 https://support.epson.biz/td/api/doc_check.php?dl=brief_FC-135R_en.pdf', 'tags': 'SMD SMT Crystal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_3215-2Pin_3.2x1.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_3215-2Pin_3.2x1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

