
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_VQFN-RHL-20_ThermalVias"
    hexID = "FZKDFNTEXASVQFNRHL2THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_VQFN-RHL-20_ThermalVias', 'description': 'http://www.ti.com/lit/ds/symlink/bq51050b.pdf', 'tags': 'RHL0020A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_VQFN-RHL-20_ThermalVias.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_VQFN-RHL-20_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

