
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_CLIK-Mate_502585-1470_1x14-1MP_P1.50mm_Horizontal"
    hexID = "FZKCNMXMXCLIKMATE525851471X141MPP15HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_CLIK-Mate_502585-1470_1x14-1MP_P1.50mm_Horizontal', 'description': 'Molex CLIK-Mate series connector, 502585-1470 (http://www.molex.com/pdm_docs/sd/5025850270_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex CLIK-Mate top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_CLIK-Mate_502585-1470_1x14-1MP_P1.50mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_CLIK-Mate_502585-1470_1x14-1MP_P1.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

