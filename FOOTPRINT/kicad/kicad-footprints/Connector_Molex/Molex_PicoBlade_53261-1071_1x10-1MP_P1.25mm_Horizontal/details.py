
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_PicoBlade_53261-1071_1x10-1MP_P1.25mm_Horizontal"
    hexID = "FZKCNMXMXPICOBLADE532611711X11MPP125HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_PicoBlade_53261-1071_1x10-1MP_P1.25mm_Horizontal', 'description': 'Molex PicoBlade series connector, 53261-1071 (http://www.molex.com/pdm_docs/sd/532610271_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex PicoBlade top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_PicoBlade_53261-1071_1x10-1MP_P1.25mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_PicoBlade_53261-1071_1x10-1MP_P1.25mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

