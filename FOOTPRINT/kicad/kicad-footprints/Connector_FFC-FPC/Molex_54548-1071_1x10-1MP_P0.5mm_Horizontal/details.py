
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_54548-1071_1x10-1MP_P0.5mm_Horizontal"
    hexID = "FZKCNFFCFPCMX545481711X11MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_54548-1071_1x10-1MP_P0.5mm_Horizontal', 'description': 'Molex FFC/FPC connector, 10 bottom-side contacts, 0.5mm pitch, 1.2mm height, https://www.molex.com/pdm_docs/sd/545481071_sd.pdf', 'tags': 'FFC FPC connector', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_54548-1071_1x10-1MP_P0.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_54548-1071_1x10-1MP_P0.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

