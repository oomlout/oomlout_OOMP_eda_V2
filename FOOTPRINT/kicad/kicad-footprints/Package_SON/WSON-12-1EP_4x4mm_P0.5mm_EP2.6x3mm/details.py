
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-12-1EP_4x4mm_P0.5mm_EP2.6x3mm"
    hexID = "FZKSONWSON121EP4X4P5EP26X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-12-1EP_4x4mm_P0.5mm_EP2.6x3mm', 'description': 'WSON, 12 Pin (http://www.ti.com/lit/ds/symlink/ldc1312.pdf#page=62), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-12-1EP_4x4mm_P0.5mm_EP2.6x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-12-1EP_4x4mm_P0.5mm_EP2.6x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

