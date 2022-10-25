
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_Pico-Lock_504050-1291_1x12-1MP_P1.50mm_Horizontal"
    hexID = "FZKCNMXMXPICOL54512911X121MPP15HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_Pico-Lock_504050-1291_1x12-1MP_P1.50mm_Horizontal', 'description': 'Molex Pico-Lock series connector, 504050-1291 (http://www.molex.com/pdm_docs/sd/5040500891_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex Pico-Lock horizontal', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_Pico-Lock_504050-1291_1x12-1MP_P1.50mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Molex : Molex_Pico-Lock_504050-1291_1x12-1MP_P1.50mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

