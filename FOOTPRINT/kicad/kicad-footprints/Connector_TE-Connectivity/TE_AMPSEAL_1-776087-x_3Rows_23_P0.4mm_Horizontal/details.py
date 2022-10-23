
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_TE-Connectivity"
    oIndex = "TE_AMPSEAL_1-776087-x_3Rows_23_P0.4mm_Horizontal"
    hexID = "FZKCNTECONNECTIVITYTEAMPSEAL177687X3ROWS23P4HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_AMPSEAL_1-776087-x_3Rows_23_P0.4mm_Horizontal', 'description': 'Connector', 'tags': 'TE 776087', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_TE-Connectivity.3dshapes/TE_AMPSEAL_1-776087-x_3Rows_23_P0.4mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_TE-Connectivity : TE_AMPSEAL_1-776087-x_3Rows_23_P0.4mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

