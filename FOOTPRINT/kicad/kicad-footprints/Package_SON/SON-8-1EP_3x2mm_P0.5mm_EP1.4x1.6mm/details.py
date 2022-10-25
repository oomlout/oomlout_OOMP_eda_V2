
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "SON-8-1EP_3x2mm_P0.5mm_EP1.4x1.6mm"
    hexID = "FZKSONSON81EP3X2P5EP14X16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SON-8-1EP_3x2mm_P0.5mm_EP1.4x1.6mm', 'description': 'SON, 8 Pin (http://www.fujitsu.com/downloads/MICRO/fsa/pdf/products/memory/fram/MB85RS16-DS501-00014-6v0-E.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'SON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/SON-8-1EP_3x2mm_P0.5mm_EP1.4x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : SON-8-1EP_3x2mm_P0.5mm_EP1.4x1.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

