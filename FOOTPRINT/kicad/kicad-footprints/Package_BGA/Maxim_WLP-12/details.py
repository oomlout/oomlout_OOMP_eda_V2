
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Maxim_WLP-12"
    hexID = "FZKBGAMAXIMWLP12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Maxim_WLP-12', 'description': 'Maxim_WLP-12 W121B2+1 http://pdfserv.maximintegrated.com/package_dwgs/21-0009.PDF', 'tags': 'Maxim_WLP-12', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Maxim_WLP-12.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Maxim_WLP-12')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

