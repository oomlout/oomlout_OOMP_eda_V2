
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "LQFP-52-1EP_10x10mm_P0.65mm_EP4.8x4.8mm"
    hexID = "FZKQFPLQFP521EP1X1P65EP48X48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LQFP-52-1EP_10x10mm_P0.65mm_EP4.8x4.8mm', 'description': 'LQFP, 52 Pin (https://www.onsemi.com/pub/Collateral/848H-01.PDF), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'LQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-52-1EP_10x10mm_P0.65mm_EP4.8x4.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : LQFP-52-1EP_10x10mm_P0.65mm_EP4.8x4.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

