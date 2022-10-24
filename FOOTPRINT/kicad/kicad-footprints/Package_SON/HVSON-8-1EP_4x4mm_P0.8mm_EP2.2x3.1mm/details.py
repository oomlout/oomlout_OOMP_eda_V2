
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "HVSON-8-1EP_4x4mm_P0.8mm_EP2.2x3.1mm"
    hexID = "FZKSONHVSON81EP4X4P8EP22X31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVSON-8-1EP_4x4mm_P0.8mm_EP2.2x3.1mm', 'description': 'HVSON, 8 Pin (https://www.nxp.com/docs/en/data-sheet/PCF8523.pdf (page 57)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'HVSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/HVSON-8-1EP_4x4mm_P0.8mm_EP2.2x3.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : HVSON-8-1EP_4x4mm_P0.8mm_EP2.2x3.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

