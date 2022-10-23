
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_CLIK-Mate_502386-0370_1x03-1MP_P1.25mm_Horizontal"
    hexID = "FZKCNMXMXCLIKMATE52386371X31MPP125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_CLIK-Mate_502386-0370_1x03-1MP_P1.25mm_Horizontal', 'description': 'Molex CLIK-Mate series connector, 502386-0370 (http://www.molex.com/pdm_docs/sd/5023860270_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex CLIK-Mate top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_CLIK-Mate_502386-0370_1x03-1MP_P1.25mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_CLIK-Mate_502386-0370_1x03-1MP_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

