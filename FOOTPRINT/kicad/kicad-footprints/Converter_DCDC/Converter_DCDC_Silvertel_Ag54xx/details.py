
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Silvertel_Ag54xx"
    hexID = "FZKCONCONSILVERTELAG54XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Silvertel_Ag54xx', 'description': 'DCDC-Converter, 30W POE, Silvertel, pitch 2.54mm, package size 62x19.5x14mm, https://silvertel.com/images/datasheets/Ag5400-datasheet-high%20Efficiency-30W-Power-Over-Ethernet-Plus-Module-PoE+PD.pdf', 'tags': 'DCDC-Converter Silvertel Ag5405 Ag5412 Ag5424 single output POE', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Silvertel_Ag54xx.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Silvertel_Ag54xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

