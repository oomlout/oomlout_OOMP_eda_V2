
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-38-1EP_5x7mm_P0.5mm_EP3.15x5.15mm_ThermalVias"
    hexID = "FZKDFNQFN381EP5X7P5EP315X515THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-38-1EP_5x7mm_P0.5mm_EP3.15x5.15mm_ThermalVias', 'description': 'QFN, 38 Pin (http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-qfn/QFN_38_05-08-1701.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-38-1EP_5x7mm_P0.5mm_EP3.15x5.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-38-1EP_5x7mm_P0.5mm_EP3.15x5.15mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

