
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "LQFP-52_10x10mm_P0.65mm"
    hexID = "FZKQFPLQFP521X1P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LQFP-52_10x10mm_P0.65mm', 'description': 'LQFP, 52 Pin (https://www.nxp.com/docs/en/package-information/98ARL10526D.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'LQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/LQFP-52_10x10mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : LQFP-52_10x10mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

