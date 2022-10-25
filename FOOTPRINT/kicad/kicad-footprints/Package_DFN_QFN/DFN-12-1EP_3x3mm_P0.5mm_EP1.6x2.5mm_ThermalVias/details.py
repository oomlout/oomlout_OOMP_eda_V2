
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-12-1EP_3x3mm_P0.5mm_EP1.6x2.5mm_ThermalVias"
    hexID = "FZKDFNDFN121EP3X3P5EP16X25THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-12-1EP_3x3mm_P0.5mm_EP1.6x2.5mm_ThermalVias', 'description': 'DFN, 12 Pin (https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/MIC2207-2MHz-3A-PWM-Buck-Regulator-DS20006470A.pdf#page=22), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'DFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-12-1EP_3x3mm_P0.5mm_EP1.6x2.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-12-1EP_3x3mm_P0.5mm_EP1.6x2.5mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

