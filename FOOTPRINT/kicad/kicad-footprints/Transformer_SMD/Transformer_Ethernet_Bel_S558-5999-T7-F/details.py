
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Ethernet_Bel_S558-5999-T7-F"
    hexID = "FZKTRSMTRETHERNETBELS5585999T7F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Ethernet_Bel_S558-5999-T7-F', 'description': 'Ethernet Transformer, Bel S558-5999-T7-F, https://www.belfuse.com/resources/ICMs/lan-/S558-5999-T7-F.pdf', 'tags': 'Ethernet Transformer', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Ethernet_Bel_S558-5999-T7-F.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Ethernet_Bel_S558-5999-T7-F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

