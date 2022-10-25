
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias"
    hexID = "FZKDFNQFN121EP3X3P5EP16X16THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias', 'description': 'QFN, 12 Pin (https://www.nxp.com/docs/en/data-sheet/MMZ09332B.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-12-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

