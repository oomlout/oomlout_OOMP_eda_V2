
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_SlimStack_52991-0408_2x20_P0.50mm_Vertical"
    hexID = "FZKCNMXMXSLIMSTACK52991482X2P5VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_SlimStack_52991-0408_2x20_P0.50mm_Vertical', 'description': 'Molex SlimStack Fine-Pitch SMT Board-to-Board Connectors, 52991-0408, 40 Pins (http://www.molex.com/pdm_docs/sd/529910308_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex SlimStack vertical', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_SlimStack_52991-0408_2x20_P0.50mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Molex : Molex_SlimStack_52991-0408_2x20_P0.50mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

