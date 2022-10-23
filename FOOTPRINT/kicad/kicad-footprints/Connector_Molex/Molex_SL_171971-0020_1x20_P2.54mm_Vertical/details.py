
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_SL_171971-0020_1x20_P2.54mm_Vertical"
    hexID = "FZKCNMXMXSL17197121X2P254VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_SL_171971-0020_1x20_P2.54mm_Vertical', 'description': 'Molex Stackable Linear Connector, 171971-0020 (compatible alternatives: 171971-0120, 171971-0220), 20 Pins per row (https://www.molex.com/pdm_docs/sd/1719710002_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex SL vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_SL_171971-0020_1x20_P2.54mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_SL_171971-0020_1x20_P2.54mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

