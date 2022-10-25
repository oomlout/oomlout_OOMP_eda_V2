
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_TRACO_TMR-xxxx_THT"
    hexID = "FZKCONCONTRACOTMRXXXXTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_TRACO_TMR-xxxx_THT', 'description': 'DCDC-Converter, TRACO, TMR xxxx, Single/Dual output, http://www.datasheetlib.com/datasheet/135136/tmr-2-2410e_traco-power.html?page=3#datasheet', 'tags': 'DCDC-Converter TRACO TMRxxxx Single/Dual_output', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_TRACO_TMR-xxxx_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_TRACO_TMR-xxxx_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

