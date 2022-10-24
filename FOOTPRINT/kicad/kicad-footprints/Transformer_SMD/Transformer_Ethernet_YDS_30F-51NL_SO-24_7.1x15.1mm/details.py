
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transformer_SMD"
    oIndex = "Transformer_Ethernet_YDS_30F-51NL_SO-24_7.1x15.1mm"
    hexID = "FZKTRSMTRETHERNETYDS3F51NLSO2471X151"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Transformer_Ethernet_YDS_30F-51NL_SO-24_7.1x15.1mm', 'description': 'YDS 30F-51NL SO, 24 Pin (https://datasheet.lcsc.com/lcsc/1811051610_Shanghai-YDS-Tech-30F-51NL_C123168.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'YDS SO Transformer_SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Transformer_Ethernet_YDS_30F-51NL_SO-24_7.1x15.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Transformer_SMD : Transformer_Ethernet_YDS_30F-51NL_SO-24_7.1x15.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

