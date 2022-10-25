
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "TO-263-9_TabPin5"
    hexID = "FZKPACKAGETOSOTSMTO2639TABPIN5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-263-9_TabPin5', 'description': 'TO-263 / D2PAK / DDPAK SMD package, http://www.ti.com/lit/ds/symlink/lm4755.pdf', 'tags': 'D2PAK DDPAK TO-263 D2PAK-9 TO-263-9', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TO-263-9_TabPin5.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : TO-263-9_TabPin5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

