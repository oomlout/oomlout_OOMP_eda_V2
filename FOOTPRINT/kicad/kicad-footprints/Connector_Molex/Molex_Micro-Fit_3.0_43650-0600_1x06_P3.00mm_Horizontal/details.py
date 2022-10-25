
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Micro-Fit_3.0_43650-0600_1x06_P3.00mm_Horizontal"
    hexID = "FZKCNMXMXMFIT3436561X6P3HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Micro-Fit_3.0_43650-0600_1x06_P3.00mm_Horizontal', 'description': 'Molex Micro-Fit 3.0 Connector System, 43650-0600 (compatible alternatives: 43650-0601, 43650-0602), 6 Pins per row (https://www.molex.com/pdm_docs/sd/436500300_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Micro-Fit_3.0 top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Micro-Fit_3.0_43650-0600_1x06_P3.00mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Micro-Fit_3.0_43650-0600_1x06_P3.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

