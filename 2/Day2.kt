package `2`

import java.io.File

fun main() {
    // part two
    val fileName = "2\\input.txt"
    val lines = File(fileName).readLines()
    var score = 0
    for (line in lines) {
        when (line[2]) {
            'X' -> {
                score += 0  // lose
                if (line[0] == 'A') score += 3  // scissors
                if (line[0] == 'B') score += 1  // rock
                if (line[0] == 'C') score += 2  // paper
            }
            'Y' -> {
                score += 3  // draw
                if (line[0] == 'A') score += 1  // rock
                if (line[0] == 'B') score += 2  // paper
                if (line[0] == 'C') score += 3  // scissors
            }
            'Z' -> {
                score += 6  // win
                if (line[0] == 'A') score += 2  // paper
                if (line[0] == 'B') score += 3  // scissors
                if (line[0] == 'C') score += 1  // rock
            }
        }
    }
    println(score)
}