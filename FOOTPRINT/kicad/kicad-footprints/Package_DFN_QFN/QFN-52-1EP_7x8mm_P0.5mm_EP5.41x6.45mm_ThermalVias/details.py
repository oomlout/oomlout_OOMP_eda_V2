
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-52-1EP_7x8mm_P0.5mm_EP5.41x6.45mm_ThermalVias"
    hexID = "FZKDFNQFN521EP7X8P5EP541X645THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-52-1EP_7x8mm_P0.5mm_EP5.41x6.45mm_ThermalVias', 'description': 'QFN, 52 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-qfn/QFN_52_05-08-1729.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-52-1EP_7x8mm_P0.5mm_EP5.41x6.45mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-52-1EP_7x8mm_P0.5mm_EP5.41x6.45mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

