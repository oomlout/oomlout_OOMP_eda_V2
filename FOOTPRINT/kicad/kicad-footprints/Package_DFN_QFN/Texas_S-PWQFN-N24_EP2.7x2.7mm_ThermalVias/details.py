
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PWQFN-N24_EP2.7x2.7mm_ThermalVias"
    hexID = "FZKDFNTEXASSPWQFNN24EP27X27THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PWQFN-N24_EP2.7x2.7mm_ThermalVias', 'description': 'QFN, 24 Pin (http://www.ti.com/lit/ds/symlink/bq25601.pdf#page=54), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N24_EP2.7x2.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PWQFN-N24_EP2.7x2.7mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

