Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.OpenTextFile("C:\Users\danie\Desktop\Wires.txt", 1) ' 1: ForReading

Set objExcel = CreateObject("Excel.Application")
objExcel.Visible = True ' Optional: Make Excel visible

Set objWorkbook = objExcel.Workbooks.Add
Set objWorksheet = objWorkbook.Worksheets(1) ' Get the first sheet in the new workbook

' Read the content from the text file and write it to the Excel sheet
columbNumber=1
rowNumber = 1
holder=1

Do Until objFile.AtEndOfStream
    lineContent = objFile.ReadLine

    ' Loop through each character in the line
    For i = 1 To Len(lineContent)
        ' Check if the character is a space
        If Mid(lineContent, i, 1) = " " Then
            objWorksheet.Cells(rowNumber, columbNumber).Value = Mid(lineContent, holder, i)
            columbNumber = columbNumber + 1
        End If
    rowNumber = rowNumber + 1
    holder=i
    Next
Loop

' Save the workbook (optional)
objWorkbook.SaveAs "C:\Path\To\Your\OutputWorkbook.xlsx"

' Clean up
objFile.Close
objExcel.Quit
Set objFile = Nothing
Set objExcel = Nothing
Set objFSO = Nothing
