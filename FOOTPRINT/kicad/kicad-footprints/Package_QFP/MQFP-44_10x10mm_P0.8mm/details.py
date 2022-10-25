
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "MQFP-44_10x10mm_P0.8mm"
    hexID = "FZKQFPMQFP441X1P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MQFP-44_10x10mm_P0.8mm', 'description': 'MQFP, 44 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/ad7722.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/MQFP-44_10x10mm_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : MQFP-44_10x10mm_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

