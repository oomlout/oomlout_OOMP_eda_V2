
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_KK-396_A-41791-0003_1x03_P3.96mm_Vertical"
    hexID = "FZKCNMXMXKK396A4179131X3P396VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_KK-396_A-41791-0003_1x03_P3.96mm_Vertical', 'description': 'Molex KK 396 Interconnect System, old/engineering part number: A-41791-0003 example for new part number: 26-60-4030, 3 Pins (https://www.molex.com/pdm_docs/sd/026604020_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex KK-396 vertical', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_KK-396_A-41791-0003_1x03_P3.96mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_KK-396_A-41791-0003_1x03_P3.96mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

