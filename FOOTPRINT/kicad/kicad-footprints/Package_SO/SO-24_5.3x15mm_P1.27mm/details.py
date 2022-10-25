
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-24_5.3x15mm_P1.27mm"
    hexID = "FZKSOSO2453X15P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-24_5.3x15mm_P1.27mm', 'description': 'SO, 24 Pin (https://www.ti.com/lit/ml/msop002a/msop002a.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SO SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-24_5.3x15mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SO-24_5.3x15mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

