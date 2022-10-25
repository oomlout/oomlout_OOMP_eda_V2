
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Mega-Fit_76829-0102_2x01_P5.70mm_Vertical"
    hexID = "FZKCNMXMXMEGAFIT76829122X1P57VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Mega-Fit_76829-0102_2x01_P5.70mm_Vertical', 'description': 'Molex Mega-Fit Power Connectors, 76829-0102 (compatible alternatives: 172065-0202, 172065-0302), 1 Pins per row (http://www.molex.com/pdm_docs/sd/768290102_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Mega-Fit side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Mega-Fit_76829-0102_2x01_P5.70mm_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Mega-Fit_76829-0102_2x01_P5.70mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

