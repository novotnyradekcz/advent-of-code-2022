package `4`

import java.io.File

fun main() {
    val fileName = "4\\input.txt"
    val lines = File(fileName).readLines()
    var total = 0
    // part one
    for (line in lines) {
        val sections = line.split(",")  //  [1-2, 3-4]
        val firstElf = sections[0].split("-")   //  [1, 2]
        val secondElf = sections[1].split("-")  //  [3, 4]
        if ((firstElf[0].toInt() <= secondElf[0].toInt() && firstElf[1].toInt() >= secondElf[1].toInt()) ||
            (firstElf[0].toInt() >= secondElf[0].toInt() && firstElf[1].toInt() <= secondElf[1].toInt())) total++
    }
    println(total)
    // part two
    total = 0
    for (line in lines) {
        val sections = line.split(",")  //  [1-2, 3-4]
        val firstElf = sections[0].split("-")   //  [1, 2]
        val secondElf = sections[1].split("-")  //  [3, 4]
        if ((firstElf[1].toInt() >= secondElf[0].toInt() && firstElf[0].toInt() <= secondElf[1].toInt()) ||
            (secondElf[1].toInt() >= firstElf[0].toInt() && secondElf[0].toInt() <= firstElf[1].toInt())) total++
    }
    println(total)
}