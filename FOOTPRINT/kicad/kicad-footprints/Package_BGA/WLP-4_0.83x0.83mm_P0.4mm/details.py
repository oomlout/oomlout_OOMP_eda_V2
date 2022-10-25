
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "WLP-4_0.83x0.83mm_P0.4mm"
    hexID = "FZKBGAWLP483X83P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLP-4_0.83x0.83mm_P0.4mm', 'description': 'WLP-4_0.83x0.83mm_P0.4mm https://pdfserv.maximintegrated.com/package_dwgs/21-100107.PDF, https://www.maximintegrated.com/en/app-notes/index.mvp/id/1891', 'tags': 'WLP-4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/WLP-4_0.83x0.83mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : WLP-4_0.83x0.83mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

