
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "STC_SOP-16_3.9x9.9mm_P1.27mm"
    hexID = "FZKSOSTCS1639X99P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'STC_SOP-16_3.9x9.9mm_P1.27mm', 'description': 'STC  SOP, 16 Pin (https://www.stcmicro.com/datasheet/STC15F2K60S2-en.pdf#page=156), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'STC SOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/STC_SOP-16_3.9x9.9mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : STC_SOP-16_3.9x9.9mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

