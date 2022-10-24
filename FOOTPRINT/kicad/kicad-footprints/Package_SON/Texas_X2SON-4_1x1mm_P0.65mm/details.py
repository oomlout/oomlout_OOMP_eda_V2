
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_X2SON-4_1x1mm_P0.65mm"
    hexID = "FZKSONTEXASX2SON41X1P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_X2SON-4_1x1mm_P0.65mm', 'description': 'X2SON 5 pin 1x1mm package (Reference Datasheet: http://www.ti.com/lit/ds/sbvs193d/sbvs193d.pdf Reference part: TPS383x) [StepUp generated footprint]', 'tags': 'X2SON', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_X2SON-4_1x1mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_SON : Texas_X2SON-4_1x1mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

