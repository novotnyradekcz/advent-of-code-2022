package `3`

import java.io.File

fun main() {
    val fileName = "3\\input.txt"
    val lines = File(fileName).readLines()
    var total = 0
    val lower = "abcdefghijklmnopqrstuvwxyz"
    val upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    // part one
    for (line in lines) {
        var temp = ' '
        for (i in 0 until line.length / 2) {
            for (j in line.length / 2 until line.length) {
                if (line[i] == line[j] && line[i] != temp) {
                    if (line[i] in lower) total += lower.indexOf(line[i]) + 1
                    if (line[i] in upper) total += upper.indexOf(line[i]) + 27
                    temp = line[i]
                }
            }
        }
    }
    println(total)
    // part two
    total = 0
    var i = 0
    while (i < lines.size - 2) {
        var temp = ' '
        for (j in lower) {
            if (j in lines[i] && j in lines[i + 1] && j in lines[i + 2] && j != temp) {
                total += lower.indexOf(j) + 1
                temp = j
            }
        }
        for (j in upper) {
            if (j in lines[i] && j in lines[i + 1] && j in lines[i + 2] && j != temp) {
                total += upper.indexOf(j) + 27
                temp = j
            }
        }
        i += 3
    }
    println(total)
}