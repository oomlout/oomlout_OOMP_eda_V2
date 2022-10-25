
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x6.7mm"
    hexID = "FZKSOTSS281EP44X97P65EP285X67"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x6.7mm', 'description': 'TSSOP, 28 Pin (JEDEC MO-153 Var AET Pkg.Code U28E-4 https://pdfserv.maximintegrated.com/package_dwgs/21-0108.PDF), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'TSSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x6.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : TSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x6.7mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

