
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Display"
    oIndex = "AG12864E"
    hexID = "FZKDIAG12864E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AG12864E', 'description': 'STN/FSTN LCD 128x64 dot https://www.digchip.com/datasheets/parts/datasheet/1121/AG-12864E-pdf.php', 'tags': 'AG12864E Graphics Display 128x64 Ampire', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Display.3dshapes/AG12864E.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Display : AG12864E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

