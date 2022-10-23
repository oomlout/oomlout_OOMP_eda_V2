
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_TDK_NLV32_3.2x2.5mm"
    hexID = "FZKINDUCTORSMLTDKNLV3232X25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_TDK_NLV32_3.2x2.5mm', 'description': 'TDK NLV32, 3.2x2.5x2.2mm, https://product.tdk.com/info/en/catalog/datasheets/inductor_commercial_standard_nlv32-ef_en.pdf', 'tags': 'tdk nlv32 nlcv32 nlfv32', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_TDK_NLV32_3.2x2.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_TDK_NLV32_3.2x2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

