
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Micro-Fit_3.0_43045-2218_2x11-1MP_P3.00mm_Vertical"
    hexID = "FZKCNMXMXMFIT3434522182X111MPP3VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Micro-Fit_3.0_43045-2218_2x11-1MP_P3.00mm_Vertical', 'description': 'Molex Micro-Fit 3.0 Connector System, 43045-2218 (compatible alternatives: 43045-2219, 43045-2220), 11 Pins per row (http://www.molex.com/pdm_docs/sd/430450218_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Micro-Fit_3.0 side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Micro-Fit_3.0_43045-2218_2x11-1MP_P3.00mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Molex : Molex_Micro-Fit_3.0_43045-2218_2x11-1MP_P3.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

