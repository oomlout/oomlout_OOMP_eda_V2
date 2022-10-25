
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_4x4mm_P0.8mm_EP2.2x3mm"
    hexID = "FZKSONWSON81EP4X4P8EP22X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_4x4mm_P0.8mm_EP2.2x3mm', 'description': 'WSON, 8 Pin (https://www.ti.com/lit/ds/symlink/lp2987.pdf#page=26), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_4x4mm_P0.8mm_EP2.2x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_4x4mm_P0.8mm_EP2.2x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

