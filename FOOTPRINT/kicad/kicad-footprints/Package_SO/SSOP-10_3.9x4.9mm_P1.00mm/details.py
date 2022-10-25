
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-10_3.9x4.9mm_P1.00mm"
    hexID = "FZKSOSS139X49P1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-10_3.9x4.9mm_P1.00mm', 'description': '10-Lead SSOP, 3.9 x 4.9mm body, 1.00mm pitch (http://www.st.com/resource/en/datasheet/viper01.pdf)', 'tags': 'SSOP 3.9 4.9 1.00', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-10_3.9x4.9mm_P1.00mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-10_3.9x4.9mm_P1.00mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

