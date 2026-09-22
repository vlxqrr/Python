package com.example.sort

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
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
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
            Sort()
        }
    }
}

@Preview(showBackground = true)
@Composable
fun Sort() {
    var userInput by remember { mutableStateOf("") }
    var sortedResult by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize()
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
                color = textColor,
                fontSize = 20.sp
            )
        }

        Box(
            modifier = Modifier
                .padding(top = 24.dp)
                .fillMaxWidth()
                .background(bgColor)
                .padding(16.dp)
        ) {
            Column(
                horizontalAlignment = Alignment.CenterHorizontally,
                modifier = Modifier.fillMaxWidth()
            ) {
                Text(
                    text = "Podaj 6 liczb po przecinku:",
                    color = textColor,
                    fontSize = 16.sp
                )
                Spacer(modifier = Modifier.height(8.dp))
                TextField(
                    value = userInput,
                    onValueChange = { userInput = it }
                )
                Spacer(modifier = Modifier.height(24.dp))

                Button(
                    onClick = {
                        val numbers = userInput.split(",")
                            .mapNotNull { it.trim().toIntOrNull() }
                            .toMutableList()

                        // BubbleSort
                        for (i in 0 until numbers.size - 1) {
                            for (j in 0 until numbers.size - 1 - i) {
                                if (numbers[j] > numbers[j + 1]) {
                                    val temp = numbers[j]
                                    numbers[j] = numbers[j + 1]
                                    numbers[j + 1] = temp
                                }
                            }
                        }

                        sortedResult = numbers.joinToString(", ")
                    },
                    modifier = Modifier.fillMaxWidth(),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = btnColor,
                        contentColor = textColor
                    )
                ) {
                    Text(
                        text = "BubbleSort",
                        fontSize = 16.sp
                    )
                }

                if (sortedResult.isNotEmpty()) {
                    Spacer(modifier = Modifier.height(16.dp))
                    Text(
                        text = "Wynik: $sortedResult",
                        color = textColor,
                        fontSize = 18.sp
                    )
                }
            }
        }
    }
}
