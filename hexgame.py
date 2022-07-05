#!/usr/bin/env python

default_rows = 9
default_columns = 9

no_player = 0
first_player = 1
second_player = 2

diamond_board = 1
horizontal_board = 2
vertical_board = 3

def printBoard(gameBoard, boardType=diamond_board):


    boardSwitch = boardType

    if boardSwitch == diamond_board:

        first_piece = "><"
        second_piece = "()"

        rowStart = gameBoard.getRowCount()
        columnStart = 0

        rowEnd = gameBoard.getRowCount()
        columnEnd = 1

        currentLine = "\n" + "   "*(rowStart-1) + " " + chr(65+rowStart-1) + "  __ " + second_piece
        print(currentLine)

        for lineIndex in range(0, gameBoard.getRowCount()+gameBoard.getColumnCount()):

            currentLine = ""

            if rowStart:

                if rowStart-1:
                    currentLine += "   "*(rowStart-2) + " " + chr(65+rowStart-2) + "  __"
                else:
                    currentLine += "   "*(rowStart)

                if not columnEnd <= gameBoard.getColumnCount():
                    currentLine += "/"

                rowStart -= 1

            else:

                if columnStart:
                    currentLine += "   "*(columnStart-1) + " " + str(columnStart).ljust(2, " ") + "   \\__"
                else:
                    currentLine += "   "*(columnStart) + "   \\__"

                if not columnEnd <= gameBoard.getColumnCount():
                    currentLine += "/"

                columnStart += 1

            if columnEnd <= gameBoard.getColumnCount():

                for loopIndex in range(columnStart, columnEnd):

                    if rowStart:
                        rowIndex = loopIndex+rowStart
                    else:
                        rowIndex = loopIndex-columnStart

                    columnIndex = loopIndex

                    if gameBoard.getCell(rowIndex, columnIndex) == first_player:
                        currentLine += "/" + first_piece + "\\"
                    elif gameBoard.getCell(rowIndex, columnIndex) == second_player:
                        currentLine += "/" + second_piece + "\\"
                    else:
                        currentLine += "/  \\"

                    if loopIndex < gameBoard.getColumnCount()-1:
                        currentLine += "__"

                if columnEnd != gameBoard.getColumnCount():
                    currentLine += " " + second_piece

                columnEnd += 1

            else:

                cellEnd = rowEnd-1

                if cellEnd > gameBoard.getColumnCount():
                    cellEnd = gameBoard.getColumnCount()

                for loopIndex in range(0, cellEnd):

                    rowIndex = loopIndex+rowStart
                    columnIndex = loopIndex+columnStart

                    if gameBoard.getCell(rowIndex, columnIndex) == first_player:
                        currentLine += first_piece + "\\__/"
                    elif gameBoard.getCell(rowIndex, columnIndex) == second_player:
                        currentLine += second_piece + "\\__/"
                    else:
                        currentLine += "  \\__/"

                if rowEnd != gameBoard.getRowCount():
                    currentLine += "   " + first_piece

                rowEnd -= 1

            print(currentLine)

        print("   "*(gameBoard.getColumnCount()-1) + " " + str(gameBoard.getColumnCount()).ljust(2, " ") + "    " + first_piece + "\n")

    elif boardSwitch == horizontal_board:

        first_piece = "X"
        second_piece = "O"

        print("\n" + "  "*(gameBoard.getRowCount()-1) + " " + "   ."*gameBoard.getRowCount())
        print("  "*gameBoard.getRowCount() + " " + "/ \\ "*gameBoard.getColumnCount())

        for rowIndex in range(gameBoard.getRowCount()-1, -1, -1):

                if rowIndex:
                        print("  "*(rowIndex-1) + " ", end=' ')

                print(chr(65+rowIndex), end=' ')

                for columnIndex in range (0, gameBoard.getColumnCount()):
                        if gameBoard.getCell(rowIndex, columnIndex) == first_player:
                                print("| " + first_piece, end=' ')
                        elif gameBoard.getCell(rowIndex, columnIndex) == second_player:
                                print("| " + second_piece, end=' ')
                        else:
                                print("|  ", end=' ')

                print("|")

                if rowIndex != 0:
                        print("  "*rowIndex + " " + "/ \\ "*gameBoard.getColumnCount() + "/")
                else:
                        print("  "*rowIndex + "  " + " \\ /"*gameBoard.getColumnCount())

        print(" " + "   '"*gameBoard.getColumnCount())

        for columnIndex in range (0, gameBoard.getColumnCount()):
                print("  " + str(columnIndex+1), end=' ')

        print("\n\n", end=' ')

class HexBoard:

    def cSetRowCount(self, rows):
        if rows > 0:
            self.boardRows = rows
        else:
            self.boardRows = default_rows

    def cSetColumnCount(self, columns):
        if columns > 0:
            self.boardColumns = columns
        else:
            self.boardColumns = default_columns

    def clearHexCells(self):

        tempList = [no_player]*self.boardColumns

        self.hexCells = []

        for index in range(0, self.boardRows):
            self.hexCells.append(tempList[:])

    def setRowCount(self, rows):
        self.cSetRowCount(rows)
        self.clearHexCells()

    def setColumnCount(self, columns):
        self.cSetColumnCount(columns)
        self.clearHexCells()

    def setCell(self, row, column, cellValue):
        if cellValue in (no_player, first_player, second_player):
            self.hexCells[row][column] = cellValue

    def setPlayer(self, playerIn):
        if playerIn in (first_player, second_player):
            self.currentPlayer = playerIn

    def getRowCount(self):
        return self.boardRows

    def getColumnCount(self):
        return self.boardColumns

    def getCell(self, row, column):

                if row in range(0, self.boardRows) and column in range(0, self.boardColumns):
                        return self.hexCells[row][column]
                else:
                        return None

    def getPlayer(self):
        return self.currentPlayer

    def initHexBoard(self, rows, columns):

        self.cSetRowCount(rows)
        self.cSetColumnCount(columns)

        self.currentPlayer = first_player

        self.clearHexCells()

    def gameWon(self):

        gameWinner = no_player

        rowIndex = 0
        columnIndex = 0

        while gameWinner == no_player and rowIndex < self.boardRows:

            prevRowIndex = rowIndex

            if self.getCell(rowIndex, columnIndex) == first_player:

                previousCell = 1

                while gameWinner == no_player:

                    cellIndex = 0
                    foundNextCell = False

                    while cellIndex < 6 and foundNextCell == False:

                        switchCell = (((previousCell+cellIndex)%6)+1)

                        if switchCell ==  1:
                            if rowIndex-1 >= 0 and self.getCell(rowIndex-1, columnIndex) == first_player:
                                foundNextCell = True
                                previousCell = 4
                                rowIndex -= 1

                        elif switchCell == 2:
                            if rowIndex-1 >= 0 and columnIndex+1 < self.boardColumns and self.getCell(rowIndex-1, columnIndex+1) == first_player:
                                foundNextCell = True
                                previousCell = 5
                                rowIndex -= 1
                                columnIndex += 1

                        elif switchCell == 3:
                            if columnIndex+1 < self.boardColumns and self.getCell(rowIndex, columnIndex+1) == first_player:
                                foundNextCell = True
                                previousCell = 6
                                columnIndex += 1

                        elif switchCell == 4:
                            if rowIndex+1 < self.boardRows and self.getCell(rowIndex+1, columnIndex) == first_player:
                                foundNextCell = True
                                previousCell = 1
                                rowIndex += 1

                        elif switchCell == 5:
                            if rowIndex+1 < self.boardRows and columnIndex-1 >= 0 and self.getCell(rowIndex+1, columnIndex-1) == first_player:
                                foundNextCell = True
                                previousCell = 2
                                rowIndex += 1
                                columnIndex -= 1

                        elif switchCell == 6:
                            if columnIndex-1 >= 0 and self.getCell(rowIndex, columnIndex-1) == first_player:
                                foundNextCell = True
                                previousCell = 3
                                columnIndex -= 1

                        cellIndex += 1

                    if columnIndex >= self.boardColumns-1:
                        gameWinner = first_player
                    elif gameWinner == no_player and columnIndex == 0 and rowIndex == prevRowIndex:
                        break

            rowIndex += 1

        rowIndex = 0
        columnIndex = 0

        while gameWinner == no_player and columnIndex < self.boardColumns:

            prevColumnIndex = columnIndex

            if self.getCell(rowIndex, columnIndex) == second_player:

                previousCell = 1

                while gameWinner == no_player:

                    cellIndex = 0
                    foundNextCell = False

                    while cellIndex < 6 and foundNextCell == False:

                        switchCell = (((previousCell+cellIndex)%6)+1)

                        if switchCell == 1:
                            if columnIndex-1 >= 0 and self.getCell(rowIndex, columnIndex-1) == second_player:
                                foundNextCell = True
                                previousCell = 4
                                columnIndex -= 1

                        elif switchCell == 2:
                            if rowIndex+1 < self.boardRows and columnIndex-1 >= 0 and self.getCell(rowIndex+1, columnIndex-1) == second_player:
                                foundNextCell = True
                                previousCell = 5
                                rowIndex += 1
                                columnIndex -= 1

                        elif switchCell == 3:
                            if rowIndex+1 < self.boardRows and self.getCell(rowIndex+1, columnIndex) == second_player:
                                foundNextCell = True
                                previousCell = 6
                                rowIndex += 1

                        elif switchCell == 4:
                            if columnIndex+1 < self.boardColumns and self.getCell(rowIndex, columnIndex+1) == second_player:
                                foundNextCell = True
                                previousCell = 1
                                columnIndex += 1

                        elif switchCell == 5:
                            if rowIndex-1 >= 0 and columnIndex+1 < self.boardColumns and self.getCell(rowIndex-1, columnIndex+1) == second_player:
                                foundNextCell = True
                                previousCell = 2
                                rowIndex -= 1
                                columnIndex += 1

                        elif switchCell == 6:
                            if rowIndex-1 >= 0 and self.getCell(rowIndex-1, columnIndex) == second_player:
                                foundNextCell = True
                                previousCell = 3
                                rowIndex -= 1

                        cellIndex += 1

                    if rowIndex >= self.boardRows-1:
                        gameWinner = second_player
                    elif gameWinner == no_player and rowIndex == 0 and columnIndex == prevColumnIndex:
                        break

            columnIndex += 1

        return gameWinner

    def __init__(self, rows=default_rows, columns=default_columns):
        self.initHexBoard(rows, columns)

if __name__ == "__main__":

        gameBoard = HexBoard(7, 7)

        boardType = diamond_board
        errorMessage = ""

        while not gameBoard.gameWon():

                printBoard(gameBoard, boardType)

                if errorMessage:
                        print(errorMessage + "-", end=' ')
                        errorMessage = ""

                if gameBoard.getPlayer() == first_player:
                        gameMove = input("First Player Move: ").strip().upper()
                elif gameBoard.getPlayer() == second_player:
                        gameMove = input("Second Player Move: ").strip().upper()

                if not gameMove[:1] in [chr(65+moveRow) for moveRow in range(0, gameBoard.getRowCount())]:
                        errorMessage += "Row not valid. "
                else:
                        moveRow = ord(gameMove[:1])-65

                if not gameMove[1:] in [str(columnItem) for columnItem in range(1, gameBoard.getColumnCount()+1)]:
                        errorMessage += "Column not valid. "
                else:
                        moveColumn = int(gameMove[1:])-1

        if gameBoard.getCell(moveRow, moveColumn) != no_player:
                errorMessage += "Cell is already taken. "

                if not errorMessage:

                        gameBoard.setCell(moveRow, moveColumn, gameBoard.getPlayer())

                        if gameBoard.getPlayer() == first_player:
                                gameBoard.setPlayer(second_player)
                        elif gameBoard.getPlayer() == second_player:
                                gameBoard.setPlayer(first_player)


                if gameBoard.gameWon():

                        printBoard(gameBoard, boardType)

                        if gameBoard.gameWon() == first_player:
                                print("First Player Won!")
                        elif gameBoard.gameWon() == second_player:
                                print("Second Player Won!")
