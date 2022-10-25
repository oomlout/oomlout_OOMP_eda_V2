
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-6L_10x3.84mm_P1.27mm"
    hexID = "FZKSOSO6L1X384P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-6L_10x3.84mm_P1.27mm', 'description': '6-pin plasic small outline 7,5mm long https://toshiba.semicon-storage.com/info/docget.jsp?did=53548&prodName=TLP2770', 'tags': 'SO-6L', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-6L_10x3.84mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SO-6L_10x3.84mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

