package `1`

import java.io.File

fun main() {
    val fileName = "1\\input.txt"
    val lines = File(fileName).readLines()
    var calories = 0
    val maxima = mutableListOf<Int>()
    for (line in lines) {
        if (line == "") {
            maxima.add(calories)
            calories = 0
        } else {
            calories += line.toInt()
        }
    }
    var topThree = 0
    topThree += maxima.max()
    println(maxima.max())   // highest
    maxima.remove(maxima.max())
    topThree += maxima.max()
    println(maxima.max())   // second highest
    maxima.remove(maxima.max())
    topThree += maxima.max()
    println(maxima.max())   // third highest
    println(topThree)   // sum of top three
}