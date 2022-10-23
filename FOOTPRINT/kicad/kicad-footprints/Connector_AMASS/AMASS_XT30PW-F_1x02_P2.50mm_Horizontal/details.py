
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_AMASS"
    oIndex = "AMASS_XT30PW-F_1x02_P2.50mm_Horizontal"
    hexID = "FZKCNAMASSAMASSXT3PWF1X2P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'AMASS_XT30PW-F_1x02_P2.50mm_Horizontal', 'description': 'Connector XT30 Horizontal PCB Female, https://www.tme.eu/en/Document/ce4077e36b79046da520ca73227e15de/XT30PW%20SPEC.pdf', 'tags': 'RC Connector XT30', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_AMASS.3dshapes/AMASS_XT30PW-F_1x02_P2.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_AMASS : AMASS_XT30PW-F_1x02_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

