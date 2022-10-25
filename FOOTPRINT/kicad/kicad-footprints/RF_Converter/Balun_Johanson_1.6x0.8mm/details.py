
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Converter"
    oIndex = "Balun_Johanson_1.6x0.8mm"
    hexID = "FZKRFBALUNJOHANSON16X8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Balun_Johanson_1.6x0.8mm', 'description': '6-pin 1.6x0.8 mm balun footprint', 'tags': 'Johanson balun filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Converter.3dshapes/Balun_Johanson_1.6x0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('RF_Converter : Balun_Johanson_1.6x0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

