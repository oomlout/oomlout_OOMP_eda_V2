
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "RF_Module"
    oIndex = "Garmin_M8-35_9.8x14.0mm_Layout6x6_P1.5mm"
    hexID = "FZKRFMOGARMINM83598X14LAYOUT6X6P15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Garmin_M8-35_9.8x14.0mm_Layout6x6_P1.5mm', 'description': 'D52M ANT SoC Module https://www.thisisant.com/assets/resources/D00001687_D52_Module_Datasheet.v.2.3_(Garmin).pdf', 'tags': 'RF SoC Radio ANT Bluetooth BLE D52 nRF52 Garmin Canada Dynastream Nordic', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/Garmin_M8-35_9.8x14.0mm_Layout6x6_P1.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('RF_Module : Garmin_M8-35_9.8x14.0mm_Layout6x6_P1.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

