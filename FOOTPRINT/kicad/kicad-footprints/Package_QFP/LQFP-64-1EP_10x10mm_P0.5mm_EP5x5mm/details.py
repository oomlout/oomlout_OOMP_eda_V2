
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "LQFP-64-1EP_10x10mm_P0.5mm_EP5x5mm"
    hexID = "FZKQFPLQFP641EP1X1P5EP5X5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LQFP-64-1EP_10x10mm_P0.5mm_EP5x5mm', 'description': 'LQFP, 64 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/adv7611.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'LQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-64-1EP_10x10mm_P0.5mm_EP5x5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : LQFP-64-1EP_10x10mm_P0.5mm_EP5x5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

