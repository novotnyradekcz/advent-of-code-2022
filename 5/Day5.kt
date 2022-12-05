package `5`

import java.io.File

fun main() {
    val fileName = "5\\input.txt"
    val lines = File(fileName).readLines()
    // part one
    val columns = mutableListOf<MutableList<Char>>()
    columns.add(mutableListOf('R', 'P', 'C', 'D', 'B', 'G'))
    columns.add(mutableListOf('H', 'V', 'G'))
    columns.add(mutableListOf('N', 'S', 'Q', 'D', 'J', 'P', 'M'))
    columns.add(mutableListOf('P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'))
    columns.add(mutableListOf('J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'))
    columns.add(mutableListOf('Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'))
    columns.add(mutableListOf('B', 'Z', 'M', 'H', 'F', 'T', 'Q'))
    columns.add(mutableListOf('C', 'M', 'D', 'B', 'F'))
    columns.add(mutableListOf('F', 'C', 'Q', 'G'))
    /*
    for (line in lines) {
        // move: 5(6), from: 12(13), to 17(18)
        val move: Int
        val from: Int
        val to: Int
        if (line[6] != ' ') {
            move = line.substring(5, 7).toInt()
            from = line[13].toString().toInt()
            to = line[18].toString().toInt()
        }
        else {
            move = line.substring(5, 6).toInt()
            from = line[12].toString().toInt()
            to = line[17].toString().toInt()
        }
        for (i in 1..move) {
            columns[to - 1].add(columns[from - 1].last())
            columns[from - 1].removeLast()
        }
    }
    for (column in columns) print(column.last())
    */
    // part two
    for (line in lines) {
        // move: 5(6), from: 12(13), to 17(18)
        val move: Int
        val from: Int
        val to: Int
        if (line[6] != ' ') {
            move = line.substring(5, 7).toInt()
            from = line[13].toString().toInt()
            to = line[18].toString().toInt()
        }
        else {
            move = line.substring(5, 6).toInt()
            from = line[12].toString().toInt()
            to = line[17].toString().toInt()
        }
        columns[to - 1].addAll(columns[from - 1].subList(columns[from - 1].size - move, columns[from - 1].lastIndex + 1))
        for (i in 1..move) {
            columns[from - 1].removeLast()
        }
    }
    for (column in columns) print(column.last())
}