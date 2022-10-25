
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_52559-3652_2x18-1MP_P0.5mm_Vertical"
    hexID = "FZKCNFFCFPCMX5255936522X181MPP5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_52559-3652_2x18-1MP_P0.5mm_Vertical', 'description': 'Molex 0.50mm Pitch Easy-On Type FFC/FPC, 52559-3652, 36 Circuits (https://www.molex.com/pdm_docs/sd/525593652_sd.pdf)', 'tags': 'connector Molex top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_52559-3652_2Rows_36pins_1MP_P0.5mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_52559-3652_2x18-1MP_P0.5mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

