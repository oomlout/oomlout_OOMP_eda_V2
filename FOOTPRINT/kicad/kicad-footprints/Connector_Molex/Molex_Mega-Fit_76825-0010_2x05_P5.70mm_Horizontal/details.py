
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Mega-Fit_76825-0010_2x05_P5.70mm_Horizontal"
    hexID = "FZKCNMXMXMEGAFIT7682512X5P57HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Mega-Fit_76825-0010_2x05_P5.70mm_Horizontal', 'description': 'Molex Mega-Fit Power Connectors, 76825-0010 (compatible alternatives: 172064-0010, 172064-1010), 5 Pins per row (http://www.molex.com/pdm_docs/sd/1720640002_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Mega-Fit top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Mega-Fit_76825-0010_2x05_P5.70mm_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Mega-Fit_76825-0010_2x05_P5.70mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

