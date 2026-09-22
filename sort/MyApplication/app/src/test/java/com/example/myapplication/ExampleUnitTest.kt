package com.example.myapplication

import org.junit.Test
import org.junit.Assert.*

class ExampleUnitTest {
    @Test
    fun bubbleSort_sortsNumbersCorrectly() {
        val input = listOf(6, 2, 8, 1, 9, 3)
        val expected = listOf(1, 2, 3, 6, 8, 9)
        assertEquals(expected, bubbleSort(input))
    }

    @Test
    fun bubbleSort_handlesAlreadySortedList() {
        val input = listOf(1, 2, 3, 4, 5)
        assertEquals(input, bubbleSort(input))
    }

    @Test
    fun bubbleSort_handlesEmptyAndSingleElementList() {
        assertEquals(emptyList<Int>(), bubbleSort(emptyList()))
        assertEquals(listOf(42), bubbleSort(listOf(42)))
    }
}
