
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_R-PWSON-N12_EP0.4x2mm"
    hexID = "FZKSONTEXASRPWSONN12EP4X2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_R-PWSON-N12_EP0.4x2mm', 'description': 'http://www.ti.com/lit/ds/symlink/tpd6f003.pdf', 'tags': 'WSON SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_R-PWSON-N12_EP0.4x2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : Texas_R-PWSON-N12_EP0.4x2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

