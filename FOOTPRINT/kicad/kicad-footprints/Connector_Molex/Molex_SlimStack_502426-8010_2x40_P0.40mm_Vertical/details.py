
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Molex"
    oIndex = "Molex_SlimStack_502426-8010_2x40_P0.40mm_Vertical"
    hexID = "FZKCNMXMXSLIMSTACK52426812X4P4VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Molex_SlimStack_502426-8010_2x40_P0.40mm_Vertical', 'description': 'Molex SlimStack Fine-Pitch SMT Board-to-Board Connectors, 502426-8010, 80 Pins (http://www.molex.com/pdm_docs/sd/5024260810_sd.pdf), generated with kicad-footprint-generator', 'tags': 'connector Molex SlimStack side entry', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Molex.3dshapes/Molex_SlimStack_502426-8010_2x40_P0.40mm_Vertical.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Molex : Molex_SlimStack_502426-8010_2x40_P0.40mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

