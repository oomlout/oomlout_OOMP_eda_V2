
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Mini-Fit_Sr_42819-62XX_1x06_P10.00mm_Vertical"
    hexID = "FZKCNMXMXMFITSR4281962XX1X6P1VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Mini-Fit_Sr_42819-62XX_1x06_P10.00mm_Vertical', 'description': 'Molex Mini-Fit Sr. Power Connectors, 42819-62XX, 6 Pins per row (http://www.molex.com/pdm_docs/sd/428192214_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Mini-Fit_Sr side entry', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Mini-Fit_Sr_42819-62XX_1x06_P10.00mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Molex : Molex_Mini-Fit_Sr_42819-62XX_1x06_P10.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

