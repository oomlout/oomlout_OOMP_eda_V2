
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "FB-BGA-484_23.0x23.0mm_Layout22x22_P1.0mm"
    hexID = "FZKBGAFBBGA48423X23LAYOUT22X22P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'FB-BGA-484_23.0x23.0mm_Layout22x22_P1.0mm', 'description': 'Xilinx FB-484, https://www.xilinx.com/support/documentation/user_guides/ug1099-bga-device-design-rules.pdf', 'tags': 'FB-BGA-484', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-484_23.0x23.0mm_Layout22x22_P1.0mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : FB-BGA-484_23.0x23.0mm_Layout22x22_P1.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

