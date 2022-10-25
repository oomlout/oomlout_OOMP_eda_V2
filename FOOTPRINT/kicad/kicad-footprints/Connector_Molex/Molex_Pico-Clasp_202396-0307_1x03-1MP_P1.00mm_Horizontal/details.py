
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Pico-Clasp_202396-0307_1x03-1MP_P1.00mm_Horizontal"
    hexID = "FZKCNMXMXPICOCLASP22396371X31MPP1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Pico-Clasp_202396-0307_1x03-1MP_P1.00mm_Horizontal', 'description': 'Molex Pico-Clasp series connector, 202396-0307 (http://www.molex.com/pdm_docs/sd/2023960207_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Pico-Clasp top entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Pico-Clasp_202396-0307_1x03-1MP_P1.00mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Pico-Clasp_202396-0307_1x03-1MP_P1.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

