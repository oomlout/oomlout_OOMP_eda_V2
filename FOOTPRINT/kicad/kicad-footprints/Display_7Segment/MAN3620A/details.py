
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display_7Segment"
    oIndex = "MAN3620A"
    hexID = "FZKDI7SMAN362A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MAN3620A', 'description': 'https://www.digchip.com/datasheets/parts/datasheet/161/MAN3640A-pdf.php', 'tags': 'One digit 7 segment orange LED with left dot', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display_7Segment.3dshapes/MAN3620A.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Display_7Segment : MAN3620A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

