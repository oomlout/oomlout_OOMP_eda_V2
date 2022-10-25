
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_S-PWQFN-N100_EP5.5x5.5mm_ThermalVias"
    hexID = "FZKDFNTEXASSPWQFNN1EP55X55THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PWQFN-N100_EP5.5x5.5mm_ThermalVias', 'description': 'http://www.ti.com/general/docs/lit/getliterature.tsp?baseLiteratureNumber=szza059&fileType=pdf,http://www.ti.com/lit/ds/sllse76m/sllse76m.pdf', 'tags': 'MultiRow QFN', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N100_EP5.5x5.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_S-PWQFN-N100_EP5.5x5.5mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

