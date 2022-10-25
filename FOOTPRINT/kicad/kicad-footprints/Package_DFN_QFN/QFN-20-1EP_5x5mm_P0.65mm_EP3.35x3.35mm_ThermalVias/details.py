
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm_ThermalVias"
    hexID = "FZKDFNQFN21EP5X5P65EP335X335THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm_ThermalVias', 'description': 'QFN, 20 Pin (http://ww1.microchip.com/downloads/en/PackagingSpec/00000049BQ.pdf#page=276), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

