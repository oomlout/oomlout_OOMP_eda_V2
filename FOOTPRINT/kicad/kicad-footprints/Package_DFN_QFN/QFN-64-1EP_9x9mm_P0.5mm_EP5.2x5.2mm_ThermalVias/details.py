
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm_ThermalVias"
    hexID = "FZKDFNQFN641EP9X9P5EP52X52THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm_ThermalVias', 'description': 'QFN, 64 Pin (https://www.silabs.com/documents/public/data-sheets/Si5345-44-42-D-DataSheet.pdf#page=51), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-64-1EP_9x9mm_P0.5mm_EP5.2x5.2mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

