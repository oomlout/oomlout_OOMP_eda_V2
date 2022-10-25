
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Molex_54132-5033_1x50-1MP_P0.5mm_Horizontal"
    hexID = "FZKCNFFCFPCMX541325331X51MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_54132-5033_1x50-1MP_P0.5mm_Horizontal', 'description': 'Molex FFC/FPC connector, 50 bottom-side contacts, 0.5mm pitch, 2.0mm height, https://www.molex.com/pdm_docs/sd/541325033_sd.pdf', 'tags': 'FFC FPC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Molex_54132-5033_1x50-1MP_P0.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Molex_54132-5033_1x50-1MP_P0.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

