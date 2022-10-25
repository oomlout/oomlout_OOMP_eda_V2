
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "HDSP-A151"
    hexID = "FZKDI7SHDSPA151"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HDSP-A151', 'description': 'One digit 7 segment red, https://docs.broadcom.com/docs/AV02-2553EN', 'tags': 'One digit 7 segment high efficiency red', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/HDSP-A151.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : HDSP-A151')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

