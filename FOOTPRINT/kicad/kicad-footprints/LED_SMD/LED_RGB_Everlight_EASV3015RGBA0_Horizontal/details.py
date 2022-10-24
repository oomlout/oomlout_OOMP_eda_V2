
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_RGB_Everlight_EASV3015RGBA0_Horizontal"
    hexID = "FZKLSMLRGBEVERLIGHTEASV315RGBAHORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_RGB_Everlight_EASV3015RGBA0_Horizontal', 'description': 'LED, RGB, right-angle, clear, https://everlightamericas.com/index.php?controller=attachment&id_attachment=3220', 'tags': 'LED RGB right-angle', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_RGB_Everlight_EASV3015RGBA0_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_RGB_Everlight_EASV3015RGBA0_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

