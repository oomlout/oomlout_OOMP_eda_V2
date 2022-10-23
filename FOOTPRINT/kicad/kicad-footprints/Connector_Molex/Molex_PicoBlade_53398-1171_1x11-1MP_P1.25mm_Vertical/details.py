
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_PicoBlade_53398-1171_1x11-1MP_P1.25mm_Vertical"
    hexID = "FZKCNMXMXPICOBLADE5339811711X111MPP125VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_PicoBlade_53398-1171_1x11-1MP_P1.25mm_Vertical', 'description': 'Molex PicoBlade series connector, 53398-1171 (http://www.molex.com/pdm_docs/sd/533980271_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex PicoBlade side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_PicoBlade_53398-1171_1x11-1MP_P1.25mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_PicoBlade_53398-1171_1x11-1MP_P1.25mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

