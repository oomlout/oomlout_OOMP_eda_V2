
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-18_4.4x6.5mm_P0.65mm"
    hexID = "FZKSOSS1844X65P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-18_4.4x6.5mm_P0.65mm', 'description': 'SSOP18: plastic shrink small outline package; 18 leads; body width 4.4 mm (http://toshiba.semicon-storage.com/info/docget.jsp?did=30523&prodName=TBD62783APG)', 'tags': 'SSOP 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-18_4.4x6.5mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-18_4.4x6.5mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

