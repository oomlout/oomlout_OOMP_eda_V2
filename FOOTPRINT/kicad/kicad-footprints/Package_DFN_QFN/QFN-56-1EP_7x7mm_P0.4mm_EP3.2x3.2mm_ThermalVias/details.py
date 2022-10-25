
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm_ThermalVias"
    hexID = "FZKDFNQFN561EP7X7P4EP32X32THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm_ThermalVias', 'description': 'QFN, 56 Pin (https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf#page=634), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

