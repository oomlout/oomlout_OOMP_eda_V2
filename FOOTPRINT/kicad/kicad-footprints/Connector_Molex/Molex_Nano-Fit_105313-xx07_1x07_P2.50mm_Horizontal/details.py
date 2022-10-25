
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Nano-Fit_105313-xx07_1x07_P2.50mm_Horizontal"
    hexID = "FZKCNMXMXNANOFIT15313XX71X7P25HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Nano-Fit_105313-xx07_1x07_P2.50mm_Horizontal', 'description': 'Molex Nano-Fit Power Connectors, 105313-xx07, 7 Pins per row (http://www.molex.com/pdm_docs/sd/1053131208_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Nano-Fit top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Nano-Fit_105313-xx07_1x07_P2.50mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Nano-Fit_105313-xx07_1x07_P2.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

