
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_ACDC"
    oIndex = "Converter_ACDC_MeanWell_IRM-05-xx_THT"
    hexID = "FZKCONCONMEANWELLIRM5XXTHT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_ACDC_MeanWell_IRM-05-xx_THT', 'description': 'http://www.meanwell.com/webapp/product/search.aspx?prod=IRM-05', 'tags': 'ACDC-Converter 5W   Meanwell IRM-05', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_ACDC.3dshapes/Converter_ACDC_MeanWell_IRM-05-xx_THT.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_ACDC : Converter_ACDC_MeanWell_IRM-05-xx_THT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

