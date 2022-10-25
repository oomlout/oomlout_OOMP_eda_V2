
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-32_11.305x20.495mm_P1.27mm"
    hexID = "FZKSOSS321135X2495P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-32_11.305x20.495mm_P1.27mm', 'description': 'SSOP, 32 Pin (http://www.issi.com/WW/pdf/61-64C5128AL.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-32_11.305x20.495mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SSOP-32_11.305x20.495mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

