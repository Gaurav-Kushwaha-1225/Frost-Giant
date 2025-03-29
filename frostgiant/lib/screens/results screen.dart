import 'package:flutter/material.dart';

class ResultsScreen extends StatelessWidget {
  final String response;
  const ResultsScreen({super.key, required this.response});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("AI Response")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text(response, style: const TextStyle(fontSize: 18)),
      ),
    );
  }
}

class AIResponse {
  final String prompt;
  final String response;

  AIResponse({required this.prompt, required this.response});

  factory AIResponse.fromJson(Map<String, dynamic> json) {
    return AIResponse(
      prompt: json["prompt"],
      response: json["response"],
    );
  }
}
