
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_RGY_R-PVQFN-N24_EP2.05x3.1mm"
    hexID = "FZKDFNTEXASRGYRPVQFNN24EP25X31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_RGY_R-PVQFN-N24_EP2.05x3.1mm', 'description': 'QFN, 24 Pin (http://www.ti.com/lit/ds/symlink/bq24133.pdf#page=40)', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_RGY_R-PVQFN-N24_EP2.05x3.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_RGY_R-PVQFN-N24_EP2.05x3.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

