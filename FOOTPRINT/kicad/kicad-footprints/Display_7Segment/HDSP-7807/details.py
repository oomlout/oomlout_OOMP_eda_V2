
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "HDSP-7807"
    hexID = "FZKDI7SHDSP787"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDSP-7807', 'description': '+-1 overflow 7 segment green, https://docs.broadcom.com/docs/AV02-2553EN', 'tags': '+-1 overflow 7 segment green', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/HDSP-7807.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : HDSP-7807')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

