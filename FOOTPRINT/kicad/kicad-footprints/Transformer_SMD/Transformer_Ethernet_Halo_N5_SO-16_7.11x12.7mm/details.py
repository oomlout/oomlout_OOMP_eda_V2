
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Ethernet_Halo_N5_SO-16_7.11x12.7mm"
    hexID = "FZKTRSMTRETHERNETHALON5SO16711X127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Ethernet_Halo_N5_SO-16_7.11x12.7mm', 'description': 'Halo N5 SO, 16 Pin (https://www.haloelectronics.com/pdf/discrete-ultra-100baset.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'Halo SO Transformer_SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Ethernet_Halo_N5_SO-16_7.11x12.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Ethernet_Halo_N5_SO-16_7.11x12.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

