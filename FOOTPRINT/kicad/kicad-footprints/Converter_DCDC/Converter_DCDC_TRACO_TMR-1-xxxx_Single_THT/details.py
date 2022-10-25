
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_TRACO_TMR-1-xxxx_Single_THT"
    hexID = "FZKCONCONTRACOTMR1XXXXSINGLETHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_TRACO_TMR-1-xxxx_Single_THT', 'description': 'DCDC-Converter, TRACO, TMR 1-xxxx, Single output, Rev. March 21.2016', 'tags': 'DCDC-Converter TRACO TMR1-xxxx Single_output', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_TRACO_TMR-1-xxxx_Single_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_TRACO_TMR-1-xxxx_Single_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

