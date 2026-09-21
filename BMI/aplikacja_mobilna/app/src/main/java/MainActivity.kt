package com.example.calculatorbmi

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
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TextFieldDefaults
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


val DarkNavyBackground = Color(0xFF232338)
val UnderweightBlue = Color(0xFF3F4E6E)
val NormalWeightBlue = Color(0xFF5A6E94)
val OverweightBlue = Color(0xFF7B8BAE)
val ObeseBlue = Color(0xFFA6B6D4)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            CalculatorBMI()
        }
    }
}

@Preview(showBackground = true)
@Composable
fun CalculatorBMI() {
    // Stan pól wejściowych i wyników
    var heightInput by remember { mutableStateOf("") }
    var weightInput by remember { mutableStateOf("") }
    var bmiResult by remember { mutableStateOf("") }
    var interpretation by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize()
    ) {

        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(80.dp)
                .background(UnderweightBlue),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = "Kalkulator BMI",
                color = ObeseBlue,
                fontSize = 20.sp
            )
        }


        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(DarkNavyBackground),
            contentAlignment = Alignment.TopCenter
        ) {

            Box(
                modifier = Modifier
                    .padding(top = 24.dp)
                    .fillMaxWidth(0.88f)
                    .background(
                        color = UnderweightBlue,
                        shape = RoundedCornerShape(20.dp)
                    )
                    .padding(horizontal = 20.dp, vertical = 24.dp),
                contentAlignment = Alignment.Center
            ) {
                Column(
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Text(
                        text = "Wzrost (w metrach):",
                        color = ObeseBlue,
                        fontSize = 15.sp,
                        modifier = Modifier.fillMaxWidth().padding(bottom = 6.dp)
                    )
                    TextField(
                        value = heightInput,
                        onValueChange = { heightInput = it },
                        modifier = Modifier.fillMaxWidth(),
                        shape = RoundedCornerShape(12.dp),
                        colors = TextFieldDefaults.colors(
                            focusedTextColor = ObeseBlue,
                            unfocusedTextColor = ObeseBlue,
                            focusedContainerColor = DarkNavyBackground,
                            unfocusedContainerColor = DarkNavyBackground,
                            focusedIndicatorColor = Color.Transparent,
                            unfocusedIndicatorColor = Color.Transparent
                        )
                    )

                    Spacer(modifier = Modifier.height(16.dp))

                    Text(
                        text = "Waga (w kg):",
                        color = ObeseBlue,
                        fontSize = 15.sp,
                        modifier = Modifier.fillMaxWidth().padding(bottom = 6.dp)
                    )
                    TextField(
                        value = weightInput,
                        onValueChange = { weightInput = it },
                        modifier = Modifier.fillMaxWidth(),
                        shape = RoundedCornerShape(12.dp),
                        colors = TextFieldDefaults.colors(
                            focusedTextColor = ObeseBlue,
                            unfocusedTextColor = ObeseBlue,
                            focusedContainerColor = DarkNavyBackground,
                            unfocusedContainerColor = DarkNavyBackground,
                            focusedIndicatorColor = Color.Transparent,
                            unfocusedIndicatorColor = Color.Transparent
                        )
                    )

                    Spacer(modifier = Modifier.height(24.dp))

                    Button(
                        onClick = {
                            val height = heightInput.toFloatOrNull()
                            val weight = weightInput.toFloatOrNull()

                            if (height != null && weight != null && height > 0f &&
                                height in 0.5f..2.5f && weight in 2f..300f
                            ) {
                                val bmi = weight / (height * height)
                                bmiResult = "Twoje BMI: %.2f".format(bmi)

                                interpretation = if (bmi < 18.5f) {
                                    "Niedowaga"
                                } else if (bmi in 18.5f..24.9f) {
                                    "Waga prawidłowa"
                                } else if (bmi in 25.0f..29.9f) {
                                    "Nadwaga"
                                } else {
                                    "Otyłość"
                                }
                            } else {
                                bmiResult = "Błędne dane"
                                interpretation = ""
                            }
                        },
                        shape = RoundedCornerShape(12.dp),
                        colors = ButtonDefaults.buttonColors(
                            containerColor = NormalWeightBlue,
                            contentColor = ObeseBlue
                        ),
                        modifier = Modifier.fillMaxWidth().height(48.dp)
                    ) {
                        Text("Oblicz", fontSize = 16.sp)
                    }

                    if (bmiResult.isNotEmpty()) {
                        Spacer(modifier = Modifier.height(20.dp))
                        Text(
                            text = bmiResult,
                            color = ObeseBlue,
                            fontSize = 18.sp
                        )
                        Text(
                            text = interpretation,
                            color = OverweightBlue,
                            fontSize = 16.sp
                        )
                    }
                }
            }
        }
    }
}