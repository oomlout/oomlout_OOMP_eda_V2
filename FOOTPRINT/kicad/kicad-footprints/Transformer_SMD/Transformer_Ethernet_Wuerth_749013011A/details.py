
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Ethernet_Wuerth_749013011A"
    hexID = "FZKTRSMTRETHERNETWUERTH7491311A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Ethernet_Wuerth_749013011A', 'description': 'Ethernet Transformer, Wuerth 749013011A, https://www.we-online.com/katalog/datasheet/749013011A.pdf', 'tags': 'Ethernet Transformer', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Ethernet_Wuerth_749013011A.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Ethernet_Wuerth_749013011A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

