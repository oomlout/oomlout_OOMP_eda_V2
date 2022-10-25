
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Sensor_Pressure"
    oIndex = "TE_MS5525DSO-DBxxxyS"
    hexID = "FZKSENPRESSURETEMS5525DSODBXXXYS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TE_MS5525DSO-DBxxxyS', 'description': 'Pressure Sensor, Dual-Barbed, https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=MS5525DSO&DocType=DS&DocLang=English', 'tags': 'Pressure DualBarbed', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Sensor_Pressure.3dshapes/TE_MS5525DSO-DBxxxyS.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Sensor_Pressure : TE_MS5525DSO-DBxxxyS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

