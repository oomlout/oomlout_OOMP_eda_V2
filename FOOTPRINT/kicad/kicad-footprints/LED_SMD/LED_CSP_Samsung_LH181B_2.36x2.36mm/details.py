
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_CSP_Samsung_LH181B_2.36x2.36mm"
    hexID = "FZKLSMLCSPSAMSUNGLH181B236X236"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_CSP_Samsung_LH181B_2.36x2.36mm', 'description': 'High Power CSP LED, 2.36mm x 2.36mm, 1.4A max, https://cdn.samsung.com/led/file/resource/2021/01/Data_Sheet_LH181B_Rev.4.0.pdf', 'tags': 'LED Samsung LH181B', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_CSP_Samsung_LH181B_2.36x2.36mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_CSP_Samsung_LH181B_2.36x2.36mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

