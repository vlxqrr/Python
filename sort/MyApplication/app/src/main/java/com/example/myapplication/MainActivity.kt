package com.example.myapplication

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

val bgColor = Color(0xFFC4B8B1)
val boxColor = Color(0xFF1D70A5)
val btnColor = Color(0xFF7D74F1)
val textColor = Color(0xFF1F191E)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    Sort()
                }
            }
        }
    }
}

fun bubbleSort(list: List<Int>): List<Int> {
    val numbers = list.toMutableList()
    for (i in 0 until numbers.size - 1) {
        for (j in 0 until numbers.size - 1 - i) {
            if (numbers[j] > numbers[j + 1]) {
                val temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            }
        }
    }
    return numbers
}
fun selectionSort(list: List<Int>): List<Int> {
    val numbers = list.toMutableList()
    
    return numbers
}

@Preview(showBackground = true)
@Composable
fun Sort() {
    var userInput by remember { mutableStateOf("") }
    var sortedResult by remember { mutableStateOf("") }
    var errorMessage by remember { mutableStateOf("") }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(bgColor)
            .verticalScroll(rememberScrollState())
    ) {
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(80.dp)
                .background(boxColor),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = "Sortowanie",
                color = Color.White,
                fontSize = 22.sp,
                fontWeight = FontWeight.Bold
            )
        }

        Card(
            modifier = Modifier
                .padding(16.dp)
                .fillMaxWidth(),
            shape = RoundedCornerShape(12.dp),
            colors = CardDefaults.cardColors(containerColor = Color.White),
            elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
        ) {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(20.dp)
            ) {
                Text(
                    text = "Podaj 6 liczb po przecinku:",
                    color = textColor,
                    fontSize = 16.sp,
                    fontWeight = FontWeight.Medium
                )
                Spacer(modifier = Modifier.height(12.dp))

                OutlinedTextField(
                    value = userInput,
                    onValueChange = {
                        userInput = it
                        errorMessage = ""
                    },
                    placeholder = { Text("np. 12, 5, 3, 8, 1, 9") },
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth()
                )

                if (errorMessage.isNotEmpty()) {
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(
                        text = errorMessage,
                        color = Color.Red,
                        fontSize = 14.sp
                    )
                }

                Spacer(modifier = Modifier.height(20.dp))

                Button(
                    onClick = {
                        val parsedNumbers = userInput.split(",")
                            .map { it.trim() }
                            .filter { it.isNotEmpty() }
                            .mapNotNull { it.toIntOrNull() }

                        if (parsedNumbers.isEmpty()) {
                            errorMessage = "Wprowadź poprawne liczby oddzielone przecinkami!"
                            sortedResult = ""
                        } else {
                            errorMessage = ""
                            val sorted = bubbleSort(parsedNumbers)
                            sortedResult = sorted.joinToString(", ")
                        }
                    },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(48.dp),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = btnColor,
                        contentColor = Color.White
                    ),
                    shape = RoundedCornerShape(8.dp)
                ) {
                    Text(
                        text = "BubbleSort",
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold
                    )
                }
                Spacer(modifier = Modifier.height(12.dp))
                Button(
                    onClick = {
                        val parsedNumbers = userInput.split(",")
                            .map { it.trim() }
                            .filter { it.isNotEmpty() }
                            .mapNotNull { it.toIntOrNull() }

                        if (parsedNumbers.isEmpty()) {
                            errorMessage = "Wprowadź poprawne liczby oddzielone przecinkami!"
                            sortedResult = ""
                        } else {
                            errorMessage = ""
                            val sorted = bubbleSort(parsedNumbers)
                            sortedResult = sorted.joinToString(", ")
                        }
                    },
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(48.dp),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = btnColor,
                        contentColor = Color.White
                    ),
                    shape = RoundedCornerShape(8.dp)
                ) {
                    Text(
                        text = "SelectionSort",
                        fontSize = 16.sp,
                        fontWeight = FontWeight.Bold
                    )
                }

                if (sortedResult.isNotEmpty()) {
                    Spacer(modifier = Modifier.height(20.dp))
                    Text(
                        text = "Wynik: $sortedResult",
                        color = textColor,
                        fontSize = 18.sp,
                        fontWeight = FontWeight.SemiBold
                    )
                }
            }
        }
    }
}
