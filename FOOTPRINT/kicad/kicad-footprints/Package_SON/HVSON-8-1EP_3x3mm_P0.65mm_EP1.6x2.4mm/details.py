
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "HVSON-8-1EP_3x3mm_P0.65mm_EP1.6x2.4mm"
    hexID = "FZKSONHVSON81EP3X3P65EP16X24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HVSON-8-1EP_3x3mm_P0.65mm_EP1.6x2.4mm', 'description': 'HVSON, 8 Pin (https://www.nxp.com/docs/en/data-sheet/TJA1051.pdf#page=16), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'HVSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/HVSON-8-1EP_3x3mm_P0.65mm_EP1.6x2.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : HVSON-8-1EP_3x3mm_P0.65mm_EP1.6x2.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

