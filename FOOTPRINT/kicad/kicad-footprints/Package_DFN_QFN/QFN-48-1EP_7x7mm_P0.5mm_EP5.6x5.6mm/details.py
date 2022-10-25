
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm"
    hexID = "FZKDFNQFN481EP7X7P5EP56X56"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm', 'description': 'QFN, 48 Pin (http://www.st.com/resource/en/datasheet/stm32f042k6.pdf#page=94), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-48-1EP_7x7mm_P0.5mm_EP5.6x5.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

