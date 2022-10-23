
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Card"
    oIndex = "microSD_HC_Hirose_DM3BT-DSF-PEJS"
    hexID = "FZKCNCARDMSDHCHIROSEDM3BTDSFPEJS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'microSD_HC_Hirose_DM3BT-DSF-PEJS', 'description': 'Micro SD, SMD, reverse on-board, right-angle, push-pull (https://www.hirose.com/product/en/download_file/key_name/DM3BT-DSF-PEJS/category/Drawing%20(2D)/doc_file_id/44097/?file_category_id=6&item_id=06090029900&is_series=)', 'tags': 'Micro SD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Card.3dshapes/microSD_HC_Hirose_DM3BT-DSF-PEJS.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Card : microSD_HC_Hirose_DM3BT-DSF-PEJS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

