
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_GCT_DCJ200-10-A_Horizontal"
    hexID = "FZKCNBARRELJBARRELJGCTDCJ21AHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_GCT_DCJ200-10-A_Horizontal', 'description': 'Barrel jack connector (5.5 mm outer diameter, 2.05 inner diameter ), https://gct.co/files/drawings/dcj200-10.pdf', 'tags': 'connector barrel jack', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_GCT_DCJ200-10-A_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_GCT_DCJ200-10-A_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

