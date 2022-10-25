
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "TO-263-3_TabPin4"
    hexID = "FZKPACKAGETOSOTSMTO2633TABPIN4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-263-3_TabPin4', 'description': 'TO-263 / D2PAK / DDPAK SMD package, http://www.infineon.com/cms/en/product/packages/PG-TO263/PG-TO263-3-1/', 'tags': 'D2PAK DDPAK TO-263 D2PAK-3 TO-263-3 SOT-404', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TO-263-3_TabPin4.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : TO-263-3_TabPin4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

