
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "Maxim_WLCSP-35_3.0x2.17mm_Layout7x5_P0.4mm_Ball0.27mm_Pad0.25mm"
    hexID = "FZKCSPMAXIMWLCSP353X217LAYOUT7X5P4BALL27PAD25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Maxim_WLCSP-35_3.0x2.17mm_Layout7x5_P0.4mm_Ball0.27mm_Pad0.25mm', 'description': 'WLCSP-35, 2.168x2.998mm, 35 Ball, 7x5 Layout, 0.4mm Pitch, https://pdfserv.maximintegrated.com/package_dwgs/21-100489.PDF', 'tags': 'CSP 35 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/Maxim_WLCSP-35_3.0x2.17mm_Layout7x5_P0.4mm_Ball0.27mm_Pad0.25mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : Maxim_WLCSP-35_3.0x2.17mm_Layout7x5_P0.4mm_Ball0.27mm_Pad0.25mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

