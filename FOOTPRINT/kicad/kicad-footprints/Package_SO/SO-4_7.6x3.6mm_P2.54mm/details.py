
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-4_7.6x3.6mm_P2.54mm"
    hexID = "FZKSOSO476X36P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-4_7.6x3.6mm_P2.54mm', 'description': '4-Lead Plastic Small Outline (SO) (http://www.everlight.com/file/ProductFile/201407061745083848.pdf)', 'tags': 'SO SOIC 2.54', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-4_7.6x3.6mm_P2.54mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SO-4_7.6x3.6mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

