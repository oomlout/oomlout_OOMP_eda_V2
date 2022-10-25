
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_ACDC"
    oIndex = "Converter_ACDC_MeanWell_IRM-03-xx_SMD"
    hexID = "FZKCONCONMEANWELLIRM3XXSM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_ACDC_MeanWell_IRM-03-xx_SMD', 'description': 'ACDC-Converter, 3W, Meanwell, IRM-03, SMD, http://www.meanwell.com/webapp/product/search.aspx?prod=IRM-03', 'tags': 'ACDC-Converter 3W', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_ACDC.3dshapes/Converter_ACDC_MeanWell_IRM-03-xx_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Converter_ACDC : Converter_ACDC_MeanWell_IRM-03-xx_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

