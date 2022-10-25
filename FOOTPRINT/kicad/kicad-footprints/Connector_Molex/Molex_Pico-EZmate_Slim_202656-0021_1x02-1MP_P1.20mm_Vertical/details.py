
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Pico-EZmate_Slim_202656-0021_1x02-1MP_P1.20mm_Vertical"
    hexID = "FZKCNMXMXPICOEZMATESLIM22656211X21MPP12VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Pico-EZmate_Slim_202656-0021_1x02-1MP_P1.20mm_Vertical', 'description': 'Molex Pico-EZmate_Slim series connector, 202656-0021 (http://www.molex.com/pdm_docs/sd/2026560021_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Pico-EZmate_Slim side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Pico-EZmate_Slim_202656-0021_1x02-1MP_P1.20mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Pico-EZmate_Slim_202656-0021_1x02-1MP_P1.20mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

