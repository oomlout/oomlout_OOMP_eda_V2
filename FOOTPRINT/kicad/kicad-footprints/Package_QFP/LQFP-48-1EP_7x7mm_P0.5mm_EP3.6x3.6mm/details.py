
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm"
    hexID = "FZKQFPLQFP481EP7X7P5EP36X36"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm', 'description': 'LQFP, 48 Pin (http://www.analog.com/media/en/technical-documentation/data-sheets/LTC7810.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'LQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : LQFP-48-1EP_7x7mm_P0.5mm_EP3.6x3.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

