
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_3x3mm_P0.5mm_EP1.2x2mm"
    hexID = "FZKSONWSON81EP3X3P5EP12X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_3x3mm_P0.5mm_EP1.2x2mm', 'description': 'WSON, 8 Pin (http://www.ti.com/lit/ds/symlink/lp2951.pdf#page=27), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_3x3mm_P0.5mm_EP1.2x2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_3x3mm_P0.5mm_EP1.2x2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

