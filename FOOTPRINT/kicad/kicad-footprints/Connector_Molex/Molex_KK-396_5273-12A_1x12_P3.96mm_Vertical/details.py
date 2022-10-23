
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_KK-396_5273-12A_1x12_P3.96mm_Vertical"
    hexID = "FZKCNMXMXKK396527312A1X12P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_KK-396_5273-12A_1x12_P3.96mm_Vertical', 'description': 'Molex KK 396 Interconnect System, old/engineering part number: 5273-12A example for new part number: 09-65-2128, 12 Pins (https://www.molex.com/pdm_docs/sd/009652028_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex KK-396 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_KK-396_5273-12A_1x12_P3.96mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_KK-396_5273-12A_1x12_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

