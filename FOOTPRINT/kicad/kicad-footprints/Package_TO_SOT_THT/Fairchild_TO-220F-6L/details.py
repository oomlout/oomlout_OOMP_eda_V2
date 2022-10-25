
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "Fairchild_TO-220F-6L"
    hexID = "FZKSOTFAIRCHILDTO22F6L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fairchild_TO-220F-6L', 'description': 'Fairchild TO-220F-6L, http://www.mouser.com/ds/2/149/FSL136MRT-113334.pdf', 'tags': 'Fairchild TO-220F-6L', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/Fairchild_TO-220F-6L.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : Fairchild_TO-220F-6L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

