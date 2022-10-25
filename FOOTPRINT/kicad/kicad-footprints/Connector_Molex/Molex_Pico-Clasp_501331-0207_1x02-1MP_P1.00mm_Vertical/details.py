
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Pico-Clasp_501331-0207_1x02-1MP_P1.00mm_Vertical"
    hexID = "FZKCNMXMXPICOCLASP51331271X21MPP1VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Pico-Clasp_501331-0207_1x02-1MP_P1.00mm_Vertical', 'description': 'Molex Pico-Clasp series connector, 501331-0207 (http://www.molex.com/pdm_docs/sd/5013310207_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Pico-Clasp side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Pico-Clasp_501331-0207_1x02-1MP_P1.00mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Pico-Clasp_501331-0207_1x02-1MP_P1.00mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

