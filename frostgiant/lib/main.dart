import 'package:flutter/material.dart';
import 'package:frostgiant/screens/home_screen.dart';

void main() {
  runApp(const FrostGiant());
}

class FrostGiant extends StatelessWidget {
  const FrostGiant({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: HomeScreen(),
    );
  }
}
