import 'package:flutter/material.dart';
import 'package:frostgiant/screens/results%20screen.dart';
import 'package:frostgiant/services/services.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  TextEditingController promptController = TextEditingController();
  bool isLoading = false;

  void sendPrompt() async {
    if (promptController.text.isEmpty) return;

    setState(() => isLoading = true);

    final response = await ApiService.sendPrompt(promptController.text);

    setState(() => isLoading = false);

    if (response != null) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ResultsScreen(response: response),
        ),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text("Error fetching AI response")),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("AI Fine-Tuning Demo")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            CustomTextField(
              controller: promptController,
              hintText: "Enter your prompt...",
            ),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: isLoading ? null : sendPrompt,
              child:
                  isLoading
                      ? CircularProgressIndicator()
                      : Text("Generate Response"),
            ),
          ],
        ),
      ),
    );
  }
}

class CustomTextField extends StatelessWidget {
  final TextEditingController controller;
  final String hintText;

  const CustomTextField({super.key,  required this.controller, required this.hintText});

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: controller,
      decoration: InputDecoration(
        hintText: hintText,
        border: OutlineInputBorder(),
      ),
    );
  }
}
