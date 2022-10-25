
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Silvertel_Ag5810"
    hexID = "FZKCONCONSILVERTELAG581"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Silvertel_Ag5810', 'description': 'DCDC-Converter, 60W POE, Silvertel, pitch 2.54mm, package size 69.98x30x15.64mm, https://silvertel.com/images/datasheets/Ag5810-datasheet-IEEE802_3bt-Power-over-Ethernet-4-pair-PD.pdf', 'tags': 'DCDC-Converter Silvertel Ag5810 single output POE', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Silvertel_Ag5810.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Silvertel_Ag5810')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

