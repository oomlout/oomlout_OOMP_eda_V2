
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_Push_2P1T_Toggle_CK_PVA1xxH1xxxxxxV2"
    hexID = "FZKBSWPUSH2P1TTOGGLECKPVA1XXH1XXXXXXV2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_Push_2P1T_Toggle_CK_PVA1xxH1xxxxxxV2', 'description': 'momentary / push-push button, h=17.5mm C&K PVA1 https://www.ckswitches.com/media/1343/pva.pdf', 'tags': 'tact sw push PVA1 DPST', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_Push_2P1T_Toggle_CK_PVA1xxH1xxxxxxV2.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_THT : SW_Push_2P1T_Toggle_CK_PVA1xxH1xxxxxxV2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

