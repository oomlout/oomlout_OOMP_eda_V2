
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Micro-Fit_3.0_43045-1415_2x07_P3.00mm_Vertical"
    hexID = "FZKCNMXMXMFIT3434514152X7P3VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Micro-Fit_3.0_43045-1415_2x07_P3.00mm_Vertical', 'description': 'Molex Micro-Fit 3.0 Connector System, 43045-1415 (compatible alternatives: 43045-1416, 43045-1417), 7 Pins per row (http://www.molex.com/pdm_docs/sd/430450217_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Micro-Fit_3.0 side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Micro-Fit_3.0_43045-1415_2x07_P3.00mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Micro-Fit_3.0_43045-1415_2x07_P3.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

