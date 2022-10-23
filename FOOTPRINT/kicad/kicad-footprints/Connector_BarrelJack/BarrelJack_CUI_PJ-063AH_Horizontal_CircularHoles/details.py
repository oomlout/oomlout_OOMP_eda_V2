
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_BarrelJack"
    oIndex = "BarrelJack_CUI_PJ-063AH_Horizontal_CircularHoles"
    hexID = "FZKCNBARRELJBARRELJCUIPJ63AHHORIZONTALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BarrelJack_CUI_PJ-063AH_Horizontal_CircularHoles', 'description': 'Barrel Jack, 2.0mm ID, 5.5mm OD, 24V, 8A, no switch, https://www.cui.com/product/resource/pj-063ah.pdf', 'tags': 'barrel jack cui dc power', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_BarrelJack.3dshapes/BarrelJack_CUI_PJ-063AH_Horizontal_CircularHoles.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_BarrelJack : BarrelJack_CUI_PJ-063AH_Horizontal_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

