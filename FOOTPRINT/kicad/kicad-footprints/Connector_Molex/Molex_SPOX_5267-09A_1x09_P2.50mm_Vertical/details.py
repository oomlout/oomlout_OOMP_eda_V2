
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_SPOX_5267-09A_1x09_P2.50mm_Vertical"
    hexID = "FZKCNMXMXSPOX52679A1X9P25VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_SPOX_5267-09A_1x09_P2.50mm_Vertical', 'description': 'Molex SPOX Connector System, 5267-09A, 9 Pins per row (http://www.molex.com/pdm_docs/sd/022035035_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex SPOX side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_SPOX_5267-09A_1x09_P2.50mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_SPOX_5267-09A_1x09_P2.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

