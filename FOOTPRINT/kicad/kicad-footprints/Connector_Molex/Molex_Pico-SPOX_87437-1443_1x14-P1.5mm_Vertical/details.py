
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Pico-SPOX_87437-1443_1x14-P1.5mm_Vertical"
    hexID = "FZKCNMXMXPICOSPOX8743714431X14P15VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Pico-SPOX_87437-1443_1x14-P1.5mm_Vertical', 'description': 'Molex Pico-SPOX Connector System, 87437-1443, 14 Pins per row (https://www.molex.com/pdm_docs/sd/874371443_sd.pdf#page=2)', 'tags': 'molex pico spox 14', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Pico-SPOX_87437-1443_1x14-P1.5mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Molex : Molex_Pico-SPOX_87437-1443_1x14-P1.5mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

