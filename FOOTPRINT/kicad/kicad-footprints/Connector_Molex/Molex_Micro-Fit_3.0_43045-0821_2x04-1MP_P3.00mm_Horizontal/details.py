
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Micro-Fit_3.0_43045-0821_2x04-1MP_P3.00mm_Horizontal"
    hexID = "FZKCNMXMXMFIT343458212X41MPP3HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Micro-Fit_3.0_43045-0821_2x04-1MP_P3.00mm_Horizontal', 'description': 'Molex Micro-Fit 3.0 Connector System, 43045-0821 (alternative finishes: 43045-082x), 4 Pins per row (https://www.molex.com/pdm_docs/sd/430450221_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Micro-Fit_3.0 horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Micro-Fit_3.0_43045-0821_2x04-1MP_P3.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Micro-Fit_3.0_43045-0821_2x04-1MP_P3.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

