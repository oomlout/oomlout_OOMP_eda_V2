
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_ACDC"
    oIndex = "Converter_ACDC_HiLink_HLK-PMxx"
    hexID = "FZKCONCONHILINKHLKPMXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_ACDC_HiLink_HLK-PMxx', 'description': 'ACDC-Converter, 3W, HiLink, HLK-PMxx, THT, http://www.hlktech.net/product_detail.php?ProId=54', 'tags': 'ACDC-Converter 3W THT HiLink board mount module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_ACDC.3dshapes/Converter_ACDC_HiLink_HLK-PMxx.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Converter_ACDC : Converter_ACDC_HiLink_HLK-PMxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

