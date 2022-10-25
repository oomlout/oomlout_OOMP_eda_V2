
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_3x2.5mm_P0.5mm_EP1.2x1.5mm_PullBack"
    hexID = "FZKSONWSON81EP3X25P5EP12X15PULLBACK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_3x2.5mm_P0.5mm_EP1.2x1.5mm_PullBack', 'description': 'WSON, 8 Pin (http://www.ti.com/lit/ml/mpds400/mpds400.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_3x2.5mm_P0.5mm_EP1.2x1.5mm_PullBack.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_3x2.5mm_P0.5mm_EP1.2x1.5mm_PullBack')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

