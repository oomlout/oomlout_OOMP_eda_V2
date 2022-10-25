
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm_ThermalVias"
    hexID = "FZKQFPTQFP11EP14X14P5EP5X5THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm_ThermalVias', 'description': 'TQFP, 100 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/tqfp_edsv/sv_100_4.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'TQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_QFP : TQFP-100-1EP_14x14mm_P0.5mm_EP5x5mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

