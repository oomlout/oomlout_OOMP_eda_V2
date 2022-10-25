
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_RGE0024C_EP2.1x2.1mm"
    hexID = "FZKDFNTEXASRGE24CEP21X21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_RGE0024C_EP2.1x2.1mm', 'description': 'Texas  QFN, 24 Pin (http://www.ti.com/lit/ds/symlink/pca9548a.pdf#page=37), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Texas QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_RGE0024C_EP2.1x2.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_RGE0024C_EP2.1x2.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

