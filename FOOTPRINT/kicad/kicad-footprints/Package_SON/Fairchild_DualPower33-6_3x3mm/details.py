
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Fairchild_DualPower33-6_3x3mm"
    hexID = "FZKSONFAIRCHILDDUALPOWER3363X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fairchild_DualPower33-6_3x3mm', 'description': 'Fairchild Power33 MOSFET package, 3x3mm (see https://www.fairchildsemi.com/datasheets/FD/FDMC8032L.pdf)', 'tags': 'mosfet', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Fairchild_DualPower33-6_3x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : Fairchild_DualPower33-6_3x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

