
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_R-PWQFN-N28_EP2.1x3.1mm_ThermalVias"
    hexID = "FZKDFNTEXASRPWQFNN28EP21X31THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_R-PWQFN-N28_EP2.1x3.1mm_ThermalVias', 'description': 'QFN, 28 Pin (http://www.ti.com/lit/ds/symlink/tps51363.pdf#page=29), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_R-PWQFN-N28_EP2.1x3.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_R-PWQFN-N28_EP2.1x3.1mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

