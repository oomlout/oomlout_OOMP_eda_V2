
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Wuerth"
    oIndex = "Wuerth_WR-WTB_64800611622_1x06_P1.50mm_Vertical"
    hexID = "FZKCNWUERTHWUERTHWRWTB6486116221X6P15VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wuerth_WR-WTB_64800611622_1x06_P1.50mm_Vertical', 'description': 'Wuerth WR-WTB series connector, 64800611622 (https://katalog.we-online.com/em/datasheet/6480xx11622.pdf), generated with kicad-footprint-generator', 'tags': 'connector Wuerth WR-WTB vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Wuerth.3dshapes/Wuerth_WR-WTB_64800611622_1x06_P1.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Wuerth : Wuerth_WR-WTB_64800611622_1x06_P1.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

