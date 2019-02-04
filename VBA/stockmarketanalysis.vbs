Sub marketanalysis()

    Dim lrow As Double
    Dim CurrentSymbol As String
    Dim NextSymbol As String
    Dim VolumeTotal As Double
    Dim outputrow As Double
    Dim YearOpen As Double
    Dim YearClose As Double
    Dim YearChange As Double
    Dim GreatestIncrease As Double
    Dim GreatestDecrease As Double
    Dim GreatestVolume As Double
    Dim PercentChange As Double
    
    For Each ws In Worksheets

        VolumeTotal = 0
        outputrow = 2

        'Find the last non-blank cell in column A(1)
        lrow = ws.Cells(Rows.Count, 1).End(xlUp).Row

        'Set the year open to the first stock value of the first stock
        YearOpen = ws.Cells(2, 3).Value

        'Create headers for output
        ws.Range("i1").Value = "Symbol"
        ws.Range("J1").Value = "Total Volume"
        ws.Range("K1").Value = "Year Change"
        ws.Range("L1").Value = "Percent Change"
        ws.Range("O1").Value = "Symbol"
        ws.Range("P1").Value = "Value"
        ws.Range("N2").Value = "Greatest % Increase"
        ws.Range("N3").Value = "Greatest % Decrease"
        ws.Range("N4").Value = "Greatest Total Volume"


        For Row = 2 To lrow + 1
        CurrentSymbol = ws.Cells(Row, 1).Value
        NextSymbol = ws.Cells(Row + 1, 1).Value
            'If this is the first non-zero stock price of the year, set it as stock opening price
            If YearOpen = 0 And ws.Cells(Row, 3) <> 0 Then
                YearOpen = ws.Cells(Row, 3)
            End If
            VolumeTotal = VolumeTotal + ws.Cells(Row, 7).Value
            'If this is the last row of data for the current stock symbol, output  summary
            If CurrentSymbol <> NextSymbol Then
                YearClose = ws.Cells(Row, 6).Value
                YearChange = YearClose - YearOpen
                ' handle case of division by zero if yearopen is 0
                If YearOpen = 0 Then
                    If YearClose = 0 Then
                        PercentChange = 0
                    Else
                        PercentChange = 100
                    End If
                Else
                    PercentChange = Round((YearChange / YearOpen * 100), 2)
                End If

                ' output totals for this tick symbol
                ws.Range("I" & outputrow).Value = CurrentSymbol
                ws.Range("J" & outputrow).Value = VolumeTotal
                ws.Range("K" & outputrow).Value = YearChange
                ws.Range("L" & outputrow).Value = PercentChange & "%"

                ' format cell color based on yearchange value
                If YearChange < 0 Then
                    ws.Range("K" & outputrow).Interior.ColorIndex = 3
                Else
                    ws.Range("K" & outputrow).Interior.ColorIndex = 4
                End If

                ' if this is the first stock, set global min and max to current percent change
                If outputrow = 2 Then
                    GreatestDecrease = PercentChange
                    GreatestIncrease = PercentChange
                    GreatestVolume = VolumeTotal
                ' otherwise check if global min and max need to be set to this stock
                Else
                    If PercentChange > GreatestIncrease Then
                        GreatestIncrease = PercentChange
                        ws.Range("O2").Value = CurrentSymbol
                        ws.Range("P2").Value = PercentChange & "%"
                    End If
                    If PercentChange < GreatestDecrease Then
                        GreatestDecrease = PercentChange
                        ws.Range("O3").Value = CurrentSymbol
                        ws.Range("P3").Value = PercentChange & "%"
                    End If
                    If VolumeTotal > GreatestVolume Then
                        GreatestVolume = VolumeTotal
                        ws.Range("O4").Value = CurrentSymbol
                        ws.Range("P4").Value = GreatestVolume
                    End If
                End If

                ' advance row for writing output for next stock symbol
                outputrow = outputrow + 1
                ' reset total and set current stock to next stock symbol
                VolumeTotal = 0
                CurrentSymbol = NextSymbol
                YearOpen = ws.Cells(Row + 1, 3).Value
            End If
        Next Row
        ' change style for percentage
        ws.Range("L:L").NumberFormat = "0.00%"
        ws.Range("P2").NumberFormat = "0.00%"
        ws.Range("P3").NumberFormat = "0.00%"
        ws.Columns("A:P").AutoFit
    Next ws
End Sub




