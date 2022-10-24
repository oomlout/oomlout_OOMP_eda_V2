
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Kingbright_APFA3010_3x1.5mm_Horizontal"
    hexID = "FZKLSMLKINGBRIGHTAPFA313X15HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Kingbright_APFA3010_3x1.5mm_Horizontal', 'description': 'LED RGB, APFA3010, http://www.kingbrightusa.com/images/catalog/SPEC/APFA3010LSEEZGKQBKC.pdf', 'tags': 'LED RGB APFA3010 KINGBRIGHT 3x1.5mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Kingbright_APFA3010_3x1.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Kingbright_APFA3010_3x1.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

