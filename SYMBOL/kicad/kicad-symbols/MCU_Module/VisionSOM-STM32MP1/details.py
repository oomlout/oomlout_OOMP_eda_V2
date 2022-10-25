
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "VisionSOM-STM32MP1"
    hexID = "SZKMCUMOVISIONSOMSTM32MP1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VisionSOM-STM32MP1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://wiki.somlabs.com/index.php/VisionSOM-STM32MP1_Datasheet_and_Pinout', 'kicadSymbolki_keywords': 'somlabs module', 'kicadSymbolki_description': 'STM32MP1 STMicroelectronics ARM Cortex-A7 800MHz single/dual core + ARM Cortex-M4 209MHz single core industrial SoM computer', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('MCU_Module : VisionSOM-STM32MP1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

