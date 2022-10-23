
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_PCBEdge"
    oIndex = "molex_EDGELOCK_2-CKT"
    hexID = "FZKCNPCBEDGEMXEDGEL2CKT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'molex_EDGELOCK_2-CKT', 'description': 'https://www.molex.com/pdm_docs/sd/2008900106_sd.pdf', 'tags': 'Connector PCBEdge molex EDGELOCK', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_PCBEdge.3dshapes/molex_EDGELOCK_2-CKT.wrl', 'pins': {'type': 'connect', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_PCBEdge : molex_EDGELOCK_2-CKT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

