
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Micro-Fit_3.0_43650-1110_1x11-1MP_P3.00mm_Horizontal_PnP"
    hexID = "FZKCNMXMXMFIT343651111X111MPP3HORIZONTALPNP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Micro-Fit_3.0_43650-1110_1x11-1MP_P3.00mm_Horizontal_PnP', 'description': 'Molex Micro-Fit 3.0 Connector System, 43650-1110 (compatible alternatives: 43650-1111, 43650-1109), 11 Pins per row (https://www.molex.com/pdm_docs/sd/436500210_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Micro-Fit_3.0 horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Micro-Fit_3.0_43650-1110_1x11-1MP_P3.00mm_Horizontal_PnP.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Molex : Molex_Micro-Fit_3.0_43650-1110_1x11-1MP_P3.00mm_Horizontal_PnP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

