
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Mini-Fit_Sr_42820-32XX_1x03_P10.00mm_Horizontal_ThermalVias"
    hexID = "FZKCNMXMXMFITSR428232XX1X3P1HORIZONTALTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Mini-Fit_Sr_42820-32XX_1x03_P10.00mm_Horizontal_ThermalVias', 'description': 'Molex Mini-Fit Sr. Power Connectors, 42820-32XX, With thermal vias in pads, 3 Pins per row (http://www.molex.com/pdm_docs/sd/428202214_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Mini-Fit_Sr top entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Mini-Fit_Sr_42820-32XX_1x03_P10.00mm_Horizontal_ThermalVias.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Mini-Fit_Sr_42820-32XX_1x03_P10.00mm_Horizontal_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

