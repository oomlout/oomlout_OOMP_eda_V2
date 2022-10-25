
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Murata_NCS1SxxxxSC_THT"
    hexID = "FZKCONCONMNCS1SXXXXSCTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Murata_NCS1SxxxxSC_THT', 'description': 'Murata NCS1SxxxxSC https://power.murata.com/data/power/ncl/kdc_ncs1.pdf (Script generated with StandardBox.py) (Murata NCS1SxxxxSC https://power.murata.com/data/power/ncl/kdc_ncs1.pdf)', 'tags': 'Murata NCS1SxxxxSC', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Murata_NCS1SxxxxSC_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Murata_NCS1SxxxxSC_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

