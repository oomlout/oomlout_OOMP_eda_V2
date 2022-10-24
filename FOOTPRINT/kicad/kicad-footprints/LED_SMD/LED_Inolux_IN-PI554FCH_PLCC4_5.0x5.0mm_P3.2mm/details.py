
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm"
    hexID = "FZKLSMLINOLUXINPI554FCHPLCC45X5P32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm', 'description': 'http://www.inolux-corp.com/datasheet/SMDLED/Addressable%20LED/IN-PI554FCH.pdf', 'tags': 'RGB LED NeoPixel addressable', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

