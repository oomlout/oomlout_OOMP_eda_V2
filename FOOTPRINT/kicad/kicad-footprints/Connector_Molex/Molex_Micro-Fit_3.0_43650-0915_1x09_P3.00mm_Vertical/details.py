
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Micro-Fit_3.0_43650-0915_1x09_P3.00mm_Vertical"
    hexID = "FZKCNMXMXMFIT343659151X9P3VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Micro-Fit_3.0_43650-0915_1x09_P3.00mm_Vertical', 'description': 'Molex Micro-Fit 3.0 Connector System, 43650-0915 (compatible alternatives: 43650-0916, 43650-0917), 9 Pins per row (http://www.molex.com/pdm_docs/sd/436500215_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Micro-Fit_3.0 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Micro-Fit_3.0_43650-0915_1x09_P3.00mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Micro-Fit_3.0_43650-0915_1x09_P3.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

