
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PWQFN-N16_EP2.1x2.1mm"
    hexID = "FZKDFNTEXASSPWQFNN16EP21X21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PWQFN-N16_EP2.1x2.1mm', 'description': 'QFN, 16 Pin (http://www.ti.com/lit/ds/symlink/drv8801.pdf#page=31 MO-220 variation VGGC), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N16_EP2.1x2.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PWQFN-N16_EP2.1x2.1mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

