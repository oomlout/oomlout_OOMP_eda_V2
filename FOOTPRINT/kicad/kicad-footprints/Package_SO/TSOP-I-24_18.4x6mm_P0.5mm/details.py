
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSOP-I-24_18.4x6mm_P0.5mm"
    hexID = "FZKSOTSI24184X6P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSOP-I-24_18.4x6mm_P0.5mm', 'description': 'TSOP-I, 24 Pin (https://www.jedec.org/standards-documents/docs/mo-142-d variation AD), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'TSOP-I SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-24_18.4x6mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : TSOP-I-24_18.4x6mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

