
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_AMASS"
    oIndex = "AMASS_XT30U-M_1x02_P5.0mm_Vertical"
    hexID = "FZKCNAMASSAMASSXT3UM1X2P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AMASS_XT30U-M_1x02_P5.0mm_Vertical', 'description': 'Connector XT30 Vertical Cable Male, https://www.tme.eu/en/Document/3cbfa5cfa544d79584972dd5234a409e/XT30U%20SPEC.pdf', 'tags': 'RC Connector XT30', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_AMASS.3dshapes/AMASS_XT30U-M_1x02_P5.0mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_AMASS : AMASS_XT30U-M_1x02_P5.0mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

