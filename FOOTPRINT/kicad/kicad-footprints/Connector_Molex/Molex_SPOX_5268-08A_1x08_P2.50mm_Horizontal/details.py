
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_SPOX_5268-08A_1x08_P2.50mm_Horizontal"
    hexID = "FZKCNMXMXSPOX52688A1X8P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_SPOX_5268-08A_1x08_P2.50mm_Horizontal', 'description': 'Molex SPOX Connector System, 5268-08A, 8 Pins per row (https://www.molex.com/pdm_docs/sd/022057045_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex SPOX horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_SPOX_5268-08A_1x08_P2.50mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_SPOX_5268-08A_1x08_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

