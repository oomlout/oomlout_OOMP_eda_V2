
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_SMD_ECS_CSM3X-2Pin_7.6x4.1mm"
    hexID = "FZKXXSMECSCSM3X2PIN76X41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_SMD_ECS_CSM3X-2Pin_7.6x4.1mm', 'description': 'http://www.ecsxtal.com/store/pdf/CSM-3X.pdf', 'tags': 'Crystal CSM-3X', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_ECS_CSM3X-2Pin_7.6x4.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Crystal_SMD_ECS_CSM3X-2Pin_7.6x4.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

