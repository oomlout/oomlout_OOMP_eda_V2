
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Buzzer_Beeper"
    oIndex = "Buzzer_TDK_PS1240P02BT_D12.2mm_H6.5mm"
    hexID = "FZKBZBUZZERTDKPS124P2BTD122H65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Buzzer_TDK_PS1240P02BT_D12.2mm_H6.5mm', 'description': 'Buzzer, D12.2mm height 6.5mm, https://product.tdk.com/info/en/catalog/datasheets/piezoelectronic_buzzer_ps_en.pdf', 'tags': 'buzzer', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Buzzer_Beeper.3dshapes/Buzzer_TDK_PS1240P02BT_D12.2mm_H6.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Buzzer_Beeper : Buzzer_TDK_PS1240P02BT_D12.2mm_H6.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

