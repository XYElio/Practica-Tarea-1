# <span style="color: #1D6F58; font-weight: bold;">Práctica 4</span>


## <span style="color: #2A2929; font-weight: bold;">Enunciado del Problema:</span>
> Σ (i) desde i = 1^3 hasta n
Generar en while,do while ,for.

## <span style="color: #2A2929; font-weight: bold;">Análisis:</span>
> * Pedir el valor de n y verificar que sea positivo.
> * Inicializas una variable suma en 0.
> * Usas un bucle para repetir la variable hasta que se cumpla las condiciones.
> * Al final del bucle, el valor de producto contendrá el suma de n.




## <span style="color: #2A2929; font-weight: bold;">Diagrama de Flujo de Datos (DFD):</span>
**WHILE**
<p align="center">
  <img src="Imagenes/24.1.png"  width="600" height="500">
</p>

**DO WHILE**
<p align="center">
  <img src="Imagenes/24.2.png"  width="600" height="500">
</p>

**FOR**
<p align="center">
  <img src="Imagenes/24.3.png"  width="600" height="500">
</p>

## <span style="color: #2A2929; font-weight: bold;">Prueba de Escritorio</span>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>WHILE</span></strong></p>
<table style="width:460.45pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 33.5pt;border-top: none;border-left: 1pt solid windowtext;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: none;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n</span></strong></p>
            </td>
            <td style="width: 21.55pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i</span></strong></p>
            </td>
            <td style="width: 68.5pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n &gt; 0</span></strong></p>
            </td>
            <td style="width: 95.25pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i &lt;= n</span></strong></p>
            </td>
            <td style="width: 42.15pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma</span></strong></p>
            </td>
            <td style="width: 124.25pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma += i^3</span></strong></p>
            </td>
            <td style="width: 75.25pt;border-top: none;border-left: none;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: 1pt solid windowtext;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i ++</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 33.5pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3</span></strong></p>
            </td>
            <td style="width: 21.55pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>1</span></p>
            </td>
            <td style="width: 68.5pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &gt; 0 True</span></p>
            </td>
            <td style="width: 95.25pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>1 &lt;=3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2 &lt;=3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &lt;=3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>4 &lt;=3 False</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 42.15pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>1</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>9</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>36</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 124.25pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>suma = 1(0+1(1^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>suma = 9(1+8(2^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-family:"Arial",sans-serif;color:black;'>suma = 36(9+27(3^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 75.25pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 2 (1 +1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 3 (2 +1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 4 (3 +1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>DO WHILE</span></strong></p>
<table style="width:453.35pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 35.55pt;border-top: none;border-left: 1pt solid windowtext;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: none;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n</span></strong></p>
            </td>
            <td style="width: 28pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i</span></strong></p>
            </td>
            <td style="width: 63.8pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n &gt; 0</span></strong></p>
            </td>
            <td style="width: 42.5pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma</span></strong></p>
            </td>
            <td colspan="2" style="width: 5cm;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma += i^3</span></strong></p>
            </td>
            <td style="width: 63.8pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i ++</span></strong></p>
            </td>
            <td style="width: 77.95pt;border-top: none;border-left: none;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: 1pt solid windowtext;background: white;padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i &lt;= n</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 35.55pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3</span></strong></p>
            </td>
            <td style="width: 28pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>1</span></p>
            </td>
            <td style="width: 63.8pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &gt; 0 True</span></p>
            </td>
            <td style="width: 42.5pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>1</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>9</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>36</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 134.7pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma = 1(0+1(1^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma = 9(1+8(2^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma = 36(9+27(3^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td colspan="2" style="width: 70.85pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 2 (1 +1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 3 (2 +1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 4 (3 +1)</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 77.95pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>2 &lt;= 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &lt;= 3 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>4 &lt;= 3 False</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
        </tr>
        <tr>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
            <td style="border:none;"><br></td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><strong><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>FOR</span></strong></p>
<table style="width:453.35pt;border-collapse:collapse;border:none;">
    <tbody>
        <tr>
            <td style="width: 24.65pt;border-top: none;border-left: 1pt solid windowtext;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: none;background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n</span></strong></p>
            </td>
            <td style="width: 69pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>n &gt; 0</span></strong></p>
            </td>
            <td style="width: 168.35pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 1; i &lt;= n; i += 1</span></strong></p>
            </td>
            <td style="width: 42.55pt;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 1.5pt solid rgb(255, 217, 102);background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma</span></strong></p>
            </td>
            <td style="width: 148.8pt;border-top: none;border-left: none;border-bottom: 1.5pt solid rgb(255, 217, 102);border-right: 1pt solid windowtext;background: white;padding: 0cm 5.4pt;height: 13.45pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma +=</span><span style="color:black;">&nbsp;</span></strong><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i^3</span></strong></p>
            </td>
        </tr>
        <tr>
            <td style="width: 24.65pt;border-right: 1pt solid windowtext;border-bottom: 1pt solid windowtext;border-left: 1pt solid windowtext;border-image: initial;border-top: none;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><strong><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3</span></strong></p>
            </td>
            <td style="width: 69pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>3 &gt; 0 True</span></p>
            </td>
            <td style="width: 168.35pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>i = 1; 1 &lt;=3; i +=1 True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2 &lt;=3; i = 2 (1 +1) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 3 &lt;=3; i = 3 (2 +1) True</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 4 &lt;=3 False</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 42.55pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>1</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>9</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>36</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
            <td style="width: 148.8pt;border-top: none;border-left: none;border-bottom: 1pt solid windowtext;border-right: 1pt solid windowtext;background: rgb(255, 242, 204);padding: 0cm 5.4pt;height: 78.8pt;vertical-align: top;">
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma = 1(0+1(1^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma = 9(1+8(2^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;color:black;'>suma = 36(9+27(3^3))</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
                <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;line-height:normal;'><span style='font-size:16px;font-family:"Arial",sans-serif;'>&nbsp;</span></p>
            </td>
        </tr>
    </tbody>
</table>
<p style='margin-top:0cm;margin-right:0cm;margin-bottom:8.0pt;margin-left:0cm;font-size:11.0pt;font-family:"Calibri",sans-serif;'><span style='font-size:16px;line-height:107%;font-family:"Arial",sans-serif;'>&nbsp;</span></p>

## Ejecución
<p align="center">
  <img src="Imagenes/4.png"  width="600" height="500">
</p>