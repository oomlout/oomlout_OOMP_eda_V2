
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_Wuerth_6941xx301002"
    hexID = "FZKCNBARRELJBARRELJWUERTH6941XX312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_Wuerth_6941xx301002', 'description': 'Wuerth electronics barrel jack connector (5.5mm outher diameter, inner diameter 2.05mm or 2.55mm depending on exact order number), See: http://katalog.we-online.de/em/datasheet/6941xx301002.pdf', 'tags': 'connector barrel jack', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_Wuerth_6941xx301002.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_Wuerth_6941xx301002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

