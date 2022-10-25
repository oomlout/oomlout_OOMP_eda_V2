
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Converter"
    oIndex = "RF_Attenuator_Susumu_PAT1220"
    hexID = "FZKRFRFATTENUATORSUSUMUPAT122"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RF_Attenuator_Susumu_PAT1220', 'description': 'http://www.susumu-usa.com/pdf/Foot_Print_38.pdf, https://www.susumu.co.jp/common/pdf/n_catalog_partition16_en.pdf', 'tags': '2mm 1.2mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Converter.3dshapes/RF_Attenuator_Susumu_PAT1220.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('RF_Converter : RF_Attenuator_Susumu_PAT1220')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

